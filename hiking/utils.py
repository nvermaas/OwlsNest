import requests
import gpxpy

from .models import Hike

def get_waypoints_from_hike(hike):
    location = hike.location
    waypoints = []

    for wpt in location['waypoints']:
        waypoints.append({
            "name": wpt['name'],
            "latitude": wpt['latitude'],
            "longitude": wpt['longitude'],
            "elevation": 0,
            "time": None,
            "description": wpt['name'],
            "symbol": wpt['type'],
            "comment": "",
            "type": wpt['type'],
        })

   # {'name': 'RogenVallen', 'latitude': 62.34841426, 'longitude': 12.57700774, 'elevation': 767.492,
   #  'time': datetime.datetime(2024, 9, 3, 9, 43, 26, tzinfo=SimpleTZ('Z')), 'description': None, 'symbol': 'Car',
  #   'comment': '03-SEP-24 11:43:26', 'type': 'car'}


    return waypoints


def get_waypoints_from_gpx(url):
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
            "type": wpt.type,
        })

    return waypoints

def extract_points(hike):
    """
    extract a list of points from the GPX and/or the location json structure
    these points will be plotted as markers on  the map.
    """
    points = []

    # first display the gpx file (if something goes wrong, just continue)
    try:
        if hike.gpx:
            waypoints = get_waypoints_from_gpx(hike.gpx)

            # do some refinement
            for waypoint in waypoints:
                # if the name is 3 characters, then it is probably a waypoint that I didn't give a name
                # so if it is a campground, then it was probably a potential camp along the way, and not a
                # campsite where we stayed. So change the type here, so I can render it differently on the map.
                try:
                    waypoint['type'] = waypoint['type'].lower()
                except:
                    waypoint['type'] = waypoint['symbol'].lower()

                if (waypoint['type'] == 'campground'):
                    name = waypoint['name']
                    if (len(name) == 3):
                        waypoint['type'] = "campsite"
                    else:
                        waypoint['type'] = "camped"

                if (waypoint['type'] == 'town'):
                    waypoint['type'] = "residence"


                points.append(waypoint)
                print(f" {waypoint['name']} => {waypoint['type']}")
    except Exception as error:
        print(error)

    if hike.waypoints:
        waypoints = get_waypoints_from_hike(hike)
        for waypoint in waypoints:
            points.append(waypoint)


    return points