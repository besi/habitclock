import machine
import neopixel
import time
#import raingaugedisplay

pixelCount = 60
np = neopixel.NeoPixel(machine.Pin(12), pixelCount)


def clear():
    np.fill((0, 0, 0))
    np.write()


def white():
    np.fill((255, 255, 255))
    np.write()


def seconds(seconds = 60):
    for i in range(seconds%60):
        np.fill((0,0,0))
        np[i] = (255,255,255)
        np.write()
        time.sleep(1)
        

def rainbow():
    # Rainbow code by https://wokwi.com/arduino/projects/305569065545499202

    rainbow = [
      (126 , 1 , 0),(114 , 13 , 0),(102 , 25 , 0),(90 , 37 , 0),(78 , 49 , 0),(66 , 61 , 0),(54 , 73 , 0),(42 , 85 , 0),
      (30 , 97 , 0),(18 , 109 , 0),(6 , 121 , 0),(0 , 122 , 5),(0 , 110 , 17),(0 , 98 , 29),(0 , 86 , 41),(0 , 74 , 53),
      (0 , 62 , 65),(0 , 50 , 77),(0 , 38 , 89),(0 , 26 , 101),(0 , 14 , 113),(0 , 2 , 125),(9 , 0 , 118),(21 , 0 , 106),
      (33 , 0 , 94),(45 , 0 , 82),(57 , 0 , 70),(69 , 0 , 58),(81 , 0 , 46),(93 , 0 , 34),(105 , 0 , 22),(117 , 0 , 10),
      (126 , 1 , 0),(114 , 13 , 0),(102 , 25 , 0),(90 , 37 , 0),(78 , 49 , 0),(66 , 61 , 0),(54 , 73 , 0),(42 , 85 , 0),
      (30 , 97 , 0),(18 , 109 , 0),(6 , 121 , 0),(0 , 122 , 5),(0 , 110 , 17),(0 , 98 , 29),(0 , 86 , 41),(0 , 74 , 53),
      (0 , 62 , 65),(0 , 50 , 77),(0 , 38 , 89),(0 , 26 , 101),(0 , 14 , 113),(0 , 2 , 125),(9 , 0 , 118),(21 , 0 , 106),
      (33 , 0 , 94),(45 , 0 , 82),(57 , 0 , 70),(69 , 0 , 58),(81 , 0 , 46),(93 , 0 , 34),(105 , 0 , 22),(117 , 0 , 10)]

    while True:
        rainbow = rainbow[-1:] + rainbow[:-1]
        for i in range(pixelCount):
            np[i] = rainbow[i]
            np.write()

        #time.sleep_ms(5)

white()
seconds(15)
time.sleep(2)
rainbow()

