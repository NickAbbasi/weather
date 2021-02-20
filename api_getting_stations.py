import json
import time
import datetime
from urllib.request import urlopen

def get_stations_from_networks(test):
    if test == 'y':

        list = ['BWI','AXA']
        return list
    else:

        """Build a station list by using a bunch of IEM networks."""
        stations = []
        states = """MD"""
        # IEM quirk to have Iowa AWOS sites in its own labeled network
        networks = ["AWOS"]
        for state in states.split():
            networks.append("%s_ASOS" % (state,))

        for network in networks:
            # Get metadata
            uri = (
                "https://mesonet.agron.iastate.edu/geojson/network/%s.geojson"
            ) % (network,)
            data = urlopen(uri)
            jdict = json.load(data)
            for site in jdict["features"]:
                stations.append(site["properties"]["sid"])
        return stations



station = get_stations_from_networks('y')

print(station)
