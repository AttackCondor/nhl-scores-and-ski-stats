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

def get_mountain_forecast_json(mountain_id, app_id, app_key, hourly_interval = None, num_of_days = None):
    try:
        #attempt to retrieve the forecast, if hourly interval is not provided default to 12, if num_of_days is not provided default to 1
        data = requests.get(
            FORMAT_URL.format(mountain_id, app_id, app_key, ("12",hourly_interval)[hourly_interval is not None], (1,num_of_days)[num_of_days is not None]), 
            timeout=REQUEST_TIMEOUT
        )
        return data.json()
    except requests.exceptions.RequestException as e:
        raise ValueError(e)

def get_weekly_mountain_forecast_json(mountain_id, app_id, app_key, hourly_interval = None):
    try:
        #attempt to retrieve the forecast, if hourly interval is not provided default to 12
        data = requests.get(
            FORMAT_URL.format(mountain_id, app_id, app_key, ("12",hourly_interval)[hourly_interval is not None], 7), 
            timeout=REQUEST_TIMEOUT
        )
        return data.json()
    except requests.exceptions.RequestException as e:
        raise ValueError(e)

def get_todays_mountain_forecast(mountain_id, app_id, app_key, month, day, hour):
    try:
        #attempt to retrieve the most current forecast, TODO: parsing and removing extra data
        data = requests.get(
            FORMAT_URL.format(mountain_id, app_id, app_key, 1, 1)
        )
    except requests.exceptions.RequestException as e:
        raise ValueError(e)

    data = data.json()
    #Parse the 

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
