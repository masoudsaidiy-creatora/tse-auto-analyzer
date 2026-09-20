import time
from datetime import datetime

SYMBOLS = ['شستا', 'شپنا', 'فملی', 'خودرو', 'اهرم', 'فزر']

def main():
    print(f"Start: {datetime.now()}")
    print("=" * 60)
    for sym in SYMBOLS:
        print(f"Processing {sym}...")
        time.sleep(1)
    print("=" * 60)
    print("Done — Workflow works!")

if __name__ == "__main__":
    main()
