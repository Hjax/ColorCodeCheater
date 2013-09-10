import ctypes
import time
import win32gui

def get_pixel_colour(i_x, i_y):
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

def click(i_x, i_y):
    ctypes._reset_cache()
    ctypes.windll.user32.SetCursorPos(i_x, i_y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
    
#values for reading colors and clicking the number buttons
colors = {"Black":(38, 38, 38), "Brown":(166, 128, 100), "Red":(255, 0, 0), "Orange":(255, 153, 0), "Yellow":(255, 255, 0), "Green":(102, 153, 0), "Blue":(0, 0, 255), "Violet":(102, 51, 255)}
bandValues = {"Black":0, "Brown":1, "Red":2, "Orange":3, "Yellow":4, "Green":5, "Blue":6, "Violet":7}
buttons = {1:(670, 580), 2:(780, 580), 3:(890, 580), 4:(670, 640), 5:(780, 640), 6:(890, 640), 7:(670, 700), 8:(780, 700), 9:(890, 700), 0:(780, 750)}

#values for reading variance and clicking the variance buttons
varianceColors = {"Gold":(254, 224, 122), "Silver":(182, 182, 182)}
varianceButtons = {"Gold":(740, 490), "Silver":(860, 490)}

def firstTwo():
    first = get_pixel_colour(623, 353)
    for i in colors:
        if colors[i] == first:
            correctButton = buttons[bandValues[i]]
            click(correctButton[0], correctButton[1])
    second = get_pixel_colour(726, 353)
    for i in colors:
        if colors[i] == second:
            correctButton = buttons[bandValues[i]]
            click(correctButton[0], correctButton[1])
    
def Multiplier():
    third = get_pixel_colour(826, 353)
    for i in colors:
        if colors[i] == third:
            for i in range (0, bandValues[i]):
                click(buttons[0][0], buttons[0][1])

def Variance():
    forth = get_pixel_colour(931, 353)
    for i in varianceColors:
        if varianceColors[i] == forth:
            correctButton = varianceButtons[i]
            click(correctButton[0], correctButton[1])

time.sleep(5)
while True:
    firstTwo()
    Multiplier()
    Variance()
    time.sleep(.1)
    
