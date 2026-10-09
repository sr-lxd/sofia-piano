from flask import Blueprint, render_template

piano_bp = Blueprint('piano', __name__, 
                    template_folder='templates',
                    static_folder='static',
                    url_prefix='/piano')

@piano_bp.route('/')
def index():
    """钢琴主页"""
    return render_template('piano_index.html')