#!/usr/bin/env python3

import datetime
import re
import requests

airport = 'KAUS'
metar_base = 'https://aviationweather.gov/adds/dataserver_current/httpparam?'
metar_params = 'dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow=3&mostRecent=true&stationString=%s' % airport
metar_url = metar_base + metar_params

raw = requests.get(metar_url).text
wind_kt = re.search('<wind_speed_kt>(.*)</wind_speed_kt>', raw)
if wind_kt is not None:
    wind_mph = round(1.15*float(wind_kt.group(1)), 1)

darksky_base = 'https://darksky.net/forecast/'
darksky_params = '30.1449,-97.6708/us12/en'
darksky_url = darksky_base + darksky_params
raw = requests.get(darksky_url).text
result = re.search(r'Wind.*?num swip\">(\d+)</span', raw, flags=re.S|re.M)
if result is not None:
    darksky_wind_mph = round(float(result.group(1)), 1)

timestamp_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M') 
print('%s, %s, %s' % (timestamp_str, wind_mph, darksky_wind_mph))
