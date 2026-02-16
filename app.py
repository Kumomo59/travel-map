from flask import Flask, render_template, jsonify
app = Flask(__name__)

shops = [
    {  "name": "相鉄ホテルズ　ザ　スプラジール　ソウル明洞","lat": 37.5620767,"lng":126.9789844,"memo":"ホテル"},
    {"name": "AAA", "lat": 35.681, "lng": 139.767, "memo": "ご飯屋さん"},
    {"name": "BBB", "lat": 35.689, "lng": 139.700, "memo": "ご飯屋さん"}

]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shops')
def get_shops():
    return jsonify(shops)
if __name__ == '__main__':
    app.run(debug=True)