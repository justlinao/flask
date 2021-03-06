
"""
第一个简单的接口  登录接口
"""
from flask import Flask, jsonify
from flask import request
app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])  # 路由默认是本地路径，在后面添加login代表下级目录。methods 标识请求方式
def login():
    request_method = request.method
    if request_method == 'GET':
        user = request.args.get('user')  # get获取地址栏参数
        password = request.args.get('password')
        if user and password:  # 对接收参数进行校验
            data = jsonify({'user': user, 'password': password,
                            'code': 200, 'message': '登录成功'})
        else:
            data = jsonify({'message': '请传入参数'})
        return data  # 返回内容
    elif request_method == 'POST':
        user = request.form.get('user')  # 表单格式
        password = request.form.get('password')
        if user and password:
            if user == 'test' and password == '123456':  # 校验接收的参数
                re_data = jsonify({'code': 200, 'message': '登录成功'})  # 返回内容
            else:
                re_data = jsonify({'code': 200, 'message': '账密不正确'})
        else:
            re_data = jsonify({'code': 200, 'message': '请输入正确的参数'})
        return re_data


if __name__ == '__main__':
    app.run()





