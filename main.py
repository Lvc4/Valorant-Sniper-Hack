# importing all necessary packages
import cv2
import numpy as np
import pyautogui
import keyboard
from pynput.mouse import Controller as Controller
from pynput.mouse import Button
import time

# start of the actual script
if __name__ == '__main__':
    print('Starting...')

    # setting up a view parameters
    mouse = Controller()
    enabled = False

    # start a while loop in order to loop infinitely and as fast as possible
    while True:
        # get the image at the position 955, 535 with 10 by 10 pixels
        # put in the half_of_your_screen_size - 8 instaed of 952 and 532
        img = pyautogui.screenshot(region=(952, 532, 16, 16))
        # convert it to an array and calculate the sum of all values
        img = np.array(img)
        frame = np.array(img).sum()

        # if you press f you activate the bot or deactivate if it is already running and take the first value
        if keyboard.is_pressed('f'):
            print('Predicting...')
            frame1 = np.array(img).sum()
            if enabled == True:
                enabled = False
                print('Disables')
            else:
                enabled = True
                print('enabled')
            time.sleep(0.1)
            

        # checks if the bot is active
        if enabled == True:
            # if the picture value is different the bot will shoot and deactivate itself
            if frame1 > (frame+2000) or frame1 < (frame-2000):
                mouse.press(Button.left)
                time.sleep(0.2)
                mouse.release(Button.left)
                enabled = False
                print('Shot')

            # if the picture value is not changing too much -> update it
            if frame1 > (frame+50) or frame1 < (frame-50): # cs:go 100, Valorant 50
                frame1 = np.array(img).sum()
