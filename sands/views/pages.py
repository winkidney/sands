from flask import render_template, request, jsonify
from flask import redirect

from sands.app import app
from sands.forms.sketch import SketchForm
from sands.models.sketch import Word


@app.route("/", methods=["GET"])
def home():
    return redirect("/sketch")


@app.route("/sketch", methods=["GET", "POST"])
def sketch():
    form = SketchForm()
    if request.method == "POST":
        if form.validate_on_submit():
            result = dict(
                (type_name, Word.random_by_type(type_name).name)
                for type_name in form.get_true_field()
            )
            return render_template(
                "from_sketch/search/result.html",
                **locals()
            )
        return jsonify(form.errors)
    else:
        return render_template("from_sketch/search/index.html", **locals())