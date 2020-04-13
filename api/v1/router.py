# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify

# 创建蓝图实例
v1 = Blueprint("v1", __name__, )


@v1.route("/index", endpoint="v1_index")
def v1_index():
    return jsonify({"msg": "v1_index"})
