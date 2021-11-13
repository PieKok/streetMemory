from kivy_garden.mapview import MapView, MapMarker
import random
from geopy.geocoders import Nominatim

class MemoryMapView(MapView):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.is_double_tap:
            print('Touch is a double tap !')
            print(touch)
            lonlat_coordinates = self.get_latlon_at(touch.x, touch.y)
            my_marker = MapMarker(lat=lonlat_coordinates.lat, lon=lonlat_coordinates.lon)
            self.add_marker(my_marker)

        else:
            super().on_touch_down(touch)