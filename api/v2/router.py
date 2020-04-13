# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify

# 创建蓝图实例
v2 = Blueprint("v2", __name__)


@v2.route("/index", endpoint="v2_index")
def v2_index():
    return jsonify({"msg": "v2_index"})
