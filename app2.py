from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://reggias:dlehdgud1!@cluster0.9mqf4xv.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index2.html')


@app.route("/chan2", methods=["POST"])
def chan2_post():
    CharacterID_receive = request.form['CharacterID_give']
    nick_give = request.form['nick_give']
    comment_give = request.form['comment_give']

    doc = {
        'CharacterID_give': CharacterID_receive,
        'nick_give': nick_give,
        'comment_give': comment_give
    }

    db.chan2.insert_one(doc)
    return jsonify({'msg': '방명록 완료!'})


@app.route("/chan2", methods=["GET"])
def chan2_get():
    return jsonify({'msg': 'GET 연결 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)