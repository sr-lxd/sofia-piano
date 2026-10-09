"""本机运行 Sofia 钢琴 Flask 应用。"""
import os

from flask import Flask
from __init__ import piano_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(piano_bp)
    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PIANO_PORT", "5051"))
    app.run(host="127.0.0.1", port=port, debug=False)
