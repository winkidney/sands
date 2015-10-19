import os
from flask import render_template
from flask import redirect

from sands.app import app


@app.route("/", methods=["GET"])
def home():
    return redirect("/sketch")


@app.route("/sketch", methods=["GET"])
def sketch():
    return render_template("from_sketch/index.html")