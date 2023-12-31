from PIL import ImageGrab, Image
import time
import pytesseract
import psutil
import subprocess

# Constants
TASK_NAME = "DarkSoulsRemastered.exe"
DEATH_LABEL_REGION = (580, 480, 1330, 650)  # (left, top, right, bottom) !!!! ASSUMES 1920:1080

# Functions
def isRedPixel(pixel):
    return pixel[0] >= pixel[1]+20 and pixel[0] >= pixel[2]+20

def readDeathCount():
    try:
    # Attempt to open the file for reading
        with open('counter.txt', 'r') as file:
            # Read and process the file contents
            return file.read() 
    except FileNotFoundError:
        # Handle the case when the file does not exist
        # Open a file for writing (creates a new file or overwrites an existing file)
        with open('counter.txt', 'w') as file:
            # Write data to the file if needed
            file.write('0')
            return 0
def getTextFromScreenshot(screenshot):
    processed = Image.new('RGB', screenshot.size)
    # Iterate through each pixel in the original image
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            pixel_color = screenshot.getpixel((x, y))
            # Check if the pixel color is within the red range
            if isRedPixel(pixel_color):
                # If it's within the range, set the pixel color to black
                processed.putpixel((x, y), (0, 0, 0))
            else:
                # If it's not within the range, set the pixel color to white
                processed.putpixel((x, y), (255, 255, 255))
    return pytesseract.image_to_string(processed,config=r'--psm 6')
def incrementDeathCount(death_count):
    death_count = int(death_count) + 1
    print(f"Death detected! Total deaths: {death_count}")
    # Open a file for writing (creates a new file if it doesn't exist or overwrites an existing file)
    with open('counter.txt', 'w') as file:
        # Write text to the file
        file.write(str(death_count))
    return death_count

# Variables
death_count = readDeathCount()
print(f"Current death count is: {death_count}")

running_game = subprocess.Popen(TASK_NAME,cwd='./')
pid = running_game.pid

while psutil.pid_exists(pid):
    # Capture a screenshot in the middle of the screen
    try:
        screenshot = ImageGrab.grab(bbox=DEATH_LABEL_REGION)
    except OSError:
        print("Couldn't grab screen. Trying again after 5 seconds...")
        time.sleep(5)
        continue
    text = getTextFromScreenshot(screenshot)
    # Check if the "YOU DIED" message is detected
    if "YOU DIED" in text:
        death_count = incrementDeathCount(death_count)
        time.sleep(8)
    # Repeat every second
    time.sleep(1)

