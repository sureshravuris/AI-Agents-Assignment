import random

class WeatherInformerAgent:
    def __init__(self):
        self.weather_data = {
            'sunny': ['clear skies', 'sunny', 'mostly sunny'],
            'cloudy': ['cloudy', 'overcast', 'partly cloudy'],
            'rainy': ['rainy', 'light rain', 'thunderstorms'],
            'snowy': ['snowy', 'light snow showers', 'blizzards']
        }

    def fetch_weather(self, location):
        # Simulate fetching weather by randomly selecting a condition
        condition = random.choice(list(self.weather_data.keys()))
        description = random.choice(self.weather_data[condition])
        temperature = random.randint(-5, 35)  # Simulated temperature range
        return condition, description, temperature

    def report_weather(self, location):
        condition, description, temperature = self.fetch_weather(location)
        print(f"Weather report for {location}:")
        print(f"Condition: {description.capitalize()}")
        print(f"Temperature: {temperature}°C\n")

# Example usage
agent = WeatherInformerAgent()
location = input("Enter a location (city) to get the weather report: ")
agent.report_weather(location)
