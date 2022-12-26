from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import random
# import winsound

# ssl._create_default_https_context = ssl._create_unverified_context

filename = "camx_2022-extracted.csv"
headers = "Firmenname, Website, Adresse, Land, Phone/Fax, Kategorien, Beschreibung, \n"
loopfile = "camx_dir_urls.txt"

# Wartepausen
waittimefrom_main, waittimeto_main = 12, 15  # Vorgabe der Wartezeit zwischen ... Sekunden und ... Sekunden
waittimefrom_card, waittimeto_card = 10, 12  # Vorgabe der Wartezeit zwischen ... Sekunden und ... Sekunden

# PROFILEINSTELLUNGEN BEGINN
# loc_adblock = 'uBlock0_1.45.3rc5.firefox.signed.xpi'  # Ad-block file path
opts = Options()
opts.set_preference("javascript.enabled", True)  # Javascript deaktivieren
opts.set_preference("permissions.default.image", 2,)
opts.set_preference("plugin.state.flash", 0)  # Flash deaktivieren
opts.set_preference("toolkit.telemetry.unified", False)  # Telemetrie deaktivieren
opts.page_load_strategy = 'normal'  # 'eager': DOM ready, but not yet images
# opts.add_argument("-headless")  # option for headless browser
# PROFILEINSTELLUNGEN ENDE
driver_card = webdriver.Firefox(options=opts)  # Fenster für Adress-Karte
driver_card.maximize_window()

f = open(filename, "a", encoding="utf-8")  # "w" fuer "write", a fuer append
f.write(headers)

with open(loopfile, encoding='utf-8', errors='replace') as linkfile:
    for page_nr, page in enumerate(linkfile):
        driver_main = webdriver.Firefox(options=opts)  # Fenster für Verzeichnis (Hauptfenster)
        driver_main.maximize_window()
        print('\nÖffne Verzeichnisseite', page)
        driver_main.get(page)  # Hauptfenster

        # Scrolling system
        height_first = driver_main.execute_script("return document.body.scrollHeight")  # Höhe der Seite in Pixel
        driver_main.execute_script("window.scrollBy(0, 1200)")
        time.sleep(1)
        driver_main.execute_script("window.scrollBy(0, 1200)")
        time.sleep(1)
        height_second = driver_main.execute_script("return document.body.scrollHeight")  # Höhe der Seite in Pixel
        while height_second > height_first:
            height_first = height_second
            driver_main.execute_script("window.scrollBy(0, 1200)")
            time.sleep(1)
            driver_main.execute_script("window.scrollBy(0, 1200)")
            time.sleep(1)
            height_second = driver_main.execute_script("return document.body.scrollHeight")
            time.sleep(1)

        # Kontaktkarte-container
        container = driver_main.find_elements(by=By.XPATH, value="//h3[contains(text(),card-Title)]/child::a")
        url_extr_list = []
        for i in container:
            lnk = i.get_attribute("href")
            url_extr_list.append(lnk)

        # Kontaktkarten extrahieren
        for idx, card_url in enumerate(url_extr_list):

            print("iteration: ", idx + 1, "of", len(url_extr_list), "on page", page_nr+1, "of 27")

            print("Öffne Kontaktkarte:", card_url )
            driver_card.get(card_url)
            time.sleep(random.randint(waittimefrom_card, waittimeto_card))
            try:
                firmenname = driver_card.find_element(by=By.XPATH, value="//h1").text
                firmenname = f'"{firmenname}"'
            except Exception as e:
                print("Ausnahme: Firmenname")
                print(e)
                firmenname = ""
                pass
            # Adresse
            try:
                addr = driver_card.find_element(by=By.XPATH, value='//p[contains(text(), showcase-address)][*]').text
                splitted = addr.split("\n")
                country = splitted[-1]
                country = f'"{country}"'
                address = splitted[:-1]
                address = address[0]
                address = f'"{address}"'
            except Exception as e:
                print("Ausnahme: Adresse")
                print(e)
                address = ""
                pass
            try:
                contact = driver_card.find_element(by=By.CLASS_NAME, value='showcase-web-phone')
                cont_extr = contact.find_elements(by=By.TAG_NAME, value="li")
                website = cont_extr[0].text
                cont_extr.pop(0)

                phone_fax = []
                for item in cont_extr:
                    phone_fax.append(item.text)
                phone_fax = "\n".join(phone_fax)
                phone_fax = f'"{phone_fax}"'
            except Exception as e:
                print("Ausnahme: Kontakt")
                print(e)
                website, phone_fax = "", ""
                pass
            try:
                categories_tmp = driver_card.find_element(by=By.ID, value='js-vue-products')
                categories = categories_tmp.find_elements(by=By.XPATH, value="*")[-1].text
                categories = f'"{categories}"'
            except Exception as e:
                print("Ausnahme: Kategorie")
                print(e)
                categories = ""
                pass
            try:
                description=driver_card.find_element(by=By.ID, value='js-vue-description').text
                description=description.split("\n")[-1]
                description = f'"{description}"'
            except Exception as e:
                print("Ausnahme: Beschreibung")
                print(e)
                description = ""
                pass

            f.write(firmenname + "," + website + "," + address + "," + country + "," + phone_fax + "," + categories +"," + description + "\n")

        driver_main.close()

        time.sleep(random.randint(waittimefrom_main, waittimeto_main))

print("Finished")

# winsound.Beep(1000, 2000)  # Piepen wenn es beendet ist.
f.close()
driver_card.close()
# os.system("shutdown -s -t 10")  # Computer herunterfahren, letzte Zahl ist Timer
