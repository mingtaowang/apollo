# -*- coding: utf-8 -*-

from flask import jsonify


def jsonify_with_data(http_status, **kwargs):
    kwargs.setdefault('msg', '')
    kwargs.setdefault('code', 0)
    return jsonify(**kwargs), http_status
