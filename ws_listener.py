import websocket
import sys
import asyncio

from websocket import create_connection

def on_error(ws, error):
    print(error)

def append(rr):
    f = open("result.txt", "a+")
    f.write("\n" + rr + "\n")
    f.close()

def on_message(ws, message):
    print(message)
    append(message)




if __name__ == '__main__':
    while 1:
        try:
            ws = websocket.WebSocketApp("ws://127.0.0.1:12001/subscribe_market_data?symbols=EURUSD&token=1@sa5",
                                        on_message=on_message,
                                        on_error=on_error)
            ws.run_forever()
        except:
            continue

