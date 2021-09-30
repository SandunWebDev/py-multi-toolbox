#!/usr/bin/env python3

# flake8: noqa

import webbrowser
import http.server
import socketserver
import functools

PORT = 8000
PATH = "./build/coverage/html_report"

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=PATH)

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Serving Cover Report @ Port", PORT)
        webbrowser.open("http://localhost:8000/")
        httpd.serve_forever()
except OSError:
    print(f"\nERROR : Port {PORT} already exist. Clear the port and try again.")
except KeyboardInterrupt:
    print('Exiting...')
    # TODO : Find a way to free the opened port.
