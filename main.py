from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.toolbar import MDToolbar
from kivy.base import EventLoop
import playScreen
from geopy.geocoders import Nominatim



class StreetMemoryApp(MDApp):
    dict_back_transitions = {"play_screen": "home_screen"
                             }

    def on_start(self):
        EventLoop.window.bind(on_keyboard=self.return_click)

    def build(self):
        Builder.load_file('main.kv')
        Builder.load_file("playScreen.kv")
        return RootWidget()

    def change_screen(self, name_screen, direction):
        self.root.transition.direction = direction
        self.root.current = name_screen

    def return_click(self, window, key, *args):
        if key == 27:  # escape key or Android return button
            my_current_screen = self.root.current
            my_destination_screen = self.dict_back_transitions[my_current_screen]
            self.change_screen(my_destination_screen, "right")
            return True

class RootWidget(ScreenManager):
    pass

class HomeScreen(Screen):
    def action_play_button(self):
        geo_app = Nominatim(user_agent='StreetMemory')
        my_latlon = geo_app.geocode(self.ids.area_text_field.text).raw
        self.parent.ids.screen_play.ids.mapViewer.zoom = 14
        self.parent.ids.screen_play.ids.mapViewer.center_on(float(my_latlon["lat"]), float(my_latlon["lon"]))
        my_app = MDApp.get_running_app()
        my_app.change_screen("play_screen", "left")


if __name__ == '__main__':
    theApp = StreetMemoryApp()
    import bugs
    bugs.fixBugs()
    theApp.run()
