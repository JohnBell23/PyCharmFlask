
from flask import Flask, render_template

from Service.MainService import MainService

app = Flask(__name__)

m_main_service = MainService()

@app.route("/")
def home():
    return render_template('base.html', service = m_main_service)

@app.route('/hello')
def hello():
    return 'Hello, App'

if __name__ == "__main__":
    app.run(debug=True)

