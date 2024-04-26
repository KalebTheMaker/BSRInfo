from pysolar.solar import *
from astral import LocationInfo
from astral.sun import sun
from datetime import datetime, timezone
import pytz

class BSRSun():
    def __init__(self):
        self.lat = 39.361770
        self.lng = -123.281374
        self.loc = LocationInfo('BSR', 'Willits', 'America/Los_Angeles', self.lat, self.lng)

    def getAltitude(self):
        dt = datetime.now(timezone.utc).astimezone(pytz.timezone("US/Pacific"))
        return round(get_altitude(self.lat, self.lng, dt), 2)
    
    def getAzimuth(self):
        dt = datetime.now(timezone.utc).astimezone(pytz.timezone("US/Pacific"))
        return round(get_azimuth(self.lat, self.lng, dt), 2)
    
    def getCSRadiation(self):
        dt = datetime.now(timezone.utc).astimezone(pytz.timezone("US/Pacific"))
        altitude_deg = self.getAltitude()
        return round(radiation.get_radiation_direct(dt, altitude_deg), 2)
    
    def getObserverData(self, data):
        dt = datetime.now(timezone.utc).astimezone(pytz.timezone("US/Pacific"))
        s = sun(self.loc.observer, date=dt)
        return s[data].strftime('%I:%M:%S')
    
    def getSunrise(self):
        return self.getObserverData('sunrise')
    
    def getSunset(self):
        return self.getObserverData('sunset')


# TESTING BELOW

# bsrSun = BSRSun()

# print(f"Altitude: {bsrSun.getAltitude()}")
# print(f"Azimuth: {bsrSun.getAzimuth()}")
# print(f"Radiation: {bsrSun.getCSRadiation()}")
# print(f"Sunrise: {bsrSun.getSunrise()}")
# print(f"Sunset: {bsrSun.getSunset()}")

# quit()

# pst_dt = datetime.now(timezone.utc).astimezone(pytz.timezone("US/Pacific"))
# lat = 39.361770
# lng = -123.281374
# loc_info = LocationInfo('BSR', 'Willits', 'America/Los_Angeles', lat, lng)

# print(loc_info)
# sun_alt = get_altitude(lat, lng, pst_dt)
# sun_azm = get_azimuth(lat, lng, pst_dt)
# print(sun_alt)
# print(sun_azm)

# s = sun(loc_info.observer, date=pst_dt)
# sr = s['sunrise'].strftime('%I:%M:%S')
# ss = s['sunset'].strftime('%I:%M:%S')
# print(sr)
# print(ss)
# print(s)

# quit()



# bsr = LocationInfo('BSR', 'Willits', 'America/Los_Angeles', lat, lng)



# s = sun(bsr.observer, date=dt)
# print(s)


# print(get_altitude(lat, lng, dt))
# print(get_azimuth(lat, lng, dt))

# print(radiation.get_radiation_direct(dt, get_altitude(lat, lng, dt)))