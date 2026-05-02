# Sheridan Dela Cruz
# May 2, 2026
# Module 7.2

# Function returns a formatted "City, Country" string.
def city_country(city, country, population=None, language=None):
    result = f"{city}, {country}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language}"
    return result

# Example calls to show how the function works.
print(city_country("Lisbon", "Portugal"))
print(city_country("Jakarta", "Indonesia", 10500000))
print(city_country("Zurich", "Switzerland", 430000, "German"))

