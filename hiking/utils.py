import requests
import gpxpy


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
            "type": wpt.type.lower(),
        })

    return waypoints

def extract_points(hike):
    """
    extract a list of points from the GPX and/or the location json structure
    these points will be plotted as markers on  the map.
    """
    points = []

    # the idea is that waypoints can come from the gpx, but also from the database itself
    # for now, I only read them from the gpx.
    if hike.gpx:
        waypoints = get_waypoints_from_gpx(hike.gpx)

        # do some refinement
        for waypoint in waypoints:
            # if the name is 3 characters, then it is probably a waypoint that I didn't give a name
            # so if it is a campground, then it was probably a potential camp along the way, and not a
            # campsite where we stayed. So change the type here, so I can render it differently on the map.

            if (waypoint['type'] == 'campground'):
                name = waypoint['name']
                if (len(name) == 3):
                    waypoint['type'] = "campsite"
                else:
                    waypoint['type'] = "camped"


            points.append(waypoint)
            print(f" {waypoint['name']} => {waypoint['type']}")

    return points