# Walmart Captcha Solver

## Overview

This project demonstrates a clever solution to bypass the 'Robot or human' captcha on Walmart's website using SeleniumBase a robust automation framework. With SeleniumBase, you can automate web interactions while evading bot detection mechanisms.

## How It Works

The key to solving the Walmart captcha lies in SeleniumBase's capabilities. By utilizing this powerful framework, you can automate interactions with Walmart's website without being detected as a bot.

## Explanation

- 🤖🌐 We start by importing the `BaseCase` class from SeleniumBase for web automation.

- 🔵 We check if this script is being run as the main program using the `if __name__ == "__main__":` block.

- 📜 Inside the `if` block, we import the `main` function from pytest to run the script with specific pytest arguments like `--uc`, `--incognito`, and `-s` (--uc is used to enable undetected mode)

- 🧪 We create a test class named `RecorderTest` that inherits from `BaseCase`. This class will contain our test methods.

- 🌐 Inside the `RecorderTest` class, we define a test method called `test_recording`. This method is responsible for automating the Walmart website.

- ⏳ Within the `test_recording` method, we use `self.open("https://www.walmart.com/blocked")` to open the Walmart 'blocked' page.

- 🔄 We then create an infinite loop using `while True:`.

- 🖱️ Inside the loop, we use `self.click("div#px-captcha")` to continuously click on the 'div#px-captcha' element.

This code essentially opens the Walmart 'blocked' page and continuously clicks on the specified captcha element, designed to bypass Walmart's captcha protection as discussed earlier. The script will keep running until manually interrupted. 🚀


![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHducnZoNHBpZjV0ZjNsc2FxbjJibnFjYmhjOWszaW0wZm9mMzV3NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7un4GZSOR6SAAKg8rB/giphy.gif)



## Credits

- SeleniumBase: [https://github.com/seleniumbase/SeleniumBase](https://github.com/seleniumbase/SeleniumBase)

## Author

- [NFT404]
