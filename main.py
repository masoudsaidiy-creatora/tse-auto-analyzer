import requests
import time
from datetime import datetime

SYMBOLS = [
    {'sym': 'شستا', 'insCode': '46348559193224090'},
    {'sym': 'شپنا', 'insCode': '7745894403636165'},
    {'sym': 'فملی', 'insCode': '35425587644337450'},
    {'sym': 'خودرو', 'insCode': '65883838195688438'},
    {'sym': 'اهرم', 'insCode': '62304835470351609'},
    {'sym': 'فزر', 'insCode': '35366681030756042'},
]

def get_price(insCode):
    url = f"https://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceInfo/{insCode}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36',
        'Accept': 'application/json',
    }
    try:
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code == 200:
            data = r.json()
            info = data.get('closingPriceInfo', {})
            # چاپ همه‌ی فیلدهای قیمتی برای دیباگ
            print(f"   pDrCotVal: {info.get('pDrCotVal')}")
            print(f"   pClosing: {info.get('pClosing')}")
            print(f"   py (دیروز): {info.get('py')}")
            print(f"   last: {info.get('last')}")
            # برگرداندن pDrCotVal (آخرین قیمت معامله)
            price = info.get('pDrCotVal') or info.get('pClosing') or info.get('py')
            if price:
                return int(price)  # ریال
    except Exception as e:
        print(f"   Error: {e}")
    return None

def main():
    print(f"Start: {datetime.now()}")
    print("=" * 60)
    for s in SYMBOLS:
        print(f"\n📊 {s['sym']} ({s['insCode']})")
        price = get_price(s['insCode'])
        if price:
            print(f"   💰 قیمت: {price:,} ریال = {price//10:,} تومان")
        else:
            print(f"   ❌ دریافت نشد")
        time.sleep(2)
    print("\n" + "=" * 60)
    print("✅ Done")

if __name__ == "__main__":
    main()
