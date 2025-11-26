import http
import socketserver
handler=http.server.SimpleHTTPRequestHandler
PORT=9000
with socketserver.TCPServer(("",PORT),handler) as HTTP:
    print("Server started on port:",PORT)
    http.serve_forever()