from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from lib2to3.pgen2 import driver
from selenium import webdriver

web = webdriver.Chrome()
web.get('https://www.juegos.com/juego/teclas-de-piano-magicas')

time.sleep(5)

Cookies = web.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
Cookies.click()

time.sleep(5)

click(500,470)

time.sleep(40)

click(500,500)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(366,666)[0] == 0:
        click(366,666)
    if pyautogui.pixel(460,666)[0] == 0:
        click(460,666)
    if pyautogui.pixel(540,666)[0] == 0:
        click(540,666)
    if pyautogui.pixel(625,666)[0] == 0:
        click(625,666)
    