"""HTTP-обёртка над калькулятором, v2: конфигурация через переменные окружения.

GET /calc?op=add&a=2&b=3  -> {"result": 5}
GET /config               -> текущая конфигурация (для лабораторной)
GET /health               -> {"status": "ok"}
"""
import os

from flask import Flask, jsonify, request

import calculator

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "calc-app")
CALC_PRECISION = int(os.getenv("CALC_PRECISION", "2"))

OPS = {
    "add": calculator.add,
    "sub": calculator.sub,
    "mul": calculator.mul,
    "div": calculator.div,
}


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/config")
def config():
    """Показывает текущую конфигурацию — чтобы было видно ConfigMap/Secret."""
    return jsonify(
        app_name=APP_NAME,
        calc_precision=CALC_PRECISION,
        db_user=os.getenv("DB_USER", "<не задан>"),
        db_password=os.getenv("DB_PASSWORD", "<не задан>"),
    )


@app.route("/calc")
def calc():
    op = request.args.get("op", "add")
    if op not in OPS:
        return jsonify(error=f"unknown op: {op}"), 400
    try:
        a = float(request.args["a"])
        b = float(request.args["b"])
        return jsonify(app=APP_NAME, result=round(OPS[op](a, b), CALC_PRECISION))
    except (KeyError, ValueError) as e:
        return jsonify(error=str(e)), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
