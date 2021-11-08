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

def get_mountain_forecast(mountain_id, app_id, app_key, hourly_interval = None, num_of_days = None):
    try:
        #attempt to retrieve the forecast, if hourly interval is not provided default to 12, if num_of_days is not provided default to 1
        data = requests.get(
            "api.weatherunlocked.com/api/resortforecast/619002?app_id=eb227ae7&app_key=dc723588891a6e17a9ab088f150fd38f&num_of_days=1", 
            timeout=REQUEST_TIMEOUT
        )
    except requests.exceptions.RequestException as e:
        raise ValueError(e)
    return data

def get_weekly_mountain_forecast(mountain_id, app_id, app_key, hourly_interval = None):
    try:
        #attempt to retrieve the forecast, if hourly interval is not provided default to 12
        data = requests.get(
            FORMAT_URL.format(mountain_id, app_id, app_key, ("12",hourly_interval)[hourly_interval is not None], 7), 
            timeout=REQUEST_TIMEOUT
        )
        return data
    except requests.exceptions.RequestException as e:
        raise ValueError(e)

def get_current_mountain_forecast(mountain_id, app_id, app_key):
    try:
        #attempt to retrieve the most current forecast, TODO: parsing and removing extra data
        data = requests.get(
            FORMAT_URL.format(mountain_id, app_id, app_key, 12, 1)
        )
        return data
    except requests.exceptions.RequestException as e:
        raise ValueError(e)