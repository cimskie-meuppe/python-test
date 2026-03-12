# Last updated: 2026-03-12 12:58:28

import datetimedef get_current_time():    now = datetime.datetime.now()    print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")    return nowif __name__ == "__main__":    get_current_time()
