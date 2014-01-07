# coding: utf8
from flask import Flask, render_template
from flask_webglearth import WebGlEarth, WebGl, MAP_TYPES, Marker, Polygon

app = Flask(__name__, template_folder=".")
WebGl(app)


@app.route("/")
@app.route("/index")
def index():
    webgl_earth = WebGlEarth(zoom=1, map_type=MAP_TYPES.get('osm'),
                             center=[46.3, 30.4], atmosphere=True,
                             markers=[Marker(49.3, 30.4, "Hello world!")],
                             polygons=[Polygon(([45.1, 30.3],
                                                [46.1, 40.56], [50.3, 20.8]))])
    return render_template('example_template.html', webgl_map=webgl_earth)


if __name__ == "__main__":
    app.run(debug=True)