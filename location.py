import geocoder
import tkinter as tk 
def get_current_location():
    g = geocoder.ip('me')
    return g.latlng

def main():
    latitude, longitude = get_current_location()
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

if __name__ == "__main__":
    main()
