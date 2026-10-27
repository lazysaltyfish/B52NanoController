#!/usr/bin/env python3
"""B52Nano Controller 本地启动器

用法:
    python3 serve.py            # http://127.0.0.1:8765 并自动打开浏览器
    python3 serve.py 9000       # 自定义端口
    python3 serve.py --no-browser
"""
import http.server
import socketserver
import os
import sys
import webbrowser

PORT = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 8765
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Server(socketserver.TCPServer):
    allow_reuse_address = True  # 快速重启时避免 Address already in use


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


with Server(("127.0.0.1", PORT), Handler) as httpd:
    url = f"http://127.0.0.1:{PORT}"
    print(f"B52Nano 控制台已启动: {url}  (Ctrl+C 退出)")
    if "--no-browser" not in sys.argv:
        webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n已退出")
