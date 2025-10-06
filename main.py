import time
import data
import helpers

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        # Checks if server URL is reachable
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
            cls.driver.get(data.URBAN_ROUTES_URL)
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running.")

    # Setting the Address (To & From Fields)
    def test_set_route(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

    # Selecting the Supportive Plan
    def test_select_plan(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.call_a_taxi()
        time.sleep(2)
        urban_routes_page.click_on_plan()
        time.sleep(2)
        urban_routes_page.find_active_selection()

    # Filling in the Phone Number
    def test_fill_phone_number(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.call_a_taxi()
        time.sleep(2)
        urban_routes_page.click_on_plan()
        time.sleep(2)
        urban_routes_page.click_on_phone_number_field()
        time.sleep(2)
        urban_routes_page.enter_phone_number_click_next(data.PHONE_NUMBER)
        time.sleep(2)
        sms_code = helpers.retrieve_phone_code(urban_routes_page.driver)
        time.sleep(2)
        urban_routes_page.click_on_code_label_enter_code_and_confirm(sms_code)
        time.sleep(2)

    # Adding a Credit Card
    def test_fill_card(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.call_a_taxi()
        time.sleep(2)
        urban_routes_page.click_on_plan()
        time.sleep(2)
        urban_routes_page.click_on_payment_field()
        time.sleep(2)
        urban_routes_page.click_on_add_card()
        time.sleep(2)
        urban_routes_page.complete_addition_of_card(data.CARD_NUMBER, data.CARD_CODE)
        time.sleep(5)
        urban_routes_page.click_on_x_button()
        time.sleep(2)
        urban_routes_page.check_payment_method()

    # Writing a Comment for the Driver
    def test_comment_for_driver(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.call_a_taxi()
        time.sleep(2)
        urban_routes_page.click_on_plan()
        time.sleep(2)
        urban_routes_page.click_on_comment_input()
        time.sleep(2)
        urban_routes_page.leave_comment_for_driver(data.MESSAGE_FOR_DRIVER)

    # Ordering a Blanket and Handkerchiefs
    def test_order_blanket_and_handkerchiefs(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.call_a_taxi()
        time.sleep(2)
        urban_routes_page.click_on_plan()
        time.sleep(2)
        urban_routes_page.add_blanket_and_handkerchief()

    # Ordering 2 Ice Creams (Supportive Taxi)
    def test_order_2_ice_creams(self):
        # Loop iterates twice
        # for i in range(2):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.call_a_taxi()
        time.sleep(2)
        urban_routes_page.click_on_plan()
        time.sleep(2)
        urban_routes_page.increment_icecream()
        time.sleep(2)
        urban_routes_page.retrieve_icecream_count()
        time.sleep(2)

    # Ordering a Taxi with the Supportive Tariff
    def test_car_search_model_appears(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.call_a_taxi()
        time.sleep(2)
        urban_routes_page.click_on_plan()
        time.sleep(2)
        urban_routes_page.click_on_phone_number_field()
        time.sleep(2)
        urban_routes_page.enter_phone_number_click_next(data.PHONE_NUMBER)
        time.sleep(2)
        sms_code = helpers.retrieve_phone_code(urban_routes_page.driver)
        time.sleep(2)
        urban_routes_page.click_on_code_label_enter_code_and_confirm(sms_code)
        time.sleep(2)
        urban_routes_page.click_on_comment_input()
        time.sleep(2)
        urban_routes_page.leave_comment_for_driver(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        urban_routes_page.click_on_order_button()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
