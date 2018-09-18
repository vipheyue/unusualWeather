from enum import Enum, unique


class WeatherEnum(Enum):
    CLEAR_DAY = "晴天"
    CLEAR_NIGHT = "晴夜"
    PARTLY_CLOUDY_DAY = '多云'
    PARTLY_CLOUDY_NIGHT = '多云'
    CLOUDY = '阴'
    RAIN = '雨'
    SNOW = '雪'
    WIND = '风'
    HAZE = '雾霾沙尘'
