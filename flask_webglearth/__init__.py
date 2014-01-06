# -*- coding: utf-8 -*-

from flask import render_template, Blueprint, Markup


map_types = ['WebGLEarth.Maps.OSM', 'WebGLEarth.Maps.MAPQUEST']


class WebGlEarth(object):
    def __init__(self, zoom=5, center=None, map_type=map_types[0],
                 atmosphere=False, markers=None):
        self.zoom = zoom
        self.center = center or []
        self.map_type = map_type
        self.atmosphere = str(atmosphere).lower()
        self.markers = markers

    def add_marker(self, marker):
        self.markers.append(marker)

    def render(self, *args, **kwargs):
        return render_template(*args, **kwargs)

    @property
    def js(self):
        return Markup(self.render('webgljs.html', webgl=self))


def webgl_map_obj(*args, **kwargs):
    webgl_map = WebGlEarth(*args, **kwargs)
    return webgl_map


def webgl_map_js(*args, **kwargs):
    return webgl_map_obj(*args, **kwargs).js


class WebGl(object):
    def __init__(self, app=None):
        if app:
            app.add_template_filter(webgl_map_js)
            self.register_blueprint(app)

    def register_blueprint(self, app):
        module = Blueprint("weglearth", __name__,
                           template_folder="templates")
        app.register_blueprint(module)
        return module


class Marker(object):
    def __init__(self, lat, lng, info_window=""):
        self.lat = lat
        self.lng = lng
        self.info_window = info_window