import streamlit as st
import plotly.graph_objects as go
import plotly.express as px 
import yfinance as yf


def get_ticker_data(ticker_symbol,data_period, data_interval):
    ticker_data =yf.download(tickers=ticker_symbol,period=data_period,interval=data_interval)
    if len(ticker_data) == 0 :
        st.write('Could not find the ticker data. Modify ticker symbol or reduce the period value')
    else:
        #format the x-axis to skip dates with missing values
        ticker_data.index = ticker_data.index.strftime("%d-%m-%Y %H:%M")
        
    return ticker_data

def plot_candle_chart(ticker_data):
    candle_fig = go.Figure()
    candle_fig.add_trace(go.Candlestick(x=ticker_data.index,
                                 open=ticker_data['Open'],
                                 high=ticker_data['High'],
                                 low=ticker_data['Low'],
                                 close=ticker_data['Close'],
                                 name='Amau Market Data'))
    candle_fig.update_layout(height=800)
    st.write(candle_fig)
    
