import algotik_tse as att
import time
from datetime import datetime

SYMBOLS = ['شستا', 'شپنا', 'فملی', 'خودرو', 'اهرم', 'فزر']

def get_stock_price(symbol):
    try:
        df = att.get_live_market(symbol)
        if df is not None and not df.empty:
            price = df.iloc[-1]['Last']
            print(f"{symbol} - Price: {price:,}")
            return price
    except Exception as e:
        print(f"Error {symbol}: {e}")
    return None

def get_option_chain(symbol):
    try:
        chain = att.get_options_chain(underlying=symbol, fetch_oi=True)
        if chain and 'calls' in chain and not chain['calls'].empty:
            calls = chain['calls']
            print(f"{symbol} - {len(calls)} calls")
            cols = ['Strike', 'Last', 'IV', 'Delta', 'Gamma', 'Vega', 'Theta']
            available = [c for c in cols if c in calls.columns]
            if available:
                print(calls[available].head(5))
            return chain
    except Exception as e:
        print(f"Option error {symbol}: {e}")
    return None

def main():
    print(f"Start: {datetime.now()}")
    print("=" * 60)
    for sym in SYMBOLS:
        print(f"\n{sym}...")
        get_stock_price(sym)
        get_option_chain(sym)
        time.sleep(1)
    print("\nDone")

if __name__ == "__main__":
    main()
