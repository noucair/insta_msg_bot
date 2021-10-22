from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions 
import time
import random
import instaloader
 
# Login Credentials
username ="" 
password =""
url = 'https://www.instagram.com/'

def getfollowers(username,password):
    bot = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(bot.context, username)
    bot.login(user=username,passwd=password)
    followers = [follower.username for follower in profile.get_followees()]
    return followers
def path():
    global chrome
    # starts a new chrome session 
    chrome = webdriver.Chrome() # Add path if required

def url_name(url): 
  chrome.get(url)
   
  # adjust sleep if you want
  time.sleep(1)

def login(username, your_password):
    time.sleep(2) 
    # finds the username box 
    usern = chrome.find_element_by_name("username")
    # sends the entered username 
    usern.send_keys(username)
    # finds the password box 
    passw = chrome.find_element_by_name("password")
    # sends the entered password 
    passw.send_keys(your_password)
     
    # press enter after sending password
    passw.send_keys(Keys.RETURN) 
    time.sleep(5)
     
    # Finding Not Now button
    notk = chrome.find_element_by_class_name("yWX7d")  
    notk.click()
    time.sleep(2)
def send_message():
   
    # Find message button
    #message = chrome.find_element_by_class_name("vBF20 _1OSdk")
    message = chrome.find_element_by_class_name('_862NM ')
    message.click()
    #chrome.find_element_by_class_name('HoLwm ').click()
    time.sleep(3)
    l = ["https://gaingame.me/PS5/","heeeey we gift you a playtation 5 simulation ,enjoooy","there is a gaveway coming sooon"]
    for elt in l:
        mbox = chrome.find_element_by_tag_name('textarea')
        mbox.send_keys(elt)
        mbox.send_keys(Keys.RETURN)
        time.sleep(2)

