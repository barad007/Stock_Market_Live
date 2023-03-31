import main
from main import stock_prices
import yfinance as yf


def test_stock_prices():
    value = "MCB"
    st = yf.Ticker(value)
    info = st.info
    assert value == info.get('symbol')




