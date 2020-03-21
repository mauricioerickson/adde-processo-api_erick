import sqlite3
import subprocess
from pathlib import Path

import connexion
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from server.configuration import environment

db = SQLAlchemy()
ma = Marshmallow()


def init_api():
    verifica_banco_local()

    app = connexion.App(__name__, specification_dir="./swagger/")
    app.add_api("swagger.yaml", arguments={"host_with_port": f"{environment.HOST}:{environment.PORT}"})
    app.app.config["SQLALCHEMY_DATABASE_URI"] = environment.DB_CONNECTION
    app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app.app)
    CORS(app.app)
    ma.init_app(app.app)
    return app


def verifica_banco_local():
    conn = None
    try:
        conn = sqlite3.connect(environment.DB_PATH)
        aplicar_migrations()
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()


def aplicar_migrations():
    cwd = Path(environment.PROJECT_PATH)
    cmd_command = "alembic upgrade head"
    process = subprocess.Popen(cmd_command.split(), stdout=subprocess.PIPE, cwd=cwd)
    _, _ = process.communicate()
