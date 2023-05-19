import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, HTTPException
import yfinance as yf

app = FastAPI()

valid_intervals = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
valid_periods = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]


@app.get("/stockPrices/getAll/{value}")
async def stock_prices(value: str):
    default_interval = '3mo'
    default_period = 'max'

    st = yf.Ticker(value)
    info = st.info
    data = st.history(interval=default_interval, period=default_period)
    df = data["Open"]
    trade_prices = df.to_json(orient="table")
    trade_prices = jsonable_encoder(trade_prices)
    info["trade_prices"] = trade_prices

    # Serializing json
    json_object = jsonable_encoder(info)
    return JSONResponse(content=json_object)


@app.get("/stockPrices/{value}/interval/{interval}/period/{period}")
async def stock_prices_in_range(value: str, interval: str, period: str):
    default_interval = '3mo'
    default_period = 'max'

    if interval not in valid_intervals:
        interval = default_interval

    if period not in valid_periods:
        period = default_period

    st = yf.Ticker(value)
    info = st.info
    data = st.history(interval=interval, period=period)
    df = data["Open"]
    trade_prices = df.to_json(orient="table")
    trade_prices = jsonable_encoder(trade_prices)
    info["trade_prices"] = trade_prices

    # Serializing json
    json_object = jsonable_encoder(info)
    return JSONResponse(content=json_object)

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
