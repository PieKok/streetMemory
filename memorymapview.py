from kivy_garden.mapview import MapView


class MemoryMapView(MapView):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.is_double_tap:
            print('Touch is a double tap !')
            print(touch)
            print(' - distance between previous is', touch.double_tap_distance)
        else:
            super().on_touch_down(touch)