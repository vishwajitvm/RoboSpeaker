import requests
import json
import pyttsx3  # For text-to-speech

# Initialize the TTS engine
engine = pyttsx3.init()

#Start infinite loop to accept multiple city names
while True:
    # Ask user to enter city name
    city = input("Enter City Name (or 'x' to exit): ")

    # Exit condition
    if city.lower() == 'x':
        engine.say("Goodbye! Have a nice day.")
        engine.runAndWait()
        break

    try:
        # Build API URL using the city input
        url = f"https://api.weatherapi.com/v1/current.json?key=e8485eeaf61e47739d0190252252106&q={city}"

        # Send request to the API
        request = requests.get(url)
        request.raise_for_status()  # Raise error for bad responses

        # Parse the JSON response
        weatherDict = json.loads(request.text)

        # Extract temperature
        temp = weatherDict["current"]["temp_c"]

        # Prepare the response string
        output = f"The current temperature in {city} is {temp} degrees Celsius."

        print(output)

        # Speak the temperature using TTS
        engine.say(output)
        engine.runAndWait()

    except Exception as e:
        print("Sorry, could not fetch weather data. Please check the city name.")
        engine.say("Sorry, I could not find the weather information for that city.")
        engine.runAndWait()
