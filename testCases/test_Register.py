from pageObjects.RegisterPage import RegisterPage
from utilities.readConfig import ReadConfig

def test_register(setup):
    driver = setup
    driver.get(ReadConfig.getRegisterUrl())
    rp = RegisterPage(driver)   

    rp.firstname_input().send_keys(ReadConfig.getFirstname())
    rp.lastname_input().send_keys(ReadConfig.getLastname())
    rp.address_input().send_keys(ReadConfig.getAddress())
    rp.city_input().send_keys(ReadConfig.getCity())
    rp.state_input().send_keys(ReadConfig.getState())
    rp.zipcode_input().send_keys(ReadConfig.getZipcode())
    rp.phone_input().send_keys(ReadConfig.getPhone())
    rp.ssn_input().send_keys(ReadConfig.getSSN())
    rp.username_input().send_keys(ReadConfig.getUsername())
    rp.password_input().send_keys(ReadConfig.getPassword())
    rp.confirm_password_input().send_keys(ReadConfig.getPassword())

    rp.register_button().click()

    assert "dashboard" in setup.current_url
