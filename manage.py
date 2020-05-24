# coding:utf-8
from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
import redis


app = Flask(__name__)
class Config(object):
    """配置信息"""
    debug = True
    SECRET_KEY = "asdhakdhjsasadsad"
    SQLALCHEMY = "mysql://root:123456@192.168.0.104:12345/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REDIS_HOST = "192.168.0.104"
    REDIS_PORT = 6379

app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)

@app.route("/index")
def index():
    return "index"


if __name__ == '__main__':
    app.run(host="192.168.0.104",debug=True)