import http.server, os
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=int(os.environ.get("PORT", 8080)))