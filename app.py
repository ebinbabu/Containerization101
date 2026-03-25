import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(os.environ["DATABASE_URL"])

@app.route("/")
def hello():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f"<h1>Hi!</h1><p>Connected to: {db_version}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
