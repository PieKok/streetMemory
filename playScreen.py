from kivy.uix.screenmanager import Screen
import random
from kivy_garden.mapview import MapMarker
from geopy.geocoders import Nominatim
from memorymapview import MemoryMapView
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class PlayScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.x_target = 0
        self.y_target = 0
        self.lonlat_target = None
        self.street_target = ""
        self.results_dialog = None

    def actionButton(self):
        my_mapview = self.ids.mapViewer
        if self.ids.toolbar.ids.right_actions.children[0].icon == "play":
            self.x_target = my_mapview.width * random.random()
            self.y_target = my_mapview.height * random.random()
            self.lonlat_target = my_mapview.get_latlon_at(self.x_target, self.y_target)
            my_geo_app = Nominatim(user_agent='StreetMemory')
            my_address = my_geo_app.reverse(self.lonlat_target)
            while not ("road" in my_address.raw['address']):
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
            self.results_dialog = MDDialog(
                type="custom",
                content_cls=ResultDialogContent(),
                size_hint=(0.8, 0.1),
                buttons=[
                    MDFlatButton(
                        text="Ok", on_release=self.close_results_dialog
                    )
                ]
            )
            self.results_dialog.open()
            guess_street = self.get_guess_address()
            my_str = 'Target: ' + self.street_target + '\nGuess: ' + guess_street
            self.results_dialog.content_cls.ids.id_result_text.text = my_str

    def get_guess_address(self):
        my_mapview = self.ids.mapViewer
        my_geo_app = Nominatim(user_agent='StreetMemory')
        my_guess_address = my_geo_app.reverse([my_mapview.guess_marker.lat, my_mapview.guess_marker.lon])
        if "road" in my_guess_address.raw['address']:
            return my_guess_address.raw['address']['road']
        else:
            return "No street found"

    def close_results_dialog(self, inst):
        self.results_dialog.dismiss()


class ResultDialogContent(BoxLayout):
    pass