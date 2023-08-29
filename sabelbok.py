from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

book = '' # Legg til bok URL
login_url = 'https://utdanning.cappelendamm.no/login/normal' # Login URL
username = '' # Brukernavn for å login
password = '' # Passord for å login

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(login_url)

sleep(3)

username_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')
username_field.send_keys(username)
password_field.send_keys(password)

sleep(3)

submit_field = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_field.click()

driver.get(book)

sleep(3)

feide_nei = driver.find_element(By.CLASS_NAME,'login-publisher')
feide_nei.click()

sleep(3)

cappelendamm = driver.find_element(By.ID, 'cdogginnButton')
cappelendamm.click()

sleep(3)

driver.get(book + '/1')

sleep(20)

page_numbers = [3, 4, 5, 6, 26, 80, 110, 142, 172, 208, 246, 292, 334, 370, 373]

for i in range(len(page_numbers)):
    iframe = driver.find_element(By.TAG_NAME, 'iframe')

    sleep(3)

    driver.switch_to.frame(iframe)

    sleep(3)

    iframe_content = driver.page_source

    sleep(3)

    with open(f"src/{i}.html", "w", encoding="utf-8") as file: 
        file.write(iframe_content)
        print(f"Finished page {i}.")

    sleep(3)
    driver.get(book + f"/{page_numbers[i]}")
    print('Going to next page.')
    sleep(20)

driver.quit()
print("Done!")
