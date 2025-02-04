from flask import Blueprint, render_template, request

from main.service.main_service import MainService

main_bp = Blueprint('main', __name__, url_prefix='/')

m_main_service = MainService()

@main_bp.route('/title')
def index_add():
    return "<h1>hello from title</h1>"


@main_bp.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print("old opt " + m_main_service.selected_option)
        m_main_service.selected_option = request.form.get('dropdown')
        print("new opt " + m_main_service.selected_option)
        return render_template('options.html', service = m_main_service)
    else:
        return render_template('main.html', service = m_main_service)

@main_bp.route('/hello')
def hello():
    return 'Hello, Main'
