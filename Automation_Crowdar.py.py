# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 23:58:54 2021

@author: michel.micheloud
"""
#! Python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_options)

    
class TestCrowdar(unittest.TestCase):
    
    def test_1(self): #Test 1: Verificar que aparece el siguiente warning: "Epic sadface: Password is required" al ingresar user sin password.
        driver.get('https://www.saucedemo.com/')
        time.sleep(5)
        username_box = driver.find_element_by_id("user-name")
        time.sleep(5)    
        username_box.click()
        time.sleep(5)
        username_box.send_keys("standard_user")
        time.sleep(5)
        login_button = driver.find_element_by_id("login-button")
        time.sleep(5)
        login_button.click()
        time.sleep(5)
        message_list1 = []
        right_message = driver.find_elements_by_xpath("//*[@id='login_button_container']/div/form/div[3]/h3")
        warning = ['Epic sadface: Password is required']
        for i in right_message:
            message_list1.append(i.text)
        print(message_list1)
        print(warning)
        self.assertEqual(message_list1, warning)
        
        time.sleep(5)
        
    def test_2(self): #Test 2: Verificar que aparece el siguiente warning:"Epic sadface: Username is required" al ingresar Password sin User".
        driver.get('https://www.saucedemo.com/')
        time.sleep(5)   
        password_box = driver.find_element_by_id("password")
        password_box.click()
        password_box.send_keys("secret_sauce")
        password_box.click()
        login_button = driver.find_element_by_id("login-button")
        time.sleep(5)
        login_button.click()
        time.sleep(5)
        message_list2 = []
        right_message = driver.find_elements_by_xpath("//*[@id='login_button_container']/div/form/div[3]/h3")
        warning = ['Epic sadface: Username is required']
        for i in right_message:
            message_list2.append(i.text)
        print(message_list2)
        print(warning)
        self.assertEqual(message_list2, warning)
        time.sleep(5)
       
    def test_3(self): #Test 3: Verificar que aparece el siguiente warning: "Epic sadface: Username and password do not match any user in this service"
        driver.get('https://www.saucedemo.com/')
        time.sleep(5)
        username_box = driver.find_element_by_id("user-name")
        time.sleep(5)    
        username_box.click()
        time.sleep(5)
        username_box.send_keys("ANY USER")
        time.sleep(5)
        password_box = driver.find_element_by_id("password")
        password_box.click()
        password_box.send_keys("ANY PASSWORD")
        login_button = driver.find_element_by_id("login-button")
        time.sleep(5)
        login_button.click()
        time.sleep(5)
        message_list = []
        right_message = driver.find_elements_by_xpath("//*[@id='login_button_container']/div/form/div[3]/h3")
        warning = ['Epic sadface: Username and password do not match any user in this service']
        for i in right_message:
            message_list.append(i.text)
        print(message_list)
        print(warning)
        self.assertEqual(message_list, warning)
        time.sleep(5)
        
    def test_4(self): #Test 4: Verificar el correcto ingreso con user: standard_user y password: secret_sauce.
        driver.get('https://www.saucedemo.com/')
        time.sleep(5)
        username_box = driver.find_element_by_id("user-name")
        time.sleep(5)    
        username_box.click()
        time.sleep(5)
        username_box.send_keys("standard_user")
        time.sleep(5)   
        password_box = driver.find_element_by_id("password")
        password_box.click()
        password_box.send_keys("secret_sauce")
        time.sleep(5)
        login_button = driver.find_element_by_id("login-button")
        time.sleep(5)
        login_button.click()        
        time.sleep(5)

        
    def test_5(self): #Test 5: Validar que al utilizar User: "locked_out_user" y password correcto (secret_sauce) aparece el siguiente mensaje "this user has been locked".
        driver.get('https://www.saucedemo.com/')
        time.sleep(5)
        username_box = driver.find_element_by_id("user-name")
        time.sleep(5)    
        username_box.click()
        time.sleep(5)
        username_box.send_keys("locked_out_user")
        time.sleep(5)
        password_box = driver.find_element_by_id("password")
        password_box.click()
        password_box.send_keys("secret_sauce")
        password_box.click()
        login_button = driver.find_element_by_id("login-button")
        time.sleep(5)
        login_button.click()
        time.sleep(5)
        message_list = []
        right_message = driver.find_elements_by_xpath("//*[@id='login_button_container']/div/form/div[3]/h3")
        warning = ['Epic sadface: Sorry, this user has been locked out.']
        for i in right_message:
            message_list.append(i.text)
        print(message_list)
        print(warning)
        self.assertEqual(message_list, warning)
        time.sleep(5)
        
    def test_6(self): #Test 6: Validar que "user: problem_user" es correcto y es posible logearse. 
        driver.get('https://www.saucedemo.com/')
        time.sleep(5)
        username_box = driver.find_element_by_id("user-name")
        time.sleep(5)    
        username_box.click()
        time.sleep(5)
        username_box.send_keys("problem_user")
        time.sleep(5)   
        password_box = driver.find_element_by_id("password")
        password_box.click()
        password_box.send_keys("secret_sauce")
        time.sleep(5)
        login_button = driver.find_element_by_id("login-button")
        time.sleep(5)
        login_button.click()        
        time.sleep(5)

    
    def test_7(self): #Test 7: Validar que "user: performance_glitch_user" es correcto y es posible logearse.
        driver.get('https://www.saucedemo.com/')
        time.sleep(5)
        username_box = driver.find_element_by_id("user-name")
        time.sleep(5)    
        username_box.click()
        time.sleep(5)
        username_box.send_keys("performance_glitch_user")
        time.sleep(5)   
        password_box = driver.find_element_by_id("password")
        password_box.click()
        password_box.send_keys("secret_sauce")
        time.sleep(5)
        login_button = driver.find_element_by_id("login-button")
        time.sleep(5)
        login_button.click()        
        time.sleep(5)
        
    def test_8(self): #Test 8: Validar que luego de ingresar el usuario y contraseña correcto se puede usar la tecla "enter" en vez de hacer click en boton de login.
        driver.get('https://www.saucedemo.com/')
        time.sleep(5)
        username_box = driver.find_element_by_id("user-name")
        time.sleep(5)    
        username_box.click()
        time.sleep(5)
        username_box.send_keys("standard_user")
        time.sleep(5)   
        password_box = driver.find_element_by_id("password")
        password_box.click()
        password_box.send_keys("secret_sauce")
        password_box.click()
        password_box.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.quit()
                       
if __name__=='__main__':
    unittest.main() 

