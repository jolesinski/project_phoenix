from subsystems.location.gps import GpsModule

class Regulator(object):
   def __init__(self):
      self.gps = GpsModule()
