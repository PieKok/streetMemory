from kivy_garden.mapview import MapView, MapMarker


class MemoryMapView(MapView):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.guess_marker = None
        self.target_marker = None

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.is_double_tap:
            lonlat_coordinates = self.get_latlon_at(touch.x, touch.y)
            if self.guess_marker is not None:
                self.remove_marker(self.guess_marker)
            self.guess_marker = MapMarker(lat=lonlat_coordinates.lat, lon=lonlat_coordinates.lon, source="marker.png")
            self.add_marker(self.guess_marker)
        else:
            super().on_touch_down(touch)

    def set_target_marker(self, latlon):
        if self.target_marker is not None:
            self.remove_marker(self.target_marker)
        self.target_marker = MapMarker(lat=latlon.lat, lon=latlon.lon, source="marker-green.png")
        self.add_marker(self.target_marker)

    def remove_target_marker(self):
        if self.target_marker is not None:
            self.remove_marker(self.target_marker)
