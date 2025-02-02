# PyCharmFlask
Demo Flask Project for PyCharm.
How to set up a debuggable Flask project for PyCharm Community Edition.

# Initial setup
- Following https://flask.palletsprojects.com/en/stable/installation/#dependencies to create the .venv
- Create project dir and cd into that dir
- Run >py -3 -m venv .venv
- Run >.venv\Scripts\activate
- Now in the venv  run >pip install Flask
- Add minimum app.py
```
# Minimum app.py for debugging -->>

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello my flask server test</h1>"

if __name__ == "__main__":
    app.run(debug=True)
# <<--
```
- Create PyCharm Debug configuration, set:
  - Run: Project Default (Path to .venv/Scripts/python.exe)
  - script: Path to app.py
  - Parameter: --debug
  - Working dir: Path to project dir
  - Environment variables, add
    - FLASK_APP=app.py
    - FLASK_ENV=development 
    - FLASK_DEBUG=1
- Now start debugging by run debug configuration, changes will be reflected when saving to files. Add breakpoints where needed.
