import pyautogui
import time
from datetime import datetime

# Safety settings
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# Step 1: Open Chrome
print("Step 1: Opening Chrome browser...")

pyautogui.hotkey('win', 'r')
time.sleep(2)

pyautogui.write('chrome', interval=0.15)
pyautogui.press('enter')
time.sleep(5)

# Step 2: Navigate to Cricbuzz
print("Step 2: Opening Cricbuzz website...")

url = "https://www.cricbuzz.com/live-cricket-stream/147953/ban-vs-rsa-1st-test-bangladesh-tour-of-south-africa-2026"

pyautogui.hotkey('ctrl', 'l')
pyautogui.write(url, interval=0.02)
pyautogui.press('enter')

# Step 3: Wait for page loading
print("Step 3: Waiting for website...")
time.sleep(10)

# Step 4: Copy webpage data
print("Step 4: Copying webpage data...")

pyautogui.hotkey('ctrl', 'a')
time.sleep(1)

pyautogui.hotkey('ctrl', 'c')
time.sleep(2)

# Step 5: Open Notepad
print("Step 5: Opening Notepad...")

pyautogui.hotkey('win', 'r')
time.sleep(2)

pyautogui.write('notepad', interval=0.15)
pyautogui.press('enter')
time.sleep(3)

# Step 6: Paste webpage data
print("Step 6: Pasting data...")

pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# Step 7: Complete
print("deactivating the script...")