# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template

bp = Blueprint('home', __name__)


@bp.route('/')
def home():
    # return redirect(url_for("items.list_focused"))
    return render_template('accounts/login.html')
