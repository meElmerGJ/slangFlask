from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo_url = "mongodb://localhost:27017/slang"
app.config["MONGO_URI"] = mongo_url
mongo = PyMongo(app)


slang = mongo.db.slangs


@app.route('/new_word', methods=['POST', 'GET'])
def insert_slang():
    if request.method == 'POST':
        word = request.form.get('word')
        meaning = request.form.get('meaning')
        slang.insert_one({'word': word, 'meaning': meaning})
        return redirect(url_for('index'))
    return render_template('new_word.html')


@app.route('/edit_word', methods=['POST', 'GET'])
def edit_slang():
    if request.method == 'POST':
        word = request.form.get('word')
        meaning = request.form.get('meaning')
        slang.update_one({'word': word}, {'$set': {'word': word, 'meaning': meaning}})
        return redirect(url_for('index'))
    documents = slang.find()
    return render_template('edit_word.html', documents=documents)


@app.route('/search_word', methods=['POST', 'GET'])
def search_slang():
    if request.method == 'POST':
        word = request.form.get('word')
        documents = slang.find({"word": word})
        return render_template('search_word.html', documents=documents)
    return render_template('search_word.html')


@app.route('/del_word', methods=['POST', 'GET'])
def del_slang():
    if request.method == 'POST':
        word = request.form.get('word')
        slang.delete_one({'word': word})
    documents = slang.find()
    return render_template('del_word.html', documents=documents)


@app.route('/', methods=['POST', 'GET'])
def index():  # put application's code here
    documents = slang.find()
    return render_template('index.html', documents=documents)


if __name__ == '__main__':
    app.run(debug=True)


