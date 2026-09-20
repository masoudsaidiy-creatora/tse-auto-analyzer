import requests
from datetime import datetime

def main():
    print(f"Start: {datetime.now()}")
    print("=" * 60)
    
    url = "https://cdn.tsetmc.com/api/ClosingPrice/GetMarketWatch?market=0&paperTypes[0]=1&withBestLimits=false&hEven=0&RefID=0"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36',
    }
    
    try:
        r = requests.get(url, headers=headers, timeout=30)
        print(f"Status: {r.status_code}")
        if r.status_code == 200:
            data = r.json()
            watch = data.get('marketwatch', [])
            print(f"تعداد کل: {len(watch)}")
            print("=" * 60)
            
            targets = {
                '46348559193224090': 'شستا',
                '7745894403636165': 'شپنا',
                '35425587644337450': 'فملی',
                '65883838195688438': 'خودرو',
                '62304835470351609': 'اهرم',
                '35366681030756042': 'فزر',
            }
            
            for item in watch:
                insCode = str(item.get('insCode', ''))
                if insCode in targets:
                    sym = targets[insCode]
                    pl = item.get('pl')       # آخرین قیمت معامله
                    py = item.get('py')       # قیمت پایانی دیروز
                    pf = item.get('pf')       # قیمت پایانی
                    
                    # انتخاب بهترین قیمت در دسترس
                    price = pl or pf or py
                    
                    print(f"\n📊 {sym}")
                    print(f"   pl={pl}, pf={pf}, py={py}")
                    if price:
                        print(f"   💰 {price:,} ریال = {price//10:,} تومان")
                    else:
                        print(f"   ⚠️ داده‌ای برای قیمت موجود نیست")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 60)
    print("✅ Done")

if __name__ == "__main__":
    main()
