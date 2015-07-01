from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/notify', methods=['POST'])
def hello_world():
    return 

if __name__ == '__main__':
    app.run()
