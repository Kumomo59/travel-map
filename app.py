from flask import Flask, render_template, jsonify
app = Flask(__name__)

shops = [
    {  "name": "相鉄ホテルズ　ザ　スプラジール　ソウル明洞","lat": 37.5620767,"lng":126.9789844,"memo":"ホテル"},
    { "name":"仁川国際空港　第2ターミナル","lat": 37.4688005, "lng": 126.4333885, "memo":"空港" },
    { "name":"ダイソー　ソウル駅店","lat":37.5542871,"lng":126.9719456,"memo":"ソウル駅1番出口付近"}

]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shops')
def get_shops():
    return jsonify(shops)
if __name__ == '__main__':
    app.run(debug=True)