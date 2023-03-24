import streamlit as st
import yfinance as fy
import plotly.graph_objects as go
import util

if __name__ == '__main__': 
    ticker_symbol = st.sidebar.text_input(
        "Please enter the stock symbol", "MSFT"
        )
    data_period = st.sidebar.text_input('Period','10d')
    data_interval = st.sidebar.radio('Interval',['15m','30m','1h','1d','5d'])


    st.header(ticker_symbol)
    ticker_data=util.get_ticker_data(ticker_symbol,data_period,data_interval)

    ticker_data

    util.plot_candle_chart(ticker_data)
