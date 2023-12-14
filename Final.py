from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('form.html')

@app.route('/search', methods=["POST"])
def search():
    name = request.form['name']
    api_key = 'k399tIUrjskAe-CDcVs3zja1YHOpypjbz70-fenL72U'  
    url = f'https://api.unsplash.com/search/photos?query={name}&client_id={api_key}'
    r = requests.get(url)
    pics = [pic['urls']['small'] for pic in r.json().get('results', [])] 
    return render_template('display.html', name=name, pics=pics)

if __name__ == '__main__':
    app.run(debug=True)
