
from PIL import ImageGrab
from pynput import mouse

from utils import Point

class SC:
    flag_capture = False
    point_start = Point(0, 0)
    point_end = Point(0, 0)


    def onClick(self, x, y, button, pressed):
        print(f"{x} {y} {button} {pressed}")
        if button == mouse.Button.left and not SC.flag_capture:
            SC.flag_capture = True
            SC.point_start.x, SC.point_start.y = x, y 

        elif button == mouse.Button.left and SC.flag_capture:
            SC.flag_capture = False
            SC.point_end.x, SC.point_end.y = x, y

        elif button == mouse.Button.right:
            SC.flag_capture = False
            SC.point_start.x, SC.point_start.y = 0, 0
            SC.point_end.x, SC.point_end.y = 0, 0

        return False


    def mouseListener(self):
        print(f"waiting for click, flag = {SC.flag_capture}")
        listener = mouse.Listener(on_click=self.onClick)
        listener.start()
        listener.join()


if __name__ == "__main__":
    print("starting program")

    sc = SC()
    
    while True:
        if sc.flag_capture == False and (sc.point_start.x != 0 or sc.point_end.x != 0):
            break
        sc.mouseListener()

    print(f"Captured: {sc.point_start.x}, {sc.point_start.y}, {sc.point_end.x}, {sc.point_end.y}")
    screenshot = ImageGrab.grab(bbox=(sc.point_start.x, sc.point_start.y, sc.point_end.x, sc.point_end.y))
    screenshot.save("screenshot.png")
    screenshot.close()
