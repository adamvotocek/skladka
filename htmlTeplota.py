from sense_hat import SenseHat
import SimpleHTTPServer
import SocketServer

sense = SenseHat()

temp = 0

def getHtml(temp):
    return (("""<html><head><script""" +
""" src="https://code.jquery.com/jquery-3.3.1.min.js"></script>""" +
"""</head><body><h1>Teplota: <span id="temp">%s</span>C</h1>""" + 
"""<script>""" +
"""$(document).ready(function(){""" +
"""   setInterval(function(){""" +
"""      $.get("get-temp", function (data){""" +
"""         $("#temp").html(data)""" +
"""      });""" +
"""   },2000);"""
"""});""" +
"""</script></body></html>""") % round(temp, 2))

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        temp = sense.get_temperature()
        self._set_headers()
        if self.path == "/get-temp":
            print("QWERTZ")
            self.wfile.write("%s" % round(temp, 2))
        else:
            self.wfile.write(getHtml(temp))
        print("00000" + self.path + "00000")

PORT = 8001

Handler = MyHandler #SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

#print("Temperature: %s C" % temp)
print ("serving at port", PORT)
httpd.serve_forever()