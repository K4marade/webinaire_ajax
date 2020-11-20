from flask import render_template, jsonify, request

from . import app
from .utils import transform_to_upper


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["userText"]
    response = transform_to_upper(user_text)
    return jsonify(response)
