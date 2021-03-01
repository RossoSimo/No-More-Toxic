import asyncio
import multiprocessing
import time
import websocket2
import browser
import sys
from http_serv import http_server

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=websocket2.start)
    p2 = multiprocessing.Process(target=http_server.start)
    p2.start()
    p1.start()
    time.sleep(0.5)
    # http_server.start()
    asyncio.get_event_loop().run_until_complete(browser.main())
    p2.join()
    p1.join()

    print("Done")
