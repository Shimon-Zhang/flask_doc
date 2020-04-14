from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import Flask, jsonify, request
from api.v1.router import v1
from api.v2.router import v2

# 创建app实例
app = Flask(__name__)
# 初始化token对象
serializer = Serializer(secret_key='token—key', expires_in=3600)
# 注册蓝图实例
app.register_blueprint(v1, url_prefix="/v1")
app.register_blueprint(v2, url_prefix="/v2")


def login_auth(func):
    def b(*args, **kwargs):
        token = request.args.get("token")
        if token:
            try:
                serializer.loads(token)
            except Exception as e:
                return jsonify({"msg": f"token验证失败：{e}", "data": None})
            else:
                ret = func(*args, **kwargs)
                return ret
        else:
            return jsonify({"msg": "token参数缺失", "data": None})

    return b


# 生死检测
@app.route("/ping", endpoint="ping")
@login_auth
def ping():
    print(app.url_map)
    return jsonify({"msg": "pong", "data": None})


@app.route("/login", methods=["POST"])
def get_token():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "xmzhang" and password == "123":
        token = serializer.dumps({"username": username, "password": password}).decode()
        return jsonify({"msg": "登录成功", "data": token})
    return jsonify({"msg": "登录失败,请重新登录", "data": None})


if __name__ == '__main__':
    app.run()
