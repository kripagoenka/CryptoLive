

# 🚀 CryptoLive – Real-Time Cryptocurrency Streaming & Sentiment Analytics Dashboard

A real-time cryptocurrency analytics platform built using **Apache Kafka**, **Python**, and **Streamlit**. The application streams live cryptocurrency prices from the CoinGecko API, processes data through an event-driven Kafka pipeline, performs sentiment analysis based on market movements, and visualizes the results on an interactive dashboard.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Apache Kafka](https://img.shields.io/badge/Apache-Kafka-black.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

# 📖 Table of Contents

- Overview
- Architecture
- Features
- Tech Stack
- Project Structure
- Installation
- Running the Project
- Dashboard
- Sentiment Analysis
- Future Improvements
- License

---

# 📌 Overview

CryptoLive is an end-to-end real-time data streaming application designed to demonstrate modern event-driven architecture using Apache Kafka.

The system continuously fetches live cryptocurrency market data from the CoinGecko API, publishes the data to a Kafka topic, consumes and processes incoming events to generate market sentiment, and displays everything on a live Streamlit dashboard.

The project demonstrates concepts commonly used in production data engineering systems, including:

- Real-time data ingestion
- Event streaming
- Producer–Consumer architecture
- Stream processing
- Live dashboards
- JSON data persistence

---

# 🏗️ System Architecture

```
                 CoinGecko API
                       │
                       ▼
             Producer (Python)
                       │
         Publish messages every 5 sec
                       │
                       ▼
               Apache Kafka Topic
             (crypto-prices topic)
                       │
         ┌─────────────┴─────────────┐
         │                           │
         ▼                           ▼
 Consumer.py                  crypto_stream.json
 (Sentiment Engine)                  │
         │                           │
         └─────────────┬─────────────┘
                       ▼
             Streamlit Dashboard
             Real-Time Visualization
```

---

# ✨ Features

## 📈 Live Cryptocurrency Streaming

- Streams live prices for:
  - Bitcoin (BTC)
  - Ethereum (ETH)
  - Solana (SOL)
  - Cardano (ADA)

- Fetches new market data every **5 seconds**.

---

## ⚡ Apache Kafka Integration

- Producer publishes market updates.
- Consumer subscribes to Kafka topic.
- Decoupled architecture for scalability.
- Event-driven communication.

---

## 📊 Sentiment Analytics

Automatically classifies market movement into:

| Market Change | Sentiment |
|---------------|-----------|
| > +5% | 🚀 Very Bullish |
| 0% to +5% | 📈 Bullish |
| -5% to 0% | 📉 Bearish |
| < -5% | 💥 Very Bearish |

---

## 📉 Interactive Dashboard

Built using Streamlit and Plotly.

Dashboard includes:

- Live crypto prices
- Market sentiment
- Interactive line charts
- 24-hour change
- Trading volume
- Market snapshot
- Auto-refresh every 2 seconds

---

## 💾 JSON Snapshot

Every Kafka update is also written to:

```
crypto_stream.json
```

This allows:

- Fast dashboard loading
- Easy debugging
- Historical logging (can be extended)

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Streaming Platform | Apache Kafka |
| API | CoinGecko API |
| Dashboard | Streamlit |
| Visualization | Plotly |
| Data Processing | Pandas, NumPy |
| Messaging | kafka-python |
| Sentiment Analysis | VADER Sentiment |
| Storage | JSON |

---

# 📂 Project Structure

```
CryptoLive/
│
├── producer_simple.py
│      Fetches live prices
│      Publishes to Kafka
│      Saves JSON snapshot
│
├── consumer.py
│      Consumes Kafka messages
│      Performs sentiment analysis
│
├── dashboard.py
│      Streamlit dashboard
│      Live visualizations
│
├── crypto_stream.json
│      Latest streamed data
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/CryptoLive.git

cd CryptoLive
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Apache Kafka

### Start ZooKeeper

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### Start Kafka Broker

```bash
bin/kafka-server-start.sh config/server.properties
```

### Create Topic

```bash
bin/kafka-topics.sh \
--create \
--topic crypto-prices \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1
```

---

# ▶️ Running the Application

## Step 1

Start the Producer

```bash
python producer_simple.py
```

Producer responsibilities:

- Fetch live prices
- Publish Kafka messages
- Update JSON snapshot

---

## Step 2

Run Consumer

```bash
python consumer.py
```

Consumer responsibilities:

- Receive Kafka events
- Analyze market sentiment
- Display processed results

---

## Step 3

Launch Dashboard

```bash
streamlit run dashboard.py
```

Open:

```
http://localhost:8501
```

---

# 📊 Dashboard

The dashboard displays:

### 📌 Market Overview

- Live price cards
- Percentage change
- Sentiment labels

---

### 📈 Price Trends

Interactive Plotly charts for every cryptocurrency.

---

### 📋 Latest Market Data

Displays:

- Coin name
- Current price
- 24h change
- Trading volume
- Timestamp
- Sentiment

---

### 📊 Sidebar Metrics

- Active cryptocurrencies
- Total updates received
- Auto refresh status

---

# 🧠 Sentiment Analysis Logic

The application classifies each cryptocurrency using percentage price change.

```
Change > +5%
        ↓
Very Bullish 🚀

0% to +5%
        ↓
Bullish 📈

-5% to 0%
        ↓
Bearish 📉

Below -5%
        ↓
Very Bearish 💥
```

This lightweight rule-based approach provides an instant view of current market momentum.

---

# 🚀 Future Improvements

Potential enhancements include:

- Historical database storage (MongoDB/PostgreSQL)
- Kafka Streams for real-time aggregation
- WebSocket-based live streaming
- Price prediction using LSTM models
- Docker and Docker Compose deployment
- Kubernetes deployment
- Multi-topic Kafka architecture
- Email and Telegram price alerts
- Real-time portfolio tracking

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Event-driven architecture
- Apache Kafka fundamentals
- Producer–Consumer messaging
- REST API integration
- Stream processing
- Real-time dashboards
- Data visualization
- Python backend development
- JSON-based data persistence
- Sentiment analytics

---

# 🙏 Acknowledgements

- CoinGecko API for free cryptocurrency market data
- Apache Kafka for distributed event streaming
- Streamlit for rapid dashboard development
- Plotly for interactive visualizations
- VADER Sentiment for rule-based sentiment analysis

---

# 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ on GitHub** to support the project and help others discover it.
