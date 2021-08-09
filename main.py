from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.toolbar import MDToolbar
from kivy.base import EventLoop
from memorymapview import MemoryMapView


class StreetMemoryApp(MDApp):
    def on_start(self):
        EventLoop.window.bind(on_keyboard=self.return_click)

    def build(self):
        Builder.load_file('main.kv')
        return RootWidget()

    def return_click(self, window, key, *args):
        if key == 27:  # escape key or Android return button
            return True


class RootWidget(ScreenManager):
    pass


class HomeScreen(Screen):
    pass


if __name__ == '__main__':
    theApp = StreetMemoryApp()
    import bugs
    bugs.fixBugs()
    theApp.run()
