#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

myemail = "aaeeii16@yahoo.com"
myname = "Tester"
mysurname = "WSB_AD_AJ"
mystreet = "Zmyslona"
myhomenumber = "9999999999"
myzipcode = "00000"
myemailaddress = "aaeeii16@yahoo.com"
mypassword = "Abcdef"
mycity = "Wroclaw"
myphonenumber = "+48 123456789"
#from selenium.webdriver.support.ui import Select


class ZikoAptekaCheck(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.get("https://www.e-zikoapteka.pl/")

        def tearDownClass(self):
            self.driver.quit()

        # self.driver.implicitly_wait(10)
    #def test_wizzair(self):
        #driver = self.driver
        #driver.get("https://wizzair.com/pl-pl")
        #time.sleep(5)

        #enter = driver.find_element_by_name("q")
        #enter.send_keys("tester")
        #enter.submit()

    def test_login(self):
            #login_field = driver.find_element_by_xpath('//button[@data-test="navigation-menu-signin"])
            #login_field.click()
            #time.sleep(5)
        driver = self.driver
        #zaloguj_btn = WebDriverWait(driver, 20).until(
        #EC.element_to_be_clickable((By.CSS_SELECTOR, '//button[data-test="navigation-menu-signin"]')))
        #zaloguj_btn.click()

#zaloguj_btn = driver.find_element_by_css_selector('button[data-test="navigation-menu-signin"]')
        #zaloguj_btn.click()
        time.sleep(2)



        #nie dziala: button_rejestracja = driver.find_element_by_class('user-na-link.user-register')

        #xpath rejestracja /html/body/header/div[3]/div/div/div/aside[1]/a[2]
        button_rejestracja = driver.find_element_by_xpath("/html/body/header/div[3]/div/div/div/aside[1]/a[2]")
        button_rejestracja.click()
        time.sleep(1)

        email = driver.find_element_by_name("login")
        email.send_keys(myemail)
        time.sleep(1)

        haslo = driver.find_element_by_name("password")
        haslo.send_keys(mypassword)
        time.sleep(2)

        powtorz_haslo = driver.find_element_by_name("password_repeat")
        powtorz_haslo.send_keys(mypassword)
        time.sleep(2)

        imie = driver.find_element_by_name("firstname")
        imie.click()
        time.sleep(2)

        imie = driver.find_element_by_name("firstname")
        imie.send_keys(myname)
        time.sleep(2)

        nazwisko = driver.find_element_by_name("surname")
        nazwisko.send_keys(mysurname)
        time.sleep(2)

        ulica = driver.find_element_by_name("street")
        ulica.send_keys(mystreet)
        time.sleep(2)

        numer_domu = driver.find_element_by_name("street_nr")
        numer_domu.send_keys(myhomenumber)
        time.sleep(2)

        kod_pocztowy = driver.find_element_by_name("zip_code")
        kod_pocztowy.send_keys(myzipcode)
        time.sleep(2)

        miejscowosc = driver.find_element_by_name("city")
        miejscowosc.send_keys(mycity)
        time.sleep(2)

        telefon = driver.find_element_by_name("phone")
        telefon.send_keys(myphonenumber)
        time.sleep(2)

        button_newsletter = driver.find_element_by_name("agree[2]")
        button_newsletter.click()
        time.sleep(2)

        button_zatwierdz = driver.find_element_by_xpath('//*[@id="content"]/div/a[2]/span')
        #//*[@id="content"]/div/a[2]/span
        #button_zatwierdz = driver.find_element_by_class("check")
        button_zatwierdz.click()
        time.sleep(2)
"""

[ADAM] - tak wyglada obecnie rezultat testu po przejsciu wszyskich krokow:

        adam@adam-ubuntupython:~/selenium_tester/20200118 Z5/selenium$ python3 zikoapteka.py
test_login (__main__.ZikoAptekaCheck) ... ERROR

======================================================================
ERROR: test_login (__main__.ZikoAptekaCheck)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "zikoapteka.py", line 119, in test_login
    button_zatwierdz.click()
  File "/usr/local/lib/python3.8/dist-packages/selenium/webdriver/remote/webelement.py", line 80, in click
    self._execute(Command.CLICK_ELEMENT)
  File "/usr/local/lib/python3.8/dist-packages/selenium/webdriver/remote/webelement.py", line 633, in _execute
    return self._parent.execute(command, params)
  File "/usr/local/lib/python3.8/dist-packages/selenium/webdriver/remote/webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "/usr/local/lib/python3.8/dist-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element <span class="check">...</span> is not clickable at point (1267, 1144). Other element would receive the click: <div class="notice_bar" id="notice_bar" style="bottom: 0px;">...</div>
  (Session info: chrome=83.0.4103.61)


----------------------------------------------------------------------
Ran 1 test in 33.698s

FAILED (errors=1)
"""







        """
        AD: smietnik z poprzednich testow i z zajec, moze wykorzystam pozniej : )

        if plec == "M":


            m = driver.find_element_by_id("register-gender-male")
            imie.click()
            m.click()
            time.sleep(3)

        else:
            f = driver.find_element_by_id("register-gender-female")
            f.click()
            time.sleep(1)

        countrycode = driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]')
        countrycode.click()
        countrycode2 = WebDriverWait(self.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//li[@data-test="AX"]')))
        countrycode2.click()
        time.sleep(1)

        driver.find_element_by_name("phoneNumberValidDigits").send_keys(myphonenumber)
        #phonenumber = driver.find_element_by_xpath('//div[@data-test="check-in-step-contact-phone-number"]')
        #phonenumber.click()
        #phonenumber.send_keys(myphonenumber)
        time.sleep(2)

        email_address = driver.find_element_by_name("email")
        email_address.send_keys(myemail)
        #time.sleep(1)
        #<input type="email" name="email" data-test="booking-register-email" data-vv-validate-on="change" maxlength="256" placeholder="E-mail" autocomplete="on" class="rf-input__input pristine rf-input__input--empty touched" aria-required="true" aria-invalid="false">
        password = driver.find_element_by_name("password")
        password.send_keys(mypassword)
        #time.sleep(1)

        country = driver.find_element_by_name("country-select")
        country.click()
        #time.sleep(1)
        #country = WebDriverWait(self.driver, 15).until(
        #EC.element_to_be_clickable((By.XPATH, '//li[@data-test="AX"]')))
        #skopiowane od prowadzacego
        country_to_choose = driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']")
        countries = country_to_choose.find_elements_by_tag_name("label")
        for label in countries:
            option=label.find_element_by_tag_name('strong')
            # print(d.text)
            if option.get_attribute("innerText") == valid_country:
                option.location_once_scrolled_into_view
                option.click()
                break
        time.sleep(2)

        driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]').click()
        time.sleep(2)
        """

if __name__ == "__main__":
    #unittest.main()
    unittest.main(verbosity=2)
