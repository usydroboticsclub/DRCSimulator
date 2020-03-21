
import http.server
import multiprocessing

server_class=http.server.HTTPServer
handler_class=http.server.SimpleHTTPRequestHandler
server_address = ('', 8000)
httpd = server_class(server_address, handler_class)
try:
    httpd.serve_forever()
except Exception:
    print("hi")
