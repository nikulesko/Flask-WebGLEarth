# -*- coding: utf-8 -*-

from flask import render_template, Blueprint, Markup


class WebGlEarth(object):
    def __init__(self):
        pass

    def render(self, *args, **kwargs):
        return render_template(*args, **kwargs)

    @property
    def js(self):
        return Markup(self.render('webgljs.html', webgl=self))


def googlemap_js(*args, **kwargs):
    return googlemap_obj(*args, **kwargs).js


class WebGl(object):
    def __init__(self, app=None):
        if app:
            app.add_template_filter(googlemap_js)
            self.register_blueprint(app)

    def register_blueprint(self, app):
        module = Blueprint("weglearth", __name__,
                           template_folder="templates")
        app.register_blueprint(module)
        return module