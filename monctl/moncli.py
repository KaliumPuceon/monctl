from .g27q import G27Q
from argparse import ArgumentParser

class Moncli():

    def __init__(self):
        pass

    def readValues(self):
        with G27Q() as monitor:
            print("Reading outputs!")

    def read_values(self):
        with G27Q() as monitor:
            brightness=monitor.get_property("Brightness")
            contrast=monitor.get_property("Contrast")
            sharpness=monitor.get_property("Sharpness")
            bluelight=monitor.get_property("BlueLight")

        return (brightness, contrast, sharpness, bluelight)

    def set_monitorProperty(self, property: str, value: int):
        with G27Q() as monitor:
            monitor.set_property(property,value)

    def set_brightness(self, value):
        self.set_monitorProperty("Brightness", value)

    def set_contrast(self, value):
        self.set_monitorProperty("Contrast", value)

    def set_sharpness(self, value):
        self.set_monitorProperty("Sharpness", value)

    def set_blueLight(self, value):
        self.set_monitorProperty("BlueLight", value)

    def app(self, argv):

        parser = ArgumentParser(
            prog = 'moncli',
            description = 'Command line add-on to monctl by Gothem, a Gigabyte monitor control program',
            epilog = 'see https://github.com/KaliumPuceon/monctl for some more details especially if you want to try scripting with this'
            )
        parser.add_argument('-b','--brightness', type=int, help="brightness [1-100]")
        parser.add_argument('-c','--contrast', type=int, help="contrast [1-10]0")
        parser.add_argument('-s','--sharpness', type=int, help="sharpness [1-10]")
        parser.add_argument('-w','--bluelight', type=int, help="display warmth [1-10]")
        parser.add_argument('-r', '--relative', action="store_true", help="change value(s) relatively instead of absolutely")
        parser.add_argument('-p', '--print', action="store_true", help="print current values")
        args = parser.parse_args(argv)

        brightness = 0
        contrast = 0
        sharpness = 0
        bluelight = 0

        if args.relative:
            brightness, contrast, sharpness, bluelight, = self.read_values()

        if args.brightness:
            self.set_brightness(brightness+args.brightness)

        if args.contrast:
            self.set_contrast(contrast+args.contrast)

        if args.sharpness:
            self.set_sharpness(sharpness+args.sharpness)

        if args.bluelight:
            self.set_blueLight(bluelight+args.bluelight)

        if args.print:
            brightness, contrast, sharpness, bluelight, = self.read_values()
            print("brightness: %d" % (brightness))
            print("contrast: %d" % (contrast))
            print("sharpness: %d" % (sharpness))
            print("bluelight: %d" % (bluelight))


