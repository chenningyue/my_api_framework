from flask import Flask, jsonify
from common.db import query

app = Flask(__name__)


@app.route("/students")
def students():
    # 这个接口背后就是查同一个库，把学生列表转成 JSON 返回
    return jsonify(query("SELECT id, name, class_name FROM students ORDER BY id"))