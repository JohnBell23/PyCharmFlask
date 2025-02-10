from flask import Blueprint, render_template, request

from counter.service.auto_counter_service import AutoCounterService
from counter.service.counter_service import CounterService

counter_bp = Blueprint('counter', __name__, url_prefix='/counter')

m_counter_service = CounterService()
m_auto_counter_service = AutoCounterService()

@counter_bp.route('/title')
def index_add():
    return "<h1>hello from title</h1>"


@counter_bp.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        m_counter_service.increment()
    return render_template('counter.html', service = m_counter_service, autocounter = m_auto_counter_service)

