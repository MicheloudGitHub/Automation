from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from variables import data as dt
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class functions:

        def __init__(self, driver):
            self.driver=driver
        
        def waitForClickeable(driver, by, element, timeout=30):
            WebDriverWait(driver, timeout=timeout).until(expected_conditions.element_to_be_clickable((by,element)))
        
        def waitForVisibility(driver, by, element, timeout=30):
            WebDriverWait(driver, timeout=timeout).until(expected_conditions.visibility_of_element_located((by,element)))
        
        def login(self, driver):
            #Click on 'Signup / Login' button
            loginbtn=self.driver.find_element(By.XPATH, dt.signup_xpath)
            loginbtn.click()
            #Verify 'New User Signup!' is visible
            self.driver.find_element(By.XPATH, dt.new_user_signup_xpath)
            #Enter name and email address
            btn_name=self.driver.find_element(By.XPATH, dt.name_box_xpath)
            btn_name.click()
            btn_name.send_keys(dt.name)
            btn_email=self.driver.find_element(By.XPATH, dt.email_box_signup_xpath)
            btn_email.click()
            btn_email.send_keys(dt.email)
            #Click 'Signup' button
            btn_signup=self.driver.find_element(By.XPATH, dt.signup_btn_xpath)
            btn_signup.click()
        
        def fillDetails(self, driver):
            #title
            self.driver.find_element(By.ID, dt.mr_id).click()
            #pass
            password=self.driver.find_element(By.ID, dt.password_id)
            password.click()
            password.send_keys(dt.password)
            #date of birth
            select_element = driver.find_element(By.ID, "days")
            select_object = Select(select_element)
            select_object.select_by_visible_text('15')

            select_element = driver.find_element(By.ID, "months")
            select_object = Select(select_element)
            select_object.select_by_visible_text('June')

            select_element = driver.find_element(By.ID, "years")
            select_object = Select(select_element)
            select_object.select_by_visible_text('1993')

            self.driver.find_element(By.ID, "newsletter").click()
            self.driver.find_element(By.ID, "optin").click()

            self.driver.find_element(By.ID, "first_name").send_keys("Michel")
            self.driver.find_element(By.ID, "last_name").send_keys("Micheloud")
            self.driver.find_element(By.ID, "company").send_keys("EY")
            self.driver.find_element(By.ID, "address1").send_keys("Street 6")

            select_element = driver.find_element(By.ID, "country")
            select_object = Select(select_element)
            select_object.select_by_visible_text('Israel')

            self.driver.find_element(By.ID, "state").send_keys("AA")
            self.driver.find_element(By.ID, "city").send_keys("AA")
            self.driver.find_element(By.ID, "zipcode").send_keys("0000")
            self.driver.find_element(By.ID, "mobile_number").send_keys("111111")
            #Click 'Create Account button'
            self.driver.find_element(By.XPATH, "//*[contains(text(),'Create Account')]").click()