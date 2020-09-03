import time
from selenium import webdriver
from selenium.webdriver import Firefox
import os
import sys
#Does not autoplay first video by default, but after initial browser interaction (ie. clicking on the movie player) autoplay works on Chrome but not Firefox?
first = True
def testSearch(driver):
    driver.get('http://www.google.com/');
    time.sleep(5) # Let the user actually see something!
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)
    driver.quit()
def createWebdriver():
    #driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
    gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
    driver = Firefox(executable_path=gecko+'.exe')
    return (driver)
def playVideo(driver, url):
    try:
        driver.get(url)
        global first 
        if first == True:
            driver.find_element_by_id("movie_player").click() #Only needed on FIRST video, when using chrome. Firefox still click each video...
            first = False
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
    for url in playlist:
        playVideo(driver, url)
    print ("End of Playlist. Goodbye.")
main()
#testSearch(driver)
