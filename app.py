
from flask import Flask, render_template, request

import additional_routes
from Service.MainService import MainService

app = Flask(__name__)

app.register_blueprint(additional_routes.additional_bp)


m_main_service = MainService()

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print("old opt " + m_main_service.selected_option)
        m_main_service.selected_option = request.form.get('dropdown')
        print("new opt " + m_main_service.selected_option)
        return render_template('options.html', service = m_main_service)
    else:
        return render_template('base.html', service = m_main_service)

@app.route('/hello')
def hello():
    return 'Hello, App'

if __name__ == "__main__":
    app.run(debug=True)

