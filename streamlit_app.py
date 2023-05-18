import streamlit as st
import pandas as pd
import yfinance as yf


st.write("""

# A simple Stock Price Application

We have the *Stock closing price* and the *volume* of Google!
**Enjoy**

""" )

#Define the ticker symbol
tickerSymbol = 'GOOGL'

#Get data on this ticker
tickerData=yf.Ticker(tickerSymbol)

#Get historical prices for this ticker
tickerDf=tickerData.history(persiod='1d',start='2010-5-31',end='2020-5-31')

#Variables obtained
#Open High Low Close Volume Dividents Stock Splits

#line plots
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


