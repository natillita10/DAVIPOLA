from node import Node
class city(Node):
    def __init__(self, id, name, lat=None, lon=None):
        super()__init__(id, name)
        self.lat = float(str(lat).raplace(",","."))if lat else None
        self.lon = float(str(lon).raplace(",","."))if lon else None