import streamlit as st
import matplotlib.pyplot as plt
from weather import get_weather, get_forecast, get_5day_forecast

# PAGE CONFIG
st.set_page_config(page_title="Weather Pro", page_icon="🌦️", layout="wide")

# CUSTOM CSS
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #1e3c72, #2a5298);
    color: white;
}

.card {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 20px;
    margin: 10px 0;
}

.big-temp {
    font-size: 60px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("🌍 Controls")
city = st.sidebar.text_input("Enter City", "Kolkata")

# TITLE
st.title("🌦️ Weather Dashboard Pro")

if city:
    weather = get_weather(city)

    if weather:
        desc = weather["description"].lower()

        if "rain" in desc:
            icon = "🌧️"
        elif "clear" in desc:
            icon = "☀️"
        elif "cloud" in desc:
            icon = "☁️"
        else:
            icon = "🌡️"

        # HEADER
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(f"""
            <div class="card">
                <h2>{icon} {weather['city']}</h2>
                <div class="big-temp">{weather['temperature']}°C</div>
                <p>{weather['description'].title()}</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="card">
                <p>🤔 Feels Like: {weather['feels_like']}°C</p>
                <p>💧 Humidity: {weather['humidity']}%</p>
                <p>🌬 Wind: {weather['wind']} m/s</p>
                <p>ضغط Pressure: {weather['pressure']} hPa</p>
            </div>
            """, unsafe_allow_html=True)

        # METRICS
        st.subheader("📊 Key Metrics")
        m1, m2, m3, m4 = st.columns(4)

        m1.metric("Temperature", f"{weather['temperature']}°C")
        m2.metric("Humidity", f"{weather['humidity']}%")
        m3.metric("Wind", f"{weather['wind']} m/s")
        m4.metric("Pressure", f"{weather['pressure']} hPa")

        st.divider()

        # 24H FORECAST
        forecast = get_forecast(city)

        if forecast:
            temps, times = forecast

            st.subheader("📈 24-Hour Trend")

            plt.figure()
            plt.plot(temps, marker='o')
            plt.xticks(range(len(times)), times, rotation=45)
            plt.xlabel("Time")
            plt.ylabel("Temp (°C)")
            plt.title("Temperature Trend")

            st.pyplot(plt)

        # 5-DAY FORECAST
        st.subheader("📅 5-Day Forecast")
        forecast_5 = get_5day_forecast(city)

        if forecast_5:
            cols = st.columns(5)
            for i, day in enumerate(forecast_5):
                cols[i].markdown(f"""
                <div class="card">
                    <h4>{day['date']}</h4>
                    <p>🌡 {day['temp']}°C</p>
                </div>
                """, unsafe_allow_html=True)

    else:
        st.error("❌ Could not fetch weather data. Check API key or city.")

else:
    st.warning("⚠️ Please enter a city")