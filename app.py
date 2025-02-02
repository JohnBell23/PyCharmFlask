# Minimum app.py for debugging -->>

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello my flask server test</h1>"

if __name__ == "__main__":
    app.run(debug=True)
# <<--
