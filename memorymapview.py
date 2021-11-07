from kivy_garden.mapview import MapView, MapMarker
import random
from geopy.geocoders import Nominatim

class MemoryMapView(MapView):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.is_double_tap:
            print('Touch is a double tap !')
            print(touch)
            print(' - distance between previous is', touch.double_tap_distance)
            print(self.get_bbox())
            print(self.width)
            print(self.height)
            x_random = self.width * random.random()
            y_random = self.height * random.random()
            print(' x = ', x_random)
            print(' y = ', y_random)
            print(self.get_latlon_at(x_random,y_random))
            lonLat_coordinates = self.get_latlon_at(x_random, y_random)
            marker1 = MapMarker(lat=lonLat_coordinates.lat, lon=lonLat_coordinates.lon)
            self.add_marker(marker1)
            print(marker1)
            app = Nominatim(user_agent='StreetMemory')
            address = app.reverse(lonLat_coordinates)
            print(address.raw['address']['road'])


        else:
            super().on_touch_down(touch)