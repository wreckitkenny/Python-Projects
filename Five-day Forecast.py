#!/usr/bin/env python3
import requests
from datetime import datetime

api_key = "bUVmjeqq2QjIOEGH6uPGB0Any4ALGGvk"
location = "hanoi"


def get_location_key(loc):
    _parameters = {"apikey": api_key, "q": loc}
    _url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    _request = requests.get(_url, params=_parameters)
    _info = _request.json()
    return(_info[0]["Key"])


def five_day_forecast():
    _num = 1
    _parameters = {"apikey": api_key, "metric": "true"}
    _url = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/\
                                    {}".format(get_location_key(location))
    _request = requests.get(_url, params=_parameters)
    _info = _request.json()
    print("")
    print("====== 5 Days of Daily Forecasts ======")
    for i in _info["DailyForecasts"]:
        _date = str(i["Date"][8:10]) + "/" + str(i["Date"][5:7]) + "/"\
                    + str(i["Date"][0:4])
        _maxtemp = i["Temperature"]["Maximum"]["Value"]
        _mintemp = i["Temperature"]["Minimum"]["Value"]
        print("""{}. Date: {}
    + Maximum Temperature: {}°C
    - Minimum Temperature: {}°C""".format(_num, _date, _maxtemp, _mintemp))
        _num += 1


if __name__ == '__main__':
    print("""
====== Current Date & Time ======
Time: {:%X}""".format(datetime.now()))
    print("Weekday: {:%A}".format(datetime.now()))
    print("Date: {:%d/%m/%Y}".format(datetime.now()))
    five_day_forecast()
