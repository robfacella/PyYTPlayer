import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from random import shuffle
import os
import sys
def testSearch(driver):
    driver.get('http://www.google.com/');
    time.sleep(5) # Let the user actually see something!
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)
    driver.quit()
def createWebdriver():
    #Set path of Driver to the one in Local Dir
    gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
    #Generate a FirefoxProfile
    profile = FirefoxProfile()
    #for that profile Disable- Web Push Notifications
    profile.set_preference("permissions.default.desktop-notification", 1)
    #Create a driver with the above settings
    driver = Firefox(profile, executable_path=gecko+'.exe')
    #driver = Firefox(executable_path=gecko+'.exe', profile) #This had args backwards
    return (driver)
def getVideoDetails():
    print ("Now Playing: " + song + " (on Channel: "+ +")")
def playVideo(driver, url):
    try:
        driver.get(url)
        driver.find_element_by_id("movie_player").click() #No AutoPlay, smei-Auto workaround
        vidStatus = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
        while vidStatus != 0:
            #according to <https://developers.google.com/youtube/js_api_reference?csw=1> state == 0 is when a video has ended
            vidStatus = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
            time.sleep(1) #Wait a second and check again.
    except:
        print("Encountered an error trying to play from < ") 
        print (url + "> skipping item." )
        print ("")
        sys.stdout.flush()
def main():
    driver = createWebdriver()
    playlist = open(os.path.join('playlist.txt')).readlines()
    shuffle(playlist)
    for url in playlist:
        playVideo(driver, url)
    print ("End of Playlist. Goodbye.")
main()
#testSearch(driver)
