# -*- coding: utf-8 -*-

import datetime

import json
import requests

from flask import Blueprint, render_template

from apollo.libs.db.store import db_mongo as db

bp = Blueprint('items', __name__, url_prefix='/items')


@bp.route('/focus')
def list_focused():
    codes = ['100032', '160106', '257070', '000942', '000059', '003318', '000478', '164906', '161725', '161720',
             '001551', '004070', '001553', '000248', '000311', '001632', '002979', '161022', '310398']
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
    for code in codes:
        extra = funds.get(code)
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


@bp.route('/east')
def get_useful_items():
    day = str(datetime.date.today())
    base_url = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=%s&' \
               'ed=%s&qdii=&tabSubtype=,,,,,&pi=1&pn=10000&dx=1&v=0.5322768018683062'
    r = requests.get(base_url % (day, day))
    content = r.content
    content = content[content.index('['): content.index(']') + 1]
    content = json.loads(content)
    data = []
    db.snowball.easts.remove({})
    for item in content:
        temp = item.split(',')
        data.append({
            'code': temp[0],  # 代码
            'name': temp[1],  # name
            'day': temp[3],  # day
            'per_value': round(float(temp[4]), 3) if temp[4] else None,  # 单位净值
            'one_day': round(float(temp[6]), 3) if temp[6] else None,  # 日增长率
            'week': round(float(temp[7]), 3) if temp[7] else None,  # 近一周
            'month': round(float(temp[8]), 3) if temp[8] else None,  # 近一月
            'three_month': round(float(temp[9]), 3) if temp[9] else None,  # 近三月
            'six_month': round(float(temp[10]), 3) if temp[10] else None,  # 近六月
            'year': round(float(temp[11]), 3) if temp[11] else None,  # 近一年
            'two_year': round(float(temp[12]), 3) if temp[12] else None,  # 近两年
            'three_year': round(float(temp[13]), 3) if temp[13] else None,  # 近三年
            'total': round(float(temp[14]), 3) if temp[14] else None  # 成立以来
        })
    db.snowball.easts.insert(data)
    return render_template('east/quality.html')


@bp.route('/statistics')
def show_items():
    data = {}
    fields = ['one_day', 'week', 'month', 'three_month', 'six_month', 'year', 'two_year', 'three_year',
              'total']
    for field in fields:
        items = db.snowball.easts.find().limit(30).sort(field, -1)
        data = get_color(data, items, fields, sort=field)
    return_list = []
    for key, value in data.items():
        return_list.append(value)
    return_list.sort(key=lambda l: l["one_day"], reverse=True)
    return render_template('east/statistics.html', data=return_list)


def get_color(data, items, fields, sort='one_day'):
    for index, item in enumerate(items):
        colors = {field: 0 for field in fields}
        default_data = data.setdefault(item.get('code'), item)
        default_color = default_data.setdefault('color', colors)
        if index < 10:
            default_color[sort] = 1
        elif 10 <= index < 20:
            default_color[sort] = 2
        else:
            default_color[sort] = 3
    return data
