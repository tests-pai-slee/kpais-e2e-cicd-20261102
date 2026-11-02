import json
import tomllib
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


def version():
    return tomllib.loads(Path(__file__).with_name("pyproject.toml").read_text())[
        "project"
    ]["version"]


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"service": "kpais-e2e", "version": version()}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
