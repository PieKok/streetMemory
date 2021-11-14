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
        my_mapview = self.ids.mapViewer
        if self.ids.toolbar.ids.right_actions.children[0].icon == "play":
            self.x_target = my_mapview.width * random.random()
            self.y_target = my_mapview.height * random.random()
            self.lonlat_target = my_mapview.get_latlon_at(self.x_target, self.y_target)
            my_geo_app = Nominatim(user_agent='StreetMemory')
            my_address = my_geo_app.reverse(self.lonlat_target)
            self.street_target = my_address.raw['address']['road']
            self.ids.id_street_text.text = "  Double-tap where you think " + self.street_target + " is"
            my_mapview.remove_target_marker()
            self.ids.toolbar.ids.right_actions.children[0].icon = "check-bold"

        elif self.ids.toolbar.ids.right_actions.children[0].icon == "check-bold":
            my_mapview.set_target_marker(self.lonlat_target)
            self.ids.id_street_text.text = "  This is where " + self.street_target + " is"
            self.ids.toolbar.ids.right_actions.children[0].icon = "play"

