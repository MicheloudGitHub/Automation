from pytest import mark, param, fixture
from variables import data as dt
from functions import functions as fc
from selenium.webdriver.common.by import By
import xmlrunner
import unittest

class regression_Tests:

    @fixture
    def driver(self, setup):
        driver = setup
        driver.get(dt.url)
        driver.maximize_window()
        fc.waitForVisibility(driver,By.ID,dt.home_header_id)
        yield driver
        driver.close()

    @mark.regression
    @mark.parametrize("test_number,scenario",
                    [param('1',"Register User", marks = mark.register),
                     param('2',"Login User with correct email and password", marks = mark.login),        
                     param('6',"Contact Us Form", marks = mark.contact),
                     param('20',"Search Products and Verify Cart After Login", marks = mark.search),                   
                    ])

    def test_regression(self, test_number, scenario, driver):
        print("\nThe next test is the number: "+ test_number)
        print("The scenario for this test is: "+ scenario)  
        self.lp=fc(driver)

        #Test 1 Register User
        if (scenario.casefold().__contains__('register user')):
            #3. Verify that home page is visible successfully
            fc.waitForVisibility(driver,By.ID,dt.home_header_id)
            self.lp.login(driver)
            #8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
            fc.waitForVisibility(driver,By.ID,dt.home_header_id)
            #9. Fill details: Title, Name, Email, Password, Date of birth
            self.lp.fillDetails(driver)
            #14. Verify that 'ACCOUNT CREATED!' is visible
            fc.waitForVisibility(driver,By.XPATH,dt.xpath_account_created)
            #15. Click 'Continue' button
            self.lp.driver.find_element(By.XPATH, dt.continue_btn).click()
            #16. Verify that 'Logged in as username' is visible
            fc.waitForVisibility(driver,By.XPATH,dt.logged_in_as_xpath)
            #17. Click 'Delete Account' button
            self.lp.driver.find_element(By.XPATH, dt.deleted_account_xpath).click()
            fc.waitForVisibility(driver,By.XPATH,"//*[contains(text(),' Delete Account')]")
            #18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
            self.lp.driver.find_element(By.XPATH, "//form[contains(@data-method, 'DELETE')]").click() #Bug
            #No permite continuar 
        
        #Test 2
        if (scenario.casefold().__contains__('login user with correct email and password')):
            #3. Verify that home page is visible successfully
            fc.waitForVisibility(driver,By.ID,dt.home_header_id)
            #4. Click on 'Signup / Login' button
            loginbtn=self.lp.driver.find_element(By.XPATH, dt.signup_xpath)
            loginbtn.click()
            #5. Verify 'Login to your account' is visible
            self.lp.driver.find_element(By.XPATH, "//*[contains(text(),'Login to your account')]")
            #6. Enter correct email address and password
            btn_email=self.lp.driver.find_element(By.XPATH, "//input[contains(@data-qa, 'login-email')]")
            btn_email.click()
            btn_email.send_keys(dt.email)

            password=self.lp.driver.find_element(By.XPATH, "//input[contains(@data-qa, 'login-password')]")
            password.click()
            password.send_keys(dt.password)

            login_btn=self.lp.driver.find_element(By.XPATH, "//button[contains(@data-qa, 'login-button')]")
            login_btn.click()
            #Verify that 'Logged in as username' is visible
            fc.waitForVisibility(driver,By.XPATH,dt.logged_in_as_xpath)
            #Click 'Delete Account' button
            self.lp.driver.find_element(By.XPATH, dt.deleted_account_xpath).click()
            fc.waitForVisibility(driver,By.XPATH,"//*[contains(text(),' Delete Account')]")
            #Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
            self.lp.driver.find_element(By.XPATH, "//form[contains(@data-method, 'DELETE')]").click() #Bug
            #No permite continuar 

        #Test #6
        if (scenario.casefold().__contains__('contact us form')):
            #3. Verify that home page is visible successfully
            fc.waitForVisibility(driver,By.ID,dt.home_header_id)
            #4. Click on 'Contact Us' button
            self.lp.driver.find_element_by_xpath(dt.contact_us_xpath).click()
            #5. Verify 'GET IN TOUCH' is visible
            fc.waitForVisibility(driver,By.XPATH,dt.get_in_touch_xpath)
            #6. Enter name, email, subject and message
            btn_name=self.lp.driver.find_element(By.XPATH, dt.name_box_xpath)
            btn_name.click()
            btn_name.send_keys(dt.name)
            btn_email=self.lp.driver.find_element(By.XPATH, dt.email_box_xpath)
            btn_email.click()
            btn_email.send_keys(dt.email)

            self.lp.driver.find_element(By.XPATH, "//input[contains(@data-qa, 'subject')]").send_keys("This is the subject")
            self.lp.driver.find_element(By.XPATH, "//textarea[contains(@data-qa, 'message')]").send_keys("This is the message")
            #7. Upload file
            TxtfileLocation = "C:/Users/WK582CS/Desktop/challenge_arbusta/Files/Test.txt"
            self.lp.driver.find_element(By.XPATH, "//input[contains(@name, 'upload_file')]").click() #Bug
            self.lp.driver.find_element_by_xpath("//input[@class='file-selector-input']").send_keys(TxtfileLocation)
            self.lp.driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
            self.lp.driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()

        #Test 20
        if (scenario.casefold().__contains__('search products and verify cart after login')):
            #Verify that home page is visible successfully
            fc.waitForVisibility(driver,By.ID,dt.home_header_id)
            self.lp.driver.find_element(By.XPATH, "//i[contains(@class, 'material-icons card_travel')]").click()
            self.lp.driver.find_element(By.ID, "search_product").send_keys("Pure Cotton V-Neck T-Shirt")
            self.lp.driver.find_element(By.ID, "submit_search").click()
            fc.waitForVisibility(driver,By.XPATH,"//h2[contains(text(),'Searched Products')]")
            #self.lp.driver.find_element(By.ID, "28").click()
            self.lp.driver.find_element(By.XPATH, "//i[contains(@class, 'fa fa-plus-square')]").click()
            self.lp.driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-default cart')]").click()
            fc.waitForVisibility(driver,By.XPATH,"//*[contains(text(),'View Cart')]")
            self.lp.driver.find_element(By.XPATH, "//*[contains(text(),'View Cart')]").click()
            #Click on 'Signup / Login' button
            loginbtn=self.lp.driver.find_element(By.XPATH, dt.signup_xpath)
            loginbtn.click()
            #5. Verify 'Login to your account' is visible
            self.lp.driver.find_element(By.XPATH, "//*[contains(text(),'Login to your account')]")
            #6. Enter correct email address and password
            btn_email=self.lp.driver.find_element(By.XPATH, "//input[contains(@data-qa, 'login-email')]")
            btn_email.click()
            btn_email.send_keys(dt.email)

            password=self.lp.driver.find_element(By.XPATH, "//input[contains(@data-qa, 'login-password')]")
            password.click()
            password.send_keys(dt.password)

            login_btn=self.lp.driver.find_element(By.XPATH, "//button[contains(@data-qa, 'login-button')]")
            login_btn.click()

            self.lp.driver.find_element(By.XPATH, "//*[contains(text(),' Cart')]").click()
            last_check=self.lp.driver.find_element(By.XPATH, "//*[contains(text(),'Pure Cotton V-Neck T-Shirt')]").text
            print(last_check)

            if (last_check=="Pure Cotton V-Neck T-Shirt"):
                assert True
            else: 
                print("Doesn't match")
                assert False

if __name__=='__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='C:/Users/WK582CS/Desktop/challenge_arbusta/Results')) #change the path