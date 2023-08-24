from seleniumbase import BaseCase
import time

if __name__ == "__main__":
    from pytest import main
    main([__file__, "--uc", "--incognito", "-s"])

class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://www.walmart.com/blocked")
        while True:
            self.click("div#px-captcha")

