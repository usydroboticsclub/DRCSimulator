
import http.server
import multiprocessing

def run(server_class=http.server.HTTPServer, handler_class=http.server.SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except Exception:
        print("hi")

# now the websocket
import websockets
import asyncio
import cv2
import numpy as np

async def hello(websocket, path):
    while (1):
        data = await websocket.recv()
        img=np.frombuffer(data,dtype=np.uint8)
        array=np.reshape(img,(480,640,4))[:,:,0:3]
        (b,g,r)=cv2.split(array)
        array=cv2.merge([r,g,b])
        array=np.flip(array,0)
        print(array.shape)
        print (np.sum(array))
        cv2.imshow("isee",array)
        cv2.waitKey(1)
        await websocket.send('{"speed":100,"steer":0.5}')
        print("sent!")


def runWS():
    start_server = websockets.serve(hello, "localhost", 8081, max_size=2**30)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__=="__main__":
    thread=multiprocessing.Process(target=run)
    thread.start()

    wsthread=multiprocessing.Process(target=runWS)
    wsthread.start()
    try:
        while 1:
            pass
    except KeyboardInterrupt:
        exit()
# # the webserver
# from flask import Flask
# app = Flask(__name__,
#             static_url_path='', 
#             static_folder='static')

# @app.route('/')
# def entry_point():
#     return app.send_static_file('index.html')

# # now mess with websockets

# import asyncio
# import threading
# 

# 