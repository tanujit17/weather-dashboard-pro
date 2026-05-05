import os

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    API_KEY = "a52342af108cbef4847905df02bcbb05"  # replace locally

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"