# 🔊 RoboSpeaker: Text-to-Speech & Weather Voice Assistant

RoboSpeaker is a simple yet powerful Python-based voice assistant that can **speak any text you type** and **announce the weather** for any city using live weather data — all through **Text-to-Speech** (TTS) technology.

---

## 🎯 Features

- 🗣️ **Text-to-Speech Tool**: Type anything and the program will speak it aloud.
- ☁️ **Weather Announcer**: Enter a city name and get the current temperature spoken out loud.
- 🔁 Loop mode: Use it continuously for multiple entries until you choose to exit.
- ✅ Easy to use and beginner-friendly.

---

## 📦 Requirements

Before running the program, make sure you have Python installed and install the following libraries:

```bash
pip install requests pyttsx3
```

---

## 📁 Project Structure

```bash
RoboSpeaker/
├── wetherApp.py           # Weather-based TTS using weatherapi.com
├── main.py                # General-purpose TTS for any typed text
├── README.md              # Project instructions
```

---

## 🚀 How to Use

### 1. Text-to-Speech (TTS) Mode

Run the following script to make the assistant speak anything you type:

```bash
python tts_speaker.py
```

- Type your sentence.
- The program will speak it out loud.
- Type `bye` to exit.

### 2. Weather Voice Announcer

Run this script to get the spoken temperature for any city:

```bash
python tts_weather.py
```

- Enter any city name (e.g., `London`, `New York`, `Mumbai`).
- The program fetches the current temperature and speaks it.
- Type `x` to exit the program.

> ⚠️ Make sure you're connected to the internet.

---

## 🔑 Weather API

This project uses [WeatherAPI.com](https://www.weatherapi.com/) to fetch real-time weather data. You can sign up to get your own free API key if needed.

---

## 🧠 Customization

You can customize:
- The voice or rate of speech using `pyttsx3` settings.
- Add more weather details (like humidity or wind) to the spoken output.
- Replace the API key for your own usage.

---


## 👨‍💻 Created By

**Vishwajit VM**  
📧 Email: [vishwajitmall50@gmail.com](mailto:vishwajitmall50@gmail.com)

---

Enjoy the power of speech in Python! 🔉
