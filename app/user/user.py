from flask import Blueprint

user_blueprints = Blueprint('user', __name__)

@user_blueprints.route('/btest', methods=['GET', 'POST'])
def hello_world():
    return 'btest '
