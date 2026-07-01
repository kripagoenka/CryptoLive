import json
import time
import requests
from datetime import datetime

print("="*70)
print("CRYPTO DATA STREAMING - Real-time Producer")
print("="*70)

while True:
    try:
        response = requests.get(
            'https://api.coingecko.com/api/v3/simple/price',
            params={
                'ids': 'bitcoin,ethereum,cardano,solana',
                'vs_currencies': 'usd',
                'include_24hr_vol': 'true',
                'include_24hr_change': 'true',
                'include_market_cap': 'true'
            }
        )
        
        if response.status_code == 200:
            data = response.json()
            
            with open('crypto_stream.json', 'w') as f:
                records = []
                for coin, details in data.items():
                    record = {
                        'coin': coin.upper(),
                        'price_usd': details.get('usd', 0),
                        'volume_24h': details.get('usd_24h_vol', 0),
                        'price_change_24h': details.get('usd_24h_change', 0),
                        'market_cap': details.get('usd_market_cap', 0),
                        'timestamp': datetime.now().isoformat()
                    }
                    records.append(record)
                    # Fixed print - no special characters
                    print(f"OK {record['coin']}: ${record['price_usd']:.2f} ({record['price_change_24h']:+.2f}%)")
                
                json.dump(records, f)
            
            print(f"\nBatch updated at {datetime.now().strftime('%H:%M:%S')}")
            print("-" * 70)
        
        time.sleep(5)
        
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
