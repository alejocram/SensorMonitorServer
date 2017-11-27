from flask import Flask, request, jsonify
from flask.ext.pymongo import PyMongo
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'sensor_monitor'
app.config['MONGO_URI'] = 'mongodb://<user>:<user>@ds259325.mlab.com:59325/sensor_monitor'

mongo = PyMongo(app)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/add',methods=['POST'])
def add():
    content = request.json
    var1 = content['var1']
    var2 = content['var2']
    print("var1", var1)
    print("var2", var2)

    if var1 and var2:
        user = mongo.db.users
        user.insert({'var1': var1, 'var2': var2})
        return jsonify({'success': '1'})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
