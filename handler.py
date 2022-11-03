import time
import pyautogui
pyautogui.FAILSAFE=True
print("Handler!")
time.sleep(2)
date=input("What is the date?")
time.sleep(1)
subject=input("What subject are you in?")
time.sleep(1)
title=input("What shall your title be today?")
if (title=="undefined"):
   namefile = {
            subject+date+".txt"
            }
   f = open(str(namefile),"a")
   f.close()
   time.sleep(1)
   pyautogui.keyDown("ctrl")
   pyautogui.keyDown("alt")
   pyautogui.press("t")
   pyautogui.keyUp("ctrl")
   pyautogui.keyUp("alt")
   pyautogui.typewrite("xed "+namefile)
   #pyautogui.press("enter")

else:
   filename=(title+"-"+subject+"-"+date+".txt")
   f = open(filename,"a")
   f.close()
   time.sleep(1)
   pyautogui.keyDown("ctrl")
   pyautogui.keyDown("alt")
   pyautogui.press("t")
   pyautogui.keyUp("ctrl")
   pyautogui.keyUp("alt")
   pyautogui.typewrite("xed "+filename)
   #pyautogui.press("enter")

