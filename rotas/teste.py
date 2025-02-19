from flask import *

teste_bp = Blueprint('usuarios', __name__)

@teste_bp.route('/a')
def teste():
    return 'xfdsfsdg'

