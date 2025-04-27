# SabelBok

<p align="center">
    <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgfx.nrk.no%2F8MyFeBD5CuJ1PscQHDBltgHoFTRKmzNFt4kEMTlpBH0g&f=1&nofb=1&ipt=f96cd518d42dbccd386ec3b4f691aaf003905d12e8e8a6e0ce444b0928124b3a" />
</p>

Kjedelig med utgående lisenser på bøker på unibok.no og må kjøpe igjen? Bruk SabelBok skriptet til å lagre dine bøker!

Datoen er 2023-08-29...

Imorgen går ut datoen på en skolebok jeg har kjøpt...

![Stress](https://media.giphy.com/media/Ta3v3I4GI1gH7Rqek6/giphy.gif) 

Jeg har eksamen om noen månder...

Jeg har to valg...

![Tenker](https://media.giphy.com/media/kPtv3UIPrv36cjxqLs/giphy.gif) 

1. Kjøp den samme boken som jeg har betalt for fire hundre lapper!
2. Piratkopiere boken for privatbruk!

Jeg skal faen meg ikke betale en dritt!

SabelBok!– en lett skript skrevet i python. 

## Hvordan funker det?

![Hacking](https://media.giphy.com/media/QdFeImLAY3jEs/giphy.gif) 

Vi bruker `selenium` til å logge oss in slik at vi har tilgang til nettsiden.

```python
username_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')
username_field.send_keys(username)
password_field.send_keys(password)
```

Etter å ha gått gjennom og sjekket ut hvordan ting fungerer, så la jeg merke til at innholdet til selve kapittelene er i en iframe-tag. Du kan lett teste dette ut ved å høyreklikke og trykke på frame content, der får du en `xhtml` med selve innholdet. Etter det, så fant jeg ut at den siste delene av linkene for en bok er selve sidetallene, så jeg lagret dette i en liste.

Vi bruker dermed `find_element` og `switch_to` til å fokusere oss på iframe-tagget der vi kan bruke `page_source` til å hente innholdet. Vi bruker således en for-løkken til å gå gjennom alle side tallene, her bruker vi `driver.get()` til å navigere oss gjennom alle kapittelene. Før det, så lagrer vi iframe innholdet i strukturerte `html` filer i en directory kalt `src/`.

```python
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
```

![Suksess!](https://media.giphy.com/media/92jYkH87yxV1C/giphy.gif) 

Da har du lagret hele boken! 

Du har lov til å piratkopiere til privatbruk! Men ikke del innholdet videre! Det er ulovelig dessverre! 

Likevel så er det ingen lover som nekter at jeg viser hvordan en kan gjøre det ☺️
