class WeatherBean:
    def __init__(self, rain_have=False, rain_desc=' 7', temperature_highest_scop=None, temperature_lowest_scop=None,
                 temperature_current=None, temperature_next_moment=None, temperature_after_work=None,
                 temperature_desc=None, aqi_max=None, aqi_desc=None, rain_suggest='', temperature_suggest='',
                 aqi_suggest='', aqi_needmasks=None):
        self.rain_have = rain_have
        self.rain_desc = rain_desc
        self.rain_suggest = rain_suggest
        self.temperature_highest_scop = temperature_highest_scop#单位时间内最高温度 {'value': 20.79, 'datetime': '2018-09-19 10:00'}
        self.temperature_lowest_scop = temperature_lowest_scop#单位时间内最低温度
        self.temperature_current = temperature_current
        self.temperature_next_moment = temperature_next_moment
        self.temperature_after_work = temperature_after_work
        self.temperature_desc = temperature_desc
        self.temperature_suggest = temperature_suggest
        self.aqi_needmasks = aqi_needmasks
        self.aqi_max = aqi_max
        self.aqi_suggest = aqi_suggest
        self.aqi_desc = aqi_desc

    def get_suggest(self):
        return self.rain_suggest+self.aqi_suggest+self.temperature_suggest+"\n \n"+self.rain_desc
if __name__ == '__main__':
    # bean = WeatherBean(True, "有")
    # bean = WeatherBean(rain_desc="有")
    bean = WeatherBean()
    print(bean.rain_have)
    print(bean.rain_desc)
