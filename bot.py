from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from chat_api import what_beats, words

driver = webdriver.Chrome()
driver.get("https://www.whatbeatsrock.com/")

assert driver.title == "What Beats Rock Game"

def play():
    ps = driver.find_elements(By.TAG_NAME, "p")
    it = ps[1].text[:-1]
    words.append(it)
    print("What beats " + it + "?")
    beater = what_beats(it)
    
    field = driver.find_element(by=By.TAG_NAME, value="input")
    field.clear()

    field.click()
    time.sleep(0.5)

    field.send_keys(beater + Keys.RETURN)

    try:
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='next']"))
        )
        print("Nice one with " + beater + "!")
        next_button.click()
        time.sleep(1)
        play()  # Recursive call
    except Exception:
        print("Failed at (infos)")
        time.sleep(1000)
        exit()


if __name__ == "__main__":
    play()
