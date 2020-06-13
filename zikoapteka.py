#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

myemail = "abc@int.pl"
myname = "Tester"
mysurname = "WSB_AD_AJ"
mystreet = "Zmyslona"
myhomenumber = "9999999999"
myzipcode = "00000"
mypassword = "Abcdef"
mycity = "Wroclaw"
myphonenumber = "+48 123456789"


class ZikoAptekaCheck(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()

#KROK 1 -   WEJDZ NA STRONE https://www.e-zikoapteka.pl/

        self.driver.maximize_window()
        self.driver.get("https://www.e-zikoapteka.pl/")

        def tearDownClass(self):
            self.driver.quit()

    def test_login(self):
        driver = self.driver

#KROK 2 -   KLIKNIJ PRZYCISK REJESTRACJA

        button_rejestracja = driver.find_element_by_xpath("/html/body/header/div[3]/div/div/div/aside[1]/a[2]")
        button_rejestracja.click()
        #time.sleep(1)

#KROK 3 -   WPISZ ADRES E-MAIL

        email = driver.find_element_by_name("login")
        email.send_keys(myemail)
        #time.sleep(1)

#KROK 4 -   WPISZ HASLO

        haslo = driver.find_element_by_name("password")
        haslo.send_keys(mypassword)
        #time.sleep(1)

#KROK 5 -   WPISZ PONOWNIE HASLO W POLU POWTORZ HASLO

        powtorz_haslo = driver.find_element_by_name("password_repeat")
        powtorz_haslo.send_keys(mypassword)
        #time.sleep(1)

#KROK 6 -   WPISZ IMIE

        imie = driver.find_element_by_name("firstname")
        imie.click()
        time.sleep(1)

        imie = driver.find_element_by_name("firstname")
        imie.send_keys(myname)
        #time.sleep(1)

#KROK 7 -   WPISZ NAZWISKO

        nazwisko = driver.find_element_by_name("surname")
        nazwisko.send_keys(mysurname)
        #time.sleep(1)

#KROK 8 -   WPISZ NAZWE ULICY

        ulica = driver.find_element_by_name("street")
        ulica.send_keys(mystreet)
        #time.sleep(1)

#KROK 9 -   WPISZ NUMER DOMU

        numer_domu = driver.find_element_by_name("street_nr")
        numer_domu.send_keys(myhomenumber)
        #time.sleep(1)

#KROK 10 -   WPISZ KOD POCZTOWY

        kod_pocztowy = driver.find_element_by_name("zip_code")
        kod_pocztowy.send_keys(myzipcode)
        #time.sleep(1)

#KROK 11 -   WPISZ MIEJSCOWOSC

        miejscowosc = driver.find_element_by_name("city")
        miejscowosc.send_keys(mycity)
        #time.sleep(1)

#KROK 12 -   WPISZ NUMER TELEFONU

        telefon = driver.find_element_by_name("phone")
        telefon.send_keys(myphonenumber)
        #time.sleep(1)

#KROK 13 -   ZAZNACZ ZGODE NA PRZETWARZANIE DANYCH MARKETINGOWYCH

        button_newsletter = driver.find_element_by_name("agree[2]")
        button_newsletter.click()
        time.sleep(1)

#KROK 14 -   KLIKNIJ PRZYCISK ZATWIERDZ

        button_zatwierdz = driver.find_element_by_xpath('//*[@id="content"]/div/a[2]')
        button_zatwierdz.location_once_scrolled_into_view
        time.sleep(2)
        button_zatwierdz.click()
        time.sleep(3)

#KROK 16 -   SPRAWDZ CZY NA STRONIE POJAWILY SIE OSTRZEZENIA Z TEKSTEM "POLE WYMAGANE"

        error_text = driver.page_source
        text_found = re.search(r'Pole wymagane', error_text)
        self.assertNotEqual(text_found, None, "CHECKBOXY SA ZAZNACZONE")
        print("WYMAGANE CHECK BOXY NIE SA ZAZNACZONE")

if __name__ == "__main__":
    #unittest.main()
    unittest.main(verbosity=2)
