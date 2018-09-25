from flask import Blueprint, request

weather_blueprints = Blueprint('weather', __name__)




@weather_blueprints.route('/realtime', methods=['GET', 'POST'])
def realtime():
    longitude = request.form['longitude']
    latitude = request.form['latitude']
    return f'weather... {longitude}'
