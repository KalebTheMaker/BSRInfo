from colors import *
from bsrsun import BSRSun
import datetime

class Dashboards():
    def __init__(self):
        pass

    ###########################################################################
    # MAIN
    ###########################################################################
    class Main():
        def __init__(self, bi):
            self.bi = bi
            self.font = bi.pygame.font.Font("helvetica.ttf", 40)

        def show(self):
            self.bi.pygame.draw.line(self.bi.screen, white, (240, 0), (240, 235))
            
            # Titles
            # Input Title
            self.surface_input = self.font.render("INPUT", True, white)
            self.rect_input = self.surface_input.get_rect()
            self.rect_input.left = 0
            self.bi.screen.blit(self.surface_input, self.rect_input)

            # Output Title
            self.surface_output = self.font.render("OUTPUT", True, white)
            self.rect_output = self.surface_output.get_rect()
            self.rect_output.left = 243
            self.bi.screen.blit(self.surface_output, self.rect_output)

            # Metrics
            # Total Input
            self.input_metric = self.bi.Metric(self.bi, "", (20, 50), 0, 4000.99, "W", None, 50, False)
            self.output_metric = self.bi.Metric(self.bi, "", (260, 50), 0, 20000.99, "W", None, 50, False)

            self.bi.pygame.display.update()

        def update(self, d):
            self.input_metric.update(str(d['total_in']))
            self.output_metric.update(str(d['inv_total_load']))
            self.bi.pygame.display.update()
            pass

    ###########################################################################
    # SCROLLER
    ###########################################################################
    class Scroller():
        def __init__(self, bi):
            self.bi = bi
            self.scroller_top = 237
            self.scroller_left = 0
            self.scroller_width = 480
            self.scroller_height = 15
            self.font = bi.pygame.font.Font(None, 22)
            self.bsrsun = BSRSun()

        def show(self):
            self.clear()
            sr = self.bsrsun.getSunrise()
            ss = self.bsrsun.getSunset()
            alt = self.bsrsun.getAltitude()
            azi = self.bsrsun.getAzimuth()
            rads = self.bsrsun.getCSRadiation()
            self.txt = f"SR: {sr} | SS: {ss} | Sun Alt: {alt} | watts/m2: {rads}"
            self.surface = self.font.render(self.txt, True, amber)
            self.rect = self.surface.get_rect()
            self.rect.left = 0
            self.rect.top = 238
            self.bi.screen.blit(self.surface, self.rect)

        def clear(self):
            self.bi.pygame.draw.rect(self.bi.screen, black, self.bi.pygame.Rect(self.scroller_left, self.scroller_top, self.scroller_width, self.scroller_height))
            self.bi.pygame.display.flip()

        def update(self):
            # Update
            #self.clear()
            #self.rect.left = self.rect.left - 1
            #self.bi.screen.blit(self.surface, self.rect)
            pass

    ###########################################################################
    # MENU
    ###########################################################################
    class Menu():
        def __init__(self, bi):
            self.menu_btn_height = 60
            self.menu_btn_width = 60
            self.bi = bi
            self.voltage = None
            self.scroller_top = 255
            self.scroller_bottom = 235

        def show(self):            
            # Load button Image
            btn_img = self.bi.pygame.image.load("back.png").convert_alpha()
            bb = btn_img
            fb = self.bi.pygame.transform.rotate(btn_img, 180)
            mb = self.bi.pygame.transform.rotate(btn_img, 270)
            btn_top = self.bi.size[1] - self.menu_btn_height
            
            # Top 
            self.bi.pygame.draw.line(self.bi.screen, white, (0, self.scroller_top), (480, self.scroller_top))
            self.bi.pygame.draw.line(self.bi.screen, white, (0, self.scroller_bottom), (480, self.scroller_bottom))

            # Back Button
            self.bi.screen.blit(bb, (0, btn_top))

            # Forward Button
            fb_left = self.bi.size[0] - self.menu_btn_width
            self.bi.screen.blit(fb, (fb_left, btn_top))

            # Menu
            self.bi.screen.blit(mb, (self.menu_btn_width +10, btn_top)) 
            
            # Small Menu Data Items
            self.datetime = self.bi.Metric(self.bi, "", (135, btn_top), 00, 10000000000000000, "", None, 30, False)

            self.voltage = self.bi.Metric(self.bi, "DC@Inverter:", (140, (btn_top + 25)), 0.00, 60.99, "V", None, 25, False)
            
            self.chg_pv = self.bi.Metric(self.bi, "PV State:", (140, (btn_top+45)), 0, 100000, "", None, 25, False)
            self.chg_inv = self.bi.Metric(self.bi, "INV State:", (280, (btn_top+45)), 0, 100000, "", None, 25, False)           

            self.bi.pygame.display.update()

        def update(self, d):
            voltage = d['inv_dc_voltage']
            color = white
            # Create color break points for volgage
            if voltage >= 53.6:                     # Full Charge
                color = amber
            elif voltage <= 53.5 and voltage >= 52: # Nominal Charge
                color = green
            elif voltage <= 51.9 and voltage >= 51.2: # Getting Low
                color = yellow
            elif voltage <= 51.1:
                color = red

            self.voltage.update(str(voltage), color)

            now = datetime.datetime.now()
            dt = now.strftime("%I:%M:%S %m-%d-%Y")
            self.datetime.update(dt)

            self.chg_pv.update(str(d['mppt_charge_state']), amber)
            self.chg_inv.update(str(d['inv_state']), amber)

