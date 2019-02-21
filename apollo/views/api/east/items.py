# -*- coding: utf-8 -*-

import json
import requests

from flask import Blueprint, render_template

bp = Blueprint('items', __name__, url_prefix='/items')


@bp.route('/focus')
def list_focused():
    funds = {
        '100032': {'expect': 0.98, 'tactics': u'长期'},
        '160106': {'expect': 0.86, 'tactics': u'长期'},
        '257070': {'expect': 1.15, 'tactics': u'长期'},
        '000942': {'expect': 0.75, 'tactics': u'长期'},
        '000059': {'expect': 0.75, 'tactics': u'长期'},
        '003318': {'expect': 0.78, 'tactics': u'长期'},
        '000478': {'expect': 1.7, 'tactics': u'长期'},
        '164906': {'expect': 0.98, 'tactics': u'长期'},
        '161725': {'expect': 0.9, 'tactics': u'长期'},
        '161720': {'expect': 0.75, 'tactics': u'长期'},
        '001551': {'expect': 0.6, 'tactics': u'长期'},
        '004070': {'expect': 0.72, 'tactics': u'长期'},
        '001553': {'expect': 0.67, 'tactics': u'长期'},
        '000248': {'expect': 1.25, 'tactics': u'长期'},
        '000311': {'expect': 1.7, 'tactics': u'长期'},
        '001632': {'expect': 1.2, 'tactics': u'长期'},
        '002979': {'expect': 0.87, 'tactics': u'长期'},
        '161022': {'expect': 0.78, 'tactics': u'长期'},
        '310398': {'expect': 1.2, 'tactics': u'长期'}
    }
    base_url = 'http://fundgz.1234567.com.cn/js/%s.js'
    data = []
    for code, extra in funds.iteritems():
        r = requests.get(base_url % str(code))
        detail = json.loads(r.content[8:-2])
        predict = float(detail.get('gsz'))
        expect = float(extra.get('expect'))
        percent = round((predict - expect) % predict, 5) * 100
        data.append({'code': detail.get('fundcode'),
                     'name': detail.get('name'),
                     'predict': predict,
                     'yesterday': detail.get('dwjz'),
                     'threshold': expect,
                     'diff': predict - expect,
                     'percent': percent,
                     'tactics': extra.get('tactics')})
    return render_template('east/focus.html', data=data)
