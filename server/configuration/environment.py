import os
from pathlib import Path

PROJECT_PATH = Path(os.path.abspath(__file__)).parents[2]
HOST = "localhost"
PORT = "8080"
DB_PATH = f"{PROJECT_PATH}{os.path.sep}db_processo.db"
DB_CONNECTION = "sqlite:///" + DB_PATH
