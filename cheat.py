import win32gui, win32api, win32con, time, colorsys
from win32api import GetSystemMetrics
import ImageGrab

## TODO  HANDLE WHEN TWO STRIPES ARE THE SAME COLOR
##       MAKE METHOD FOR FINDING KEYS


def get_pixel_colour(i_x, i_y):
        return image.getpixel((i_x, i_y))
def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def get_stripe(level):
        current_stripe = {}
        for i in range (level, level+GetSystemMetrics(1)):
                pixelColor = get_pixel_colour(i, level)
                try:
                        if current_stripe[-1] != pixelColor:
                                current_stripe[i] = pixelColor
                except:
                        current_stripe[i] = pixelColor
        return current_stripe
                
def get_number_of_stripes():
        return GetSystemMetrics(1)

def get_buttons(stripe):
        first_column = stripe[stripe.keys()[0]]
        print first_column
def stripe_scanner(stripe):
        colorCode = {}
        if backgroundColor in stripe.values():
                counter = 0
                for i in stripe.values():
                        for j in colors:
                                if colors[j] == i:
                                        colorCode[j] = stripe.keys()[counter]
                        counter += 1
        if len(colorCode) > 1:
                print colorCode
        if len(colorCode) == 4:
                return colorCode
        else:
                return 0
        
#values for reading colors and clicking the number buttons
colors = {"Black":(38, 38, 38), "Brown":(166, 128, 100), "Red":(255, 0, 0), "Orange":(255, 153, 0), "Yellow":(255, 255, 0), "Green":(102, 153, 0), "Blue":(0, 0, 255), "Violet":(102, 51, 255), "Gold":(254, 224, 122), "Silver":(182, 182, 182)}
bandValues = {"Black":0, "Brown":1, "Red":2, "Orange":3, "Yellow":4, "Green":5, "Blue":6, "Violet":7}
buttons = {1:(670, 580), 2:(780, 580), 3:(890, 580), 4:(670, 640), 5:(780, 640), 6:(890, 640), 7:(670, 700), 8:(780, 700), 9:(890, 700), 0:(780, 750)}
backgroundColor = (152, 186, 186)

#values for reading variance and clicking the variance buttons
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
image = ImageGrab.grab()
while True:

#        firstTwo()
#        Multiplier()
#        Variance()
        for i in range (0, get_number_of_stripes()):
                stripe = stripe_scanner(get_stripe(i))
                if stripe == 0:
                        pass
                else:
                        get_buttons(stripe)
                
