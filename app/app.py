import os

import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            connect_timeout=3,
        )
        with conn, conn.cursor() as cur:
            cur.execute("select now()")
            now = cur.fetchone()[0]
        conn.close()
        return jsonify(db="ok", now=str(now))
    except Exception as e:
        app.logger.error("Connexion a la base impossible: %s", e)
        return jsonify(db="unreachable"), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
