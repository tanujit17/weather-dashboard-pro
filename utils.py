import requests

def get_user_location():
    try:
        res = requests.get("http://ip-api.com/json/", timeout=5)
        data = res.json()
        return data.get("city", "Kolkata")
    except:
        return "Kolkata"