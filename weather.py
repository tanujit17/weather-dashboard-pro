import requests
from config import API_KEY, BASE_URL, FORECAST_URL


def get_weather(city):
    try:
        if not API_KEY:
            return None

        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url, timeout=10)
        data = res.json()

        if res.status_code != 200:
            print("API ERROR:", data)
            return None

        return {
            "city": data.get("name"),
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }

    except Exception as e:
        print("ERROR:", e)
        return None


def get_forecast(city):
    try:
        url = f"{FORECAST_URL}?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url, timeout=10)
        data = res.json()

        if res.status_code != 200:
            return None

        temps, times = [], []

        for item in data["list"][:8]:
            temps.append(item["main"]["temp"])
            times.append(item["dt_txt"].split(" ")[1][:5])

        return temps, times

    except:
        return None


def get_5day_forecast(city):
    try:
        url = f"{FORECAST_URL}?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url, timeout=10)
        data = res.json()

        if res.status_code != 200:
            return None

        daily = {}

        for item in data["list"]:
            date = item["dt_txt"].split(" ")[0]
            temp = item["main"]["temp"]

            daily.setdefault(date, []).append(temp)

        result = []
        for date, temps in list(daily.items())[:5]:
            result.append({
                "date": date,
                "temp": round(sum(temps)/len(temps), 1)
            })

        return result

    except:
        return None