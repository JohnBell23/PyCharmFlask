from flask import Blueprint, render_template

additional_bp = Blueprint('additional', __name__, url_prefix='/add')

@additional_bp.route('/')
def index():
    return "<h1>hello from additional</h1>"

@additional_bp.route('/add')
def add():
    return "<h1>hello from additional add</h1>"
