import requests
import gpxpy


def parse_gpx_waypoints(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    gpx = gpxpy.parse(response.text)

    waypoints = []

    for wpt in gpx.waypoints:
        waypoints.append({
            "name": wpt.name,
            "latitude": wpt.latitude,
            "longitude": wpt.longitude,
            "elevation": wpt.elevation,
            "time": wpt.time,
            "description": wpt.description,
            "symbol": wpt.symbol,
            "comment": wpt.comment,
            "type": wpt.type.lower(),
        })

        print(wpt.type)

    return waypoints

def extract_points(hike):
    """
    extract a list of points from the GPX and/or the location json structure
    these points will be plotted as markers on  the map.
    """
    points = []
    if hike.gpx:
        waypoints = parse_gpx_waypoints(hike.gpx)
        points = waypoints


    return points