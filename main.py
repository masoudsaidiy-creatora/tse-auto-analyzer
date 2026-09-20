import requests
import time
from datetime import datetime

def main():
    print(f"Start: {datetime.now()}")
    print("=" * 60)
    
    url = "https://cdn.tsetmc.com/api/ClosingPrice/GetMarketWatch?market=0&paperTypes[0]=1&withBestLimits=false&hEven=0&RefID=0"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36',
        'Accept': 'application/json',
    }
    
    try:
        r = requests.get(url, headers=headers, timeout=30)
        print(f"Status: {r.status_code}")
        if r.status_code == 200:
            data = r.json()
            watch = data.get('marketwatch', [])
            print(f"تعداد نمادها: {len(watch)}")
            
            # نمادهای مورد نظر (insCode)
            targets = {
                '46348559193224090': 'شستا',
                '7745894403636165': 'شپنا',
                '35425587644337450': 'فملی',
                '65883838195688438': 'خودرو',
                '62304835470351609': 'اهرم',
                '35366681030756042': 'فزر',
            }
            
            print("\n" + "=" * 60)
            for item in watch:
                insCode = str(item.get('insCode', ''))
                if insCode in targets:
                    sym = targets[insCode]
                    pl = item.get('pl')        # آخرین قیمت
                    pc = item.get('pc')        # قیمت پایانی
                    pd = item.get('pDrCotVal') # قیمت آخرین معامله
                    py = item.get('py')        # قیمت دیروز
                    print(f"\n📊 {sym} ({insCode})")
                    print(f"   pl (آخرین): {pl}")
                    print(f"   pc (پایانی): {pc}")
                    print(f"   pDrCotVal: {pd}")
                    print(f"   py (دیروز): {py}")
                    if pl:
                        print(f"   💰 {int(pl):,} ریال = {int(pl)//10:,} تومان")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 60)
    print("✅ Done")

if __name__ == "__main__":
    main()
