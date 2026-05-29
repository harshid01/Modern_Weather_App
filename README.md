# 🌤 Weather App

A desktop weather application made with Python and Tkinter that shows real-time weather information using the OpenWeather API.

I created this project to improve my Python skills and learn how APIs work in real applications. The app has a modern dark-themed interface where users can search weather details by entering a city name and country code.

---

## 🚀 Features

* Real-time weather data
* Search weather by city and country code
* Shows:

  * Temperature
  * Feels like temperature
  * Humidity
  * Weather condition
  * Wind speed
* Modern GUI using Tkinter
* Dark theme interface
* Responsive and resizable window

---

## 🛠 Technologies Used

* Python
* Tkinter
* Requests Library
* OpenWeather API

---

## 📦 Installation

### 1. Clone Repository

```bash id="kq51dh"
git clone https://github.com/your-username/weather-app.git
```

### 2. Open Project Folder

```bash id="x8r0vl"
cd weather-app
```

### 3. Install Required Packages

```bash id="p2c6my"
pip install requests
```

If pip does not work:

```bash id="w4u9se"
py -m pip install requests
```

---

## 🔑 Setup API Key

Create a free API key from OpenWeather:

https://openweathermap.org/api

Replace this line in `app.py`:

```python id="f9n3yb"
api_key = "YOUR_API_KEY"
```

with your own API key.

---

## ▶ Run the Application

```bash id="z1t7qk"
py app.py
```

---

## 🌍 Example

| City      | Country Code |
| --------- | ------------ |
| Ahmedabad | IN           |
| London    | UK           |
| New York  | US           |

---

## 📁 Project Structure

```txt id="m5w2rp"
weather-app/
│
├── app.py
├── README.md
```

---

## 👨‍💻 Developer

Harshid Panchal
