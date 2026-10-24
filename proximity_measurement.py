"""Calculate straight-line distances between map-selected coordinates.

Provide latitude/longitude for the launch site and each reference feature.
The results depend on the coordinates selected and are not road distances.
"""
from math import radians, sin, cos, asin, sqrt

EARTH_RADIUS_KM = 6371.0088

def haversine_km(lat1, lon1, lat2, lon2):
    """Return great-circle distance in kilometres."""
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 2 * EARTH_RADIUS_KM * asin(sqrt(a))

if __name__ == "__main__":
    print("Enter coordinates selected from your map; values below are examples only.")
    launch_lat = float(input("Launch site latitude: "))
    launch_lon = float(input("Launch site longitude: "))
    features = ["Shoreline", "Railway", "Highway", "Titusville centre"]
    for name in features:
        lat = float(input(f"{name} latitude: "))
        lon = float(input(f"{name} longitude: "))
        print(f"{name}: {haversine_km(launch_lat, launch_lon, lat, lon):.2f} km")
