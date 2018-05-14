from sense_hat import SenseHat
import SimpleHTTPServer
import SocketServer

sense = SenseHat()

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        temp = sense.get_temperature()
        self._set_headers()
        self.wfile.write("<html><body><h1>Teplota: %s C</h1></body></html>" % temp)


PORT = 8000

Handler = MyHandler #SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

#print("Temperature: %s C" % temp)
print ("serving at port", PORT)
httpd.serve_forever()