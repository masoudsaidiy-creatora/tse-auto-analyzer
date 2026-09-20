
import requests
import re
from datetime import datetime
import time

SYMBOLS = [
    {'sym': 'شستا', 'insCode': '46348559193224090'},
    {'sym': 'شپنا', 'insCode': '7745894403636165'},
    {'sym': 'فملی', 'insCode': '35425587644337450'},
    {'sym': 'خودرو', 'insCode': '65883838195688438'},
    {'sym': 'اهرم', 'insCode': '62304835470351609'},
    {'sym': 'فزر', 'insCode': '35366681030756042'},
]

def get_price_jina(insCode):
    """استفاده از r.jina.ai به عنوان پروکسی (رایگان)"""
    target = f"https://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceInfo/{insCode}"
    url = f"https://r.jina.ai/{target}"
    try:
        r = requests.get(url, timeout=20)
        if r.status_code == 200:
            text = r.text
            m = re.search(r'"pDrCotVal":(\d+)', text)
            if m:
                return int(m.group(1)) // 10
            m = re.search(r'"pClosing":(\d+)', text)
            if m:
                return int(m.group(1)) // 10
    except Exception as e:
        print(f"  Jina error: {e}")
    return None

def get_price_direct(insCode):
    """اتصال مستقیم (ممکنه کار نکنه)"""
    url = f"https://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceInfo/{insCode}"
    try:
        r = requests.get(url, timeout=8)
        if r.status_code == 200:
            data = r.json()
            info = data.get('closingPriceInfo', {})
            price = info.get('pDrCotVal') or info.get('pClosing') or info.get('py')
            if price:
                return int(price) // 10
    except:
        pass
    return None

def main():
    print(f"Start: {datetime.now()}")
    print("=" * 60)
    for s in SYMBOLS:
        print(f"\n📊 {s['sym']} ({s['insCode']})")
        
        # اول مستقیم امتحان کن
        price = get_price_direct(s['insCode'])
        if price:
            print(f"  ✅ Direct: {price:,} تومان")
            continue
        
        # اگه مستقیم نشد، با Jina امتحان کن
        print(f"  ⏳ Direct failed, trying Jina...")
        price = get_price_jina(s['insCode'])
        if price:
            print(f"  ✅ Jina: {price:,} تومان")
        else:
            print(f"  ❌ هر دو روش رد شدند")
        
        time.sleep(1)
    
    print("\n" + "=" * 60)
    print("✅ Done")

if __name__ == "__main__":
    main()
