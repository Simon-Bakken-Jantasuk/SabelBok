from selenium import webdriveFerdig med side num. r
from selenium.webdriver.common.by import By
from time import sleep

WAIT = sleep(3) # sekunder
LOGIN_URL = 'https://utdanning.cappelendamm.no/login/normal' # kan endres

book = input('Bok URL: ')
username = input('Brukernavn: ')
password = input('Passord: ')

driver = webdriver.Chrome()
driver.implicitly_wait(10) # nettleseren kan bruke litt
driver.get(login_url)

WAIT

username_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')
username_field.send_keys(username)
password_field.send_keys(password)

WAIT

submit_field = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_field.click()

driver.get(book)

WAIT

feide_nei = driver.find_element(By.CLASS_NAME,'login-publisher')
feide_nei.click()

WAIT

cappelendamm = driver.find_element(By.ID, 'cdogginnButton')
cappelendamm.click()

WAIT

driver.get(book + '/1')

sleep(20)

page_numbers = [3, 4, 5, 6, 26, 80, 110, 142, 172, 208, 246, 292, 334, 370, 373] # fant jeg ut ved å telle manuelt fra siste del av lenken

for i in range(len(page_numbers)):
    iframe = driver.find_element(By.TAG_NAME, 'iframe')

    WAIT

    driver.switch_to.frame(iframe)

    WAIT

    iframe_content = driver.page_source

    WAIT

    with open(f"src/{i}.html", "w", encoding="utf-8") as file: 
        file.write(iframe_content)
        print(f"Ferdig med side num. {i}.")

    WAIT

    driver.get(book + f"/{page_numbers[i]}")
    print('Går til neste side...')
    sleep(20)

driver.quit()
print("Ferdig")

if "ma"