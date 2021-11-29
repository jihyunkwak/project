from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/create', methods=['POST'])
def write_class():
    title_receive = request.form['title_give']
    name_receive = request.form['name_give']
    phone_receive = request.form['phone_give']
    email_receive = request.form['email_receive']
    place_receive = request.form['place_give']
    date_receive = request.form['date_give']
    fee_receive = request.form['fee_give']
    target_receive = request.form['target_give']
    detail_receive = request.form['detail_give']
    ref_receive = request.form['ref_give']

    doc = {
        'title': title_receive,
        'name': name_receive,
        'phone': phone_receive,
        'email': email_receive,
        'place': place_receive,
        'date': date_receive,
        'fee': fee_receive,
        'target': target_receive,
        'detail': detail_receive,
        'ref': ref_receive

    }

    db.classes.insert_one(doc)



    return jsonify({'msg': '저장 완료'})


@app.route('/create', methods=['GET'])
def read_class():
    classes = list(db.classes.find({}, {'_id': False}))
    return jsonify({'all_class': classes})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)