
from flask import Flask

from counter.controller import counter_controller
from main.controller import main_controller

app = Flask(__name__)

app.register_blueprint(main_controller.main_bp)
app.register_blueprint(counter_controller.counter_bp)

if __name__ == "__main__":
    app.run(debug=True)

