from unittest import TestCase, main
import sys
import os
# hacky fix to get parent directory
sys.path.append(os.getcwd() + '/..')

#import our file that has user login and the path to the tor and chrome drivers
from secretDirectory import secret
from post import post
from FacebookChatPhisher import loginToFacebook, getDriver, Browser

class Test(TestCase):
    def test_post(self):
        email=secret.EMAIL
        passw=secret.passw
        uname = secret.UNAME
        tor_path=secret.torBrowserPath
        driver_path=secret.exePath
        driver = getDriver(driver_path, Browser.TOR, tor_path)
        loginToFacebook(driver, email, passw)
        friendURL="https://www.facebookcorewwwi.onion/profile.php?id=100064037088173"
        message='''Hello Abdullah Arif,

We are an international research firm looking for research participants. We've recognized you as a prime candidate to participate in one of our research studies in the fields of:

1. Musician/Band
2. Video Game
3. Community

It will only take a few moments! As a thank you for participating in our research we will be providing you with a $25 Starbucks gift card upon completion and verification.

If you would like to participate please click the participation button below.

https://steve-pham.github.io/UserClicks/'''
        post(driver, friendURL, message)


if __name__ == '__main__':
    main()