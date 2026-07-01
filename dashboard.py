import streamlit as st
import plotly.graph_objects as go
import json
import pandas as pd
from datetime import datetime
import time
from collections import defaultdict, deque
import os

st.set_page_config(page_title="Crypto Analytics", layout="wide")
st.title("Real-Time Cryptocurrency Analytics Dashboard")

if 'data' not in st.session_state:
    st.session_state.data = defaultdict(lambda: deque(maxlen=100))
    st.session_state.count = 0

try:
    if os.path.exists('crypto_stream.json'):
        with open('crypto_stream.json', 'r') as f:
            records = json.load(f)
            for record in records:
                st.session_state.data[record['coin']].append({
                    'time': pd.to_datetime(record['timestamp']),
                    'price': record['price_usd'],
                    'change': record['price_change_24h'],
                    'volume': record['volume_24h']
                })
                st.session_state.count += 1
except:
    pass

with st.sidebar:
    st.title("Dashboard Controls")
    st.metric("Total Updates", st.session_state.count)
    st.metric("Active Coins", len(st.session_state.data))
    st.info("Tech Stack: Python Streaming, Sentiment Analysis, Real-time Viz")

if not st.session_state.data:
    st.warning("Waiting for data... Start producer!")
    st.code("python producer_simple.py")
else:
    st.subheader("Live Market Overview")
    cols = st.columns(4)
    for i, (coin, data) in enumerate(list(st.session_state.data.items())[:4]):
        if data:
            latest = list(data)[-1]
            with cols[i]:
                change = latest['change']
                if change > 5:
                    sentiment = "VERY BULLISH"
                elif change > 0:
                    sentiment = "BULLISH"
                elif change > -5:
                    sentiment = "BEARISH"
                else:
                    sentiment = "VERY BEARISH"
                
                st.metric(coin, f"${latest['price']:,.2f}", f"{latest['change']:+.2f}%")
                st.caption(sentiment)
    
    st.subheader("Price Trends")
    cols2 = st.columns(2)
    for i, (coin, data) in enumerate(list(st.session_state.data.items())[:2]):
        if data and len(data) > 1:
            with cols2[i]:
                df = pd.DataFrame(list(data))
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=df['time'], 
                    y=df['price'],
                    mode='lines+markers',
                    name='Price',
                    line=dict(color='#1f77b4', width=2)
                ))
                fig.update_layout(
                    title=f"{coin} Price Movement",
                    height=300,
                    template="plotly_white"
                )
                st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Latest Market Data")
    table_data = []
    for coin, data in st.session_state.data.items():
        if data:
            latest = list(data)[-1]
            table_data.append({
                'Coin': coin,
                'Price': f"${latest['price']:,.2f}",
                '24h Change': f"{latest['change']:+.2f}%",
                'Volume': f"${latest['volume']:,.0f}",
                'Time': latest['time'].strftime('%H:%M:%S')
            })
    if table_data:
        st.dataframe(pd.DataFrame(table_data), use_container_width=True, hide_index=True)

time.sleep(2)
st.rerun()
