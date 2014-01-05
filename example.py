# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_webglearth import WebGlEarth, WebGl, map_types

app = Flask(__name__, template_folder=".")
WebGl(app)

@app.route("/")
@app.route("/index")
def index():
    webgl_earth = WebGlEarth(zoom=5, map_type=map_types[0],
                             center=[46.3, 30.4], atmosphere=True)
    return render_template('example_template.html', webgl_map=webgl_earth)


if __name__ == "__main__":
    app.run(debug=True)