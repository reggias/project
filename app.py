from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://reggias:dlehdgud1!@cluster0.9mqf4xv.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/chan", methods=["POST"])
def chan_post():
    name_receive = request.form['name_give']
    job_receive = request.form['job_give']
    comment_receive = request.form['comment_give']

    chan_list = list(db.chan.find({}, {'_id': False}))
    count = len(chan_list) + 1

    doc = {
        'num':count,
        'name':name_receive,
        'job':job_receive,
        'comment':comment_receive,
        'done':0
    }

    db.chan.insert_one(doc)
    return jsonify({'msg': '가입 신청 완료!'})


@app.route("/chan/done", methods=["POST"])
def chan_done():
    num_receive = request.form['num_give']
    db.chan.delete_one({'num': int(num_receive)}, {'done': 0})
    return jsonify({'msg': '삭제 완료!'})


@app.route("/chan", methods=["GET"])
def chan_get():
    return jsonify({'msg': 'GET 연결 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)