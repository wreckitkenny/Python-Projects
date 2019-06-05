#!/usr/bin/env python3
import requests
from datetime import datetime
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="5-day Weather Forecast Tool")
    parser.add_argument("api_key", type=str, help="Accuweather API key")
    parser.add_argument("location", type=str, help="City or Country")
    args = parser.parse_args()
    print("""====== Current Date & Time ======
Time: {:%X}""".format(datetime.now()))
    print("Weekday: {:%A}".format(datetime.now()))
    print("Date: {:%d/%m/%Y}".format(datetime.now()))
    if len(sys.argv) == 3:
        if args.api_key and args.location:
            sys.stdout.write(str(five_day_forecast(args)))


def get_location_key(api_key, loc):
    _parameters = {"apikey": api_key, "q": loc}
    _url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    _request = requests.get(_url, params=_parameters)
    _info = _request.json()
    return(_info[0]["Key"])


def five_day_forecast(args):
    _num = 1
    _parameters = {"apikey": args.api_key, "metric": "true"}
    _url = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/\
                                    {}".format(get_location_key(args.api_key,
                                                                args.location))
    _request = requests.get(_url, params=_parameters)
    _info = _request.json()
    print("")
    print("===== 5 Days of Daily Forecasts =====")
    for i in _info["DailyForecasts"]:
        _date = str(i["Date"][8:10]) + "/" + str(i["Date"][5:7]) + "/"\
                    + str(i["Date"][0:4])
        _maxtemp = i["Temperature"]["Maximum"]["Value"]
        _mintemp = i["Temperature"]["Minimum"]["Value"]
        print("""{}. Date: {}
    + Maximum Temperature: {}°C
    - Minimum Temperature: {}°C""".format(_num, _date, _maxtemp, _mintemp))
        _num += 1
    return("=====================================")


if __name__ == '__main__':
    main()
