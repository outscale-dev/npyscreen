import osc_npyscreen
import curses

class ScansSlider(osc_npyscreen.Slider):
    def translate_value(self):
        return "{:2d}".format(int(self.value))

class TitleScansSlider(osc_npyscreen.TitleSlider):
    _entry_type = ScansSlider

#class ScanRunForm(osc_npyscreen.FormBaseNew):
#    DEFAULT_LINES = 12
#    DEFAULT_COLUMNS = 50
#    SHOW_ATX = 5
#    SHOW_ATY = 3
#
#    def create(self):
#        wLoc = self.add(osc_npyscreen.TitleText, name="Location:")
#        wPasses = self.add(ScansSlider, name="Scans:", out_of=10,
#                           lowest=1, step=1)



def sliderTest(screen):
    F = osc_npyscreen.Form()
    F.add(osc_npyscreen.TitleSlider, name="Slider 1")
    F.add(osc_npyscreen.TitleSlider, color='STANDOUT', name="Slider 2")
    F.add(osc_npyscreen.Slider, name="Slider 3")
    wPasses = F.add(TitleScansSlider, name="Scans:", out_of=10,
                               lowest=1, step=1)
    
    F.edit()



if __name__ == "__main__":
	curses.wrapper(sliderTest)