import yfinance as yf
import datetime
import streamlit as st
import plotly.graph_objects as go

#https://streamlit.io/gallery 여기 들어가면 사용법 다양

# streamlit run 웹개발_주식차트.py
st.write("# 주식차트")

ticker = st.text_input("티커(주식이름) 입력 >> (ex:AAPL, 005930.KS(samsung)) ")
data = yf.Ticker(ticker)
today = datetime.datetime.today().strftime("%Y-%m-%d")
df = data.history(period="1d",start="2015-01-01",end=today)
st.dataframe(df)

st.write("##종가 기준")
st.line_chart(df['Close'])
st.bar_chart(df["Volume"])

st.write("## 캔들차트")

candle = go.Candlestick(x=df.index, open=df["Open"],
               close=df["Close"], high=df["High"],
               low = df["Low"])
layout = go.Layout(yaxis={"fixedrange":False})
fig = go.Figure(data=[candle], layout=layout)
st.plotly_chart(fig)
