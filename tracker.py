import requests

def track_location():
    url = "https://ipinfo.io/json"
    response = requests.get(url)
    data = response.json()

    print("Geolocation Details")
    print("----------------------")
    print("IP Address :", data.get("ip"))
    print("City       :", data.get("city"))
    print("Region     :", data.get("region"))
    print("Country    :", data.get("country"))
    print("Location   :", data.get("loc"))  # Latitude, Longitude
    print("ISP        :", data.get("org"))

    # Google Maps Link
    location = data.get("loc")
    if location:
        lat, lon = location.split(",")
        print("\nGoogle Maps Link:")
        print(f"https://www.google.com/maps?q={lat},{lon}")

track_location()
