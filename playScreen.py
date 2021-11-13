from kivy.uix.screenmanager import Screen
import random
from kivy_garden.mapview import MapMarker
from geopy.geocoders import Nominatim
from memorymapview import MemoryMapView


class PlayScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.x_target = 0
        self.y_target = 0
        self.lonlat_target = None
        self.street_target = ""

    def actionButton(self):
        if self.ids.toolbar.ids.right_actions.children[0].icon == "play":
            self.x_target = self.ids.mapViewer.width * random.random()
            self.y_target = self.ids.mapViewer.height * random.random()
            self.lonlat_target = self.ids.mapViewer.get_latlon_at(self.x_target, self.y_target)
            my_geo_app = Nominatim(user_agent='StreetMemory')
            my_address = my_geo_app.reverse(self.lonlat_target)
            self.street_target = my_address.raw['address']['road']
            self.ids.id_street_text.text = "  Double-tap where you think " + self.street_target + " is"
            self.ids.toolbar.ids.right_actions.children[0].icon = "check-bold"

        elif self.ids.toolbar.ids.right_actions.children[0].icon == "check-bold":
            my_marker = MapMarker(lat=self.lonlat_target.lat, lon=self.lonlat_target.lon)
            self.ids.mapViewer.add_marker(my_marker)
            self.ids.toolbar.ids.right_actions.children[0].icon = "play"

