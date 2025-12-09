class LoginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"

    def __init__(self, driver):
        self.driver=driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)