import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from pydantic import BaseModel
import json
import pandas as pd
import yfinance as yf

app = FastAPI()

@app.get("/{value}")
async def stock_prices(value: str):
    # interval - data interval: “1m”, “2m”, “5m”, “15m”, “30m”, “60m”, “90m”, “1h”, “1d”, “5d”, “1wk”, “1mo”, “3mo”
    interval = '5m'
    # period - data period to download: “1d”, “5d”, “1mo”, “3mo”, “6mo”, “1y”, “2y”, “5y”, “10y”, “ytd”, “max”
    period = '1d'

    st = yf.Ticker(value)
    info = st.info
    data = st.history(interval=interval, period=period)
    df = data["Open"]
    trade_prices = df.to_json(orient="table")
    info["trade_prices"] = trade_prices

    # Serializing json
    json_object = jsonable_encoder(info)
    return JSONResponse(content=json_object)

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
