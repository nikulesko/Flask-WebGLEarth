# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_webglearth import WebGlEarth, WebGl

app = Flask(__name__, template_folder=".")
WebGl(app)

@app.route("/")
@app.route("/index")
def index():
    webgl_earth = WebGlEarth()
    return render_template('index_template.html', webgl_map=webgl_earth)


if __name__ == "__main__":
    app.run(debug=True)