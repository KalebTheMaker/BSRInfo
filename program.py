# Standard Python Modules
import time
import json
from urllib.request import urlopen
import urllib.error

# Custom Python Modules
from BSRInfo import bsrInfo
from dashboards import Dashboards
from lcddisplay import LCDDisplay
from infinitetimer import InfiniteTimer

# Setup global Variables
data_url = "http://jane.bsr.lan/power/data"
amber = (206, 145, 81)
white = (204, 204, 204)
green = (106, 153, 85)
red = (255, 0, 0)
dashboard = 'main'
data = None

# =================================================================================================
if __name__ == "__main__":
    # Setup ##################################################
    bi = bsrInfo()

    db = Dashboards()
    db_menu = db.Menu(bi)
    db_main = db.Main(bi)
    db_main.show()
    db_scroller = db.Scroller(bi)
    db_scroller.show()

    # Main Program ###########################################
    db_menu.show()
 
    def everySecond():
        #print("Tick")
        #data = json.loads("{}")
        global data
        try:
            response = urlopen(data_url)
            data = json.loads(response.read())
        except urllib.error.URLError as e:
            print("Got URLError!!")
            print(e)
            pass

        db_menu.update(data)
        db_main.update(data)

    def everyMinute():
        print("Tick: Minute")
        db_scroller.show()

    # def scrollCallback():
    #     print("Scroll Tick")
    #     db_scroller.update()

    # Data Timer
    s_timer = InfiniteTimer(1, everySecond)
    s_timer.start()

    # Minute Timer
    m_timer = InfiniteTimer(60, everyMinute)
    m_timer.start()

    # Scroller Timer
    # scroll_timer = InfiniteTimer(.25, scrollCallback)
    # scroll_timer.start()

    while True:
        for event in bi.pygame.event.get():
            print(event)
        pass

##############################################################################################33333
quit()




if dashboard == 'testdb':
    solarwatts = bi.Metric(bi, "Solar Watts:", (0,0), 0, 4000.99, "W", None, 30, True)
    genwatts = bi.Metric(bi, "Gen Watts:", (0,60), 0, 3000.99, "W", None, 30, True)
    totalload = bi.Metric(bi, "Total Load:", (0, 120), 0, 20000, "W",None, 30, True)

elif dashboard == 'main':
    bi.pygame.draw.line(bi.screen, white, (240, 0), (240, 255))

    lbl_in = bi.Metric(bi, "INPUT", (50, 0), 0, 10, "W", None, 60, False)
    lbl_out = bi.Metric(bi, "OUTPUT", (275, 0), 0, 10, "W", None, 60, False)
    in_watts = bi.Metric(bi, "", (0, 60), 0, 4000.99, "W", None, 60, False)
    out_watts = bi.Metric(bi, "", (250, 60), 0, 20000, "W", None, 60, False)

    pv_pwr = bi.Metric(bi, "PV:", (0, 166), 0, 4000.00, "W", None, 30, True)
    gs_pwr = bi.Metric(bi, "GEN:", (0, 210), 0, 2800.99, "W", None, 30, True)
    l1_pwr = bi.Metric(bi, "L1:", (250, 166), 0, 10000, "W", None, 30, True)
    l2_pwr = bi.Metric(bi, "L2:", (250, 210), 0, 10000, "W", None, 30, True)
    pass

while True:
    response = urlopen(data_url)
    data = json.loads(response.read())


    if dashboard == 'testdb':
        color = green
        if data['pv_power'] < data['inv_total_load']:
            color = red

        solarwatts.update(str(data['pv_power']))
        genwatts.update(str(data['genset_total_watts']))
        totalload.update(str(data['inv_total_load']), color)
    elif dashboard == 'main':
        # Change text color based on state
        color = green
        if data['inv_total_load'] > data['total_in']:
            color = red

        pv_pwr.update(str(data['pv_power']))
        gs_pwr.update(str(data['genset_total_watts']))
        l1_pwr.update(str(data['inv_l1_load']))
        l2_pwr.update(str(data['inv_l2_load']))

        in_watts.update(str(data['total_in']), color)
        out_watts.update(str(data['inv_total_load']), color)

        pass

    time.sleep(1)



