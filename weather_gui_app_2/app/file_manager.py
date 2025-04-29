def log_weather_data(city, temperature, description):
    with open("weather_log.txt", "a") as f:
        f.write(f"{city}: {temperature}F, {description}\n")

def read_cities_from_file(filename="cities.txt"):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []