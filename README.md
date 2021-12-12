# project_kivy_screenshot_experiment
sandbox program that uses pyautogui to make screenshots.

instructions: hold "shift + 1" to define the first corner, then "shift + 2" to define the second. 
This program will save a screengrab of the rectangle formed by the two in "images/" directory local to this project.

notes
1: only works on your primary monitor, due to limitations of pyautogui.
2: saves the image as "new_image_1.png", or if present then the next largest that is not.
