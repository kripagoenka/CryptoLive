from kafka import KafkaConsumer
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

consumer = KafkaConsumer(
    'crypto-prices',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='latest'
)

analyzer = SentimentIntensityAnalyzer()
count = 0

print("="*70)
print("Crypto Analytics Consumer - Waiting for messages...")
print("="*70)

for message in consumer:
    try:
        data = message.value
        count += 1
        
        # Sentiment
        if data['price_change_24h'] > 5:
            sentiment = "Very Bullish 🚀"
        elif data['price_change_24h'] > 0:
            sentiment = "Bullish 📈"
        elif data['price_change_24h'] > -5:
            sentiment = "Bearish 📉"
        else:
            sentiment = "Very Bearish 💥"
        
        print(f"\n{'='*70}")
        print(f"Message #{count} | Coin: {data['coin']}")
        print(f"{'='*70}")
        print(f"💰 Price: ${data['price_usd']:,.2f}")
        print(f"📊 24h Change: {data['price_change_24h']:+.2f}%")
        print(f"🎯 Sentiment: {sentiment}")
        print(f"💹 Volume: ${data['volume_24h']:,.0f}")
    except Exception as e:
        print(f"Error: {e}")
