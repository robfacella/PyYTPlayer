import time
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import shuffle
import os
import sys


def createWebdriver():
    #Set path of Driver to the one in Local Dir, or the symLink to it
    #gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
    #service = ( gecko+'.exe' )
    #Generate a FirefoxProfile (deprecated)
    #opts = Options()
    # Think I was using the push notifications disabler for Win10 at the time
    #for that profile Disable- Web Push Notifications
    #opts.set_preference("permissions.default.desktop-notification", 1)
    #Hopefully incorporate uBlock
    absolutePathHack = os.environ['PWD'] #Not ideal, but she WORKS!
    ublockfile = os.path.normpath(os.path.join(absolutePathHack, 'uBlock0@raymondhill.net'))
    #Create a driver with the above settings
    try:
        driver = webdriver.Firefox()
    except Exception as error:
                print ("An exception occurred: ", error)
                print ("[*] Exiting..")
                sys.exit(1)
    try:
        #Try to add local ublock.xpi to the browser; don't crash if that fails though.
        driver.install_addon(ublockfile+'.xpi', temporary=True)
    except Exception as error:
        print ("An exception occurred: ", error)
        print ("Could not install uBlock Origin. Is uBlock0@raymondhill.net.xpi in the same folder as the script? ")
        print ("Try running the script from the directory it is located in, used a PWD hack for the Required AbsolutePath for AddonInstallation.")
        print ("Will function anyway, but do you REALLY want to do this without an AdBlocker?")
    return (driver)
def sanitizeTextFromHTML(htmlToPrint):
    f = open(os.devnull, 'w') #for writing garbage print-check text to null
    htmlText = htmlToPrint.text
    output = ""
    for chara in htmlText:
        try:
            f.write(chara) #Makes sure character is printable, but writes to <null> as so not to make a mess of the CLI
            output = output + chara
        except:
            #Replace char which couldn't be encoded (ie unicode error) with the string <?>
            #Prevents interpreter crash trying to print.
            output = output + "<?>"
    f.close()
    #print (output)
    #sys.stdout.flush()
    return (output)
def getVideoDetails(driver):
    try:
        wait = WebDriverWait(driver, 10)
        song = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"yt-formatted-string.ytd-watch-metadata:nth-child(1)")))
    except Exception as error:
        print ("An exception occurred: ", error)
        song = "ERROR"
    try:
        wait = WebDriverWait(driver, 10)
        chan = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"ytd-channel-name.ytd-video-owner-renderer > div:nth-child(1) > div:nth-child(1) > yt-formatted-string:nth-child(1) > a:nth-child(1)")))
    except Exception as error:
        print ("An exception occurred: ", error)
        chan = "ERROR"
    print ( "Now Playing: " + sanitizeTextFromHTML(song) )
    print ( "on Channel:  " + sanitizeTextFromHTML(chan) )
    sys.stdout.flush()
    print ("")
def playVideo(driver, url):
    try:
        driver.get(url)
        time.sleep(3)
        try:
          mov = driver.find_element("id","movie_player")
          mov.click() #No AutoPlay, smei-Auto workaround
          time.sleep(2)
        except Exception as error:
          print ("An exception occurred: ", error)
        try:
            #Not sure why but this added try/except block seemed to improve the success rate of the nested statements?, makes no sense but SURE why not.
            getVideoDetails(driver)
        except Exception as error:
            print ("An exception occurred: ", error)
            print ("Call to 'getVideoDetails(driver)' failed.")
            sys.stdout.flush()
        vidStatus = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
        while vidStatus != 0:
            #according to <https://developers.google.com/youtube/js_api_reference?csw=1> state == 0 is when a video has ended
            vidStatus = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
            time.sleep(1) #Wait a second and check again.
    except Exception as error:
        print ("An exception occurred: ", error)
        print("Encountered an error trying to play from < ")
        print (url + "> skipping item." )
        print ("")
        sys.stdout.flush()

def getPlaylist():
        playlistFile = open(os.path.join('playlist.txt'))
        playlist = playlistFile.readlines()
        playlistFile.close()
        shuffle(playlist)
        return(playlist)
def main():
    driver = createWebdriver()
    playlist = getPlaylist()
    for url in playlist:
        playVideo(driver, url)
    print ("End of Playlist. Goodbye.")
main()
