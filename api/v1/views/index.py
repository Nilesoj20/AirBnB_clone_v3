#!/usr/bin/python3
""" index method for API development """
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=['GET'], strict_slaches=False)
def status():
    """ method to check the API status  """
    return jsonify({"status": "OK"})

