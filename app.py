import requests
import tkinter as tk
from tkinter import messagebox

# =========================
# API KEY
# =========================
api_key = "[Write Your API Key Here"

# =========================
# GET WEATHER FUNCTION
# =========================
def get_weather():

    city = city_entry.get()
    country = country_entry.get()

    if city == "" or country == "":
        messagebox.showerror("Error", "Please enter city and country code")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:

            city_name = data["name"]
            country_code = data["sys"]["country"]
            temp = data["main"]["temp"]
            feels = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]
            wind = data["wind"]["speed"]

            result = f"""
📍 {city_name}, {country_code}

🌡 Temperature : {temp} °C
🤗 Feels Like : {feels} °C
💧 Humidity   : {humidity} %
🌥 Condition  : {weather}
🌬 Wind Speed : {wind} m/s
"""

            result_label.config(text=result)

        else:
            messagebox.showerror("Error", data["message"])

    except Exception as e:
        messagebox.showerror("Error", str(e))


# =========================
# MAIN WINDOW
# =========================
root = tk.Tk()

root.title("Modern Weather App")

# Default Window Size
root.geometry("1000x700")

# Minimum Size
root.minsize(700, 600)

# Allow Resize
root.resizable(True, True)

# Background Color
root.configure(bg="#121212")

# =========================
# TITLE
# =========================
title = tk.Label(
    root,
    text="🌤 Weather App",
    font=("Segoe UI", 24, "bold"),
    fg="white",
    bg="#121212"
)
title.pack(pady=20)

# =========================
# MAIN FRAME
# =========================
frame = tk.Frame(root, bg="#1E1E1E", bd=0)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# =========================
# CITY LABEL + ENTRY
# =========================
city_label = tk.Label(
    frame,
    text="City Name (e.g. Patan, New York)",
    font=("Segoe UI", 12),
    fg="white",
    bg="#1E1E1E"
)
city_label.pack(pady=(30,5))

city_entry = tk.Entry(
    frame,
    font=("Segoe UI", 14),
    width=25,
    relief="flat",
    bg="#2A2A2A",
    fg="white",
    insertbackground="white"
)
city_entry.pack(ipady=8)

# =========================
# COUNTRY LABEL + ENTRY
# =========================
country_label = tk.Label(
    frame,
    text="Country Code (e.g. India - IN, United State - US)",
    font=("Segoe UI", 12),
    fg="white",
    bg="#1E1E1E"
)
country_label.pack(pady=(20,5))

country_entry = tk.Entry(
    frame,
    font=("Segoe UI", 14),
    width=25,
    relief="flat",
    bg="#2A2A2A",
    fg="white",
    insertbackground="white"
)
country_entry.pack(ipady=8)

# =========================
# SEARCH BUTTON
# =========================
search_btn = tk.Button(
    frame,
    text="Get Weather",
    font=("Segoe UI", 14, "bold"),
    bg="#00ADB5",
    fg="white",
    activebackground="#00CED1",
    relief="flat",
    cursor="hand2",
    command=get_weather
)
search_btn.pack(pady=30, ipadx=20, ipady=10)

# =========================
# RESULT AREA
# =========================
result_label = tk.Label(
    frame,
    text="",
    font=("Consolas", 14),
    fg="white",
    bg="#1E1E1E",
    justify="left"
)
result_label.pack(pady=20)

# =========================
# FOOTER
# =========================
footer = tk.Label(
    root,
    text="Created by Harshid panchal",
    #text="Powered by OpenWeather API",
    font=("Segoe UI", 10),
    fg="gray",
    bg="#121212"
)
footer.pack(pady=10)

# =========================
# RUN APP
# =========================
root.mainloop()
