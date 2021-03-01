import functools
import http.server, ssl
import os
import socketserver
import socket



# Create an object of the above class
def start():
    path=os.getcwd()
    server_address = ('localhost', 4443)
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=path+"/http_serv/html/")
    httpd = socketserver.TCPServer(server_address, handler,False)
    httpd.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    httpd.server_bind()
    httpd.server_activate()
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   server_side=True,
                                   certfile=path+"/http_serv/"+'localhost.pem',
                                   ssl_version=ssl.PROTOCOL_TLS)
    print("inizializzato il server https")
    httpd.serve_forever()
