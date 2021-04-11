import pandas as pd
from IPython.display import display
import folium
from folium import plugins
from folium.plugins import MeasureControl
from folium.plugins import HeatMap
import re

def generateBaseMap(default_location=[37.76, -122.45], tiles='OpenStreetMap', default_zoom_start=12):
    '''
    Create a map
    '''
    base_map = folium.Map(
        location = default_location
        , control_scale = True
        , zoom_start = default_zoom_start
    )
    return base_map





base_map = generateBaseMap(default_location=[37.76, -122.45], tiles='OpenStreetMap', zoom_start=12)

m = folium.Map(location=[-23.877610095191628, 135.01297734173076], tiles='OpenStreetMap', zoom_start=12)