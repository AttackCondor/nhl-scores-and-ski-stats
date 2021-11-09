import json
import requests
import debug

#Simple base URL to contruct subsequent URLs
BASE_URL = "https://api.weatherunlocked.com/api/resortforecast/"
#Simplest for of the get forecast request, can be used when attempting defaults
FUNCTIONAL_URL = BASE_URL + '{0}?app_id={1}&app_key={2}'
#Include the typical parameters for the forecast request
FORMAT_URL = BASE_URL + '{0}?app_id={1}&app_key={2}&hourly_interval{3}&num_of_days={4}'
#The timeout used for the get requests
REQUEST_TIMEOUT = 5

TIMEOUT_TESTING = 0.001  # TO DELETE

def get_mountain_forecast_json(mountain_id, app_id, app_key, hourly_interval = 12, num_of_days = 1):
    try:
        #attempt to retrieve the forecast, if hourly interval is not provided default to 12, if num_of_days is not provided default to 1
        data = requests.get(
            FORMAT_URL.format(mountain_id, app_id, app_key, hourly_interval, num_of_days), 
            timeout=REQUEST_TIMEOUT
        )
        return data.json()
    except requests.exceptions.RequestException as e:
        raise ValueError(e)

def get_weekly_mountain_forecast_json(mountain_id, app_id, app_key, hourly_interval = 12):
    try:
        #attempt to retrieve the forecast, if hourly interval is not provided default to 12
        data = requests.get(
            FORMAT_URL.format(mountain_id, app_id, app_key, hourly_interval, 7), 
            timeout=REQUEST_TIMEOUT
        )
        return data.json()
    except requests.exceptions.RequestException as e:
        raise ValueError(e)

def get_todays_mountain_forecast(mountain_id, app_id, app_key):
    try:
        #attempt to retrieve the most current forecast, TODO: parsing and removing extra data
        data = requests.get(
            FORMAT_URL.format(mountain_id, app_id, app_key, 6, 1)
        )
    except requests.exceptions.RequestException as e:
        raise ValueError(e)

    data = data.json()
    #Parse the forecast for the times at 7am, 1pm, and 7pm
    morn = data["forecast"][1]
    mid = data["forecast"][2]
    night = data["forecast"][3]

    high = max(morn["base"]["temp_max_f"], mid["base"]["temp_max_f"], night["base"]["temp_max_f"])
    low = min(morn["base"]["temp_min_f"], mid["base"]["temp_min_f"], night["base"]["temp_min_f"])
    desc = mid["base"]["wx_desc"]
    fresh_snow = sum(morn["snow_in"], mid["snow_in"], night["snow_in"])
    forecast = {"high":high, "low":low, "desc":desc, "fresh_snow":fresh_snow}
    return forecast
    

def get_mountain_name(mountain_id, app_id, app_key):
    try:
        #attempt to retrieve the most current forecast, TODO: parsing and removing extra data
        data = requests.get(
            FUNCTIONAL_URL.format(mountain_id, app_id, app_key)
        ).json()
    except requests.exceptions.RequestException as e:
        raise ValueError(e)
    mountain_name = data["name"]
    return mountain_name
