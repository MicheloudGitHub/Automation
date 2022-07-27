class data:
    url='http://automationexercise.com'
    name='Michel'
    email="mail2ee170129@gmail.com"
    password="1234"

    home_header_id='header'
    signup_xpath="//a[text()=' Signup / Login']"
    email_box_signup_xpath="//input[contains(@data-qa, 'signup-email')]"
    email_box_login_xpath="//input[contains(@data-qa, 'login-email')]"
    name_box_xpath="//input[contains(@placeholder, 'Name')]"
    signup_btn_xpath="//button[contains(@data-qa, 'signup-button')]"
    new_user_signup_xpath="//*[contains(text(),'New User Signup!')]"

    mr_id="id_gender1"
    password_id="password"
    xpath_account_created="//*[contains(text(),'Account Created!')]"
    continue_btn="//*[contains(text(),'Continue')]"
    logged_in_as_xpath="//*[contains(text(),' Logged in as ')]"
    deleted_account_xpath="//*[contains(text(),' Delete Account')]"


    contact_us_xpath="//*[contains(text(),' Contact us')]"
    get_in_touch_xpath="//h2[contains(text()[1], 'Get In Touch')]"
    contact_us_name_box_xpath="//input[contains(@placeholder, 'Name')]"
    email_box_xpath="//input[contains(@data-qa, 'email')]"
