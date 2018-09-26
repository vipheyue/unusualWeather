from flask import Blueprint, request

weather_blueprints = Blueprint('weather', __name__)


@weather_blueprints.route('/realtime', methods=['GET', 'POST'])
def realtime():
    longitude = request.form['longitude']
    latitude = request.form['latitude']
    return f'weather... {longitude}'


@weather_blueprints.route('/unusualWeather', methods=['GET', 'POST'])
def unusual_weather():
    from app.weather.caiyun import realtime, daily_forest
    from app.notice.mail import send_email

    if request.method == 'POST':
        longitude = request.form['longitude']
        latitude = request.form['latitude']
        receiverEmail = request.form['receiverEmail']
        result = daily_forest(longitude, latitude)
        if result != '':
            # 发送邮件
            send_email(receiverEmail, result)
            return str(result)
        return "no unusual weather."
    else:
        return 'get method  no support'
