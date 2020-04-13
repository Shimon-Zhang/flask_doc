from flask import Flask, session, jsonify
from api.v1.router import v1
from api.v2.router import v2

# 创建app实例
app = Flask(__name__)
# 注册蓝图实例
app.register_blueprint(v1, url_prefix="/v1")
app.register_blueprint(v2, url_prefix="/v2")


# 生死检测
@app.route("/", endpoint="ping")
def ping():
    print(app.url_map)
    return jsonify({"msg": "pong"})


if __name__ == '__main__':
    app.run()
