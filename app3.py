from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://reggias:dlehdgud1!@cluster0.9mqf4xv.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index3.html')


@app.route("/chan3", methods=["POST"])
def chan3_post():
    return jsonify({'msg': 'POST 연결 완료!'})


@app.route("/chan3", methods=["GET"])
def chan3_get():
    return jsonify({'msg': 'GET 연결 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5002, debug=True)
