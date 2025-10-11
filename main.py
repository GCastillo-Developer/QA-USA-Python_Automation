import data
import helpers

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
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

        urban_routes_page.enter_from_location(data.ADDRESS_FROM)

        from_address = urban_routes_page.get_from_location()

        assert from_address == data.ADDRESS_FROM, f"Expected '{data.ADDRESS_FROM}', but got '{from_address}'"

        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        to_address = urban_routes_page.get_to_location()

        assert to_address == data.ADDRESS_TO, f"Expected '{data.ADDRESS_TO}', but got '{to_address}'"

    # Selecting the Supportive Plan
    def test_select_plan(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.call_a_taxi()

        urban_routes_page.click_on_plan()

        correct_plan = urban_routes_page.find_active_selection()

        assert data.SUPPORTIVE_PLAN in correct_plan, f"Expected '{data.SUPPORTIVE_PLAN}', but got '{correct_plan}'"

    # Filling in the Phone Number
    def test_fill_phone_number(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.call_a_taxi()

        urban_routes_page.click_on_plan()

        urban_routes_page.click_on_phone_number_field()

        urban_routes_page.click_on_secondary_phone_number_field()

        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)

        urban_routes_page.click_next_button()

        sms_code = helpers.retrieve_phone_code(urban_routes_page.driver)

        urban_routes_page.enter_code_and_confirm(sms_code)

        phone_field = urban_routes_page.retrieve_phone_number()

        assert phone_field == data.PHONE_NUMBER, f"Expected '{data.PHONE_NUMBER}', but got '{phone_field}'"

    # Adding a Credit Card
    def test_fill_card(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.call_a_taxi()

        urban_routes_page.click_on_plan()

        urban_routes_page.click_on_payment_method()

        urban_routes_page.click_on_add_card()

        urban_routes_page.complete_addition_of_card(data.CARD_NUMBER, data.CARD_CODE)

        urban_routes_page.click_on_x_button()

        payment_method_text = urban_routes_page.check_payment_method()

        assert data.PAYMENT_METHOD_TEXT == payment_method_text, f"Expected '{data.PAYMENT_METHOD_TEXT}', but got '{payment_method_text}'"

    # Writing a Comment for the Driver
    def test_comment_for_driver(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.call_a_taxi()

        urban_routes_page.click_on_plan()

        urban_routes_page.click_on_comment_input()

        urban_routes_page.fill_comment_input(data.MESSAGE_FOR_DRIVER)

        comment_text = urban_routes_page.retrieve_comment_input()

        assert data.MESSAGE_FOR_DRIVER == comment_text, f"Expected '{data.MESSAGE_FOR_DRIVER}', but got '{comment_text}'"

    # Ordering a Blanket and Handkerchiefs
    def test_order_blanket_and_handkerchiefs(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.call_a_taxi()

        urban_routes_page.click_on_plan()

        urban_routes_page.click_on_blanket_and_handkerchief()

        selection_confirmed = urban_routes_page.return_toggle_switch()

        # Verify that the selection is confirmed using the correct assertion.
        assert selection_confirmed is True, f"Slider is not checked: {selection_confirmed}"

    # Ordering 2 Ice Creams (Supportive Taxi)
    def test_order_2_ice_creams(self):
        # Loop iterates twice
        # for i in range(2):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.call_a_taxi()

        urban_routes_page.click_on_plan()

        urban_routes_page.increment_icecream()

        # Retrieve ice cream count
        icecream_count = urban_routes_page.retrieve_icecream_count()

        # Assert that the displayed count matches 2.
        assert icecream_count == "2", f"Expected 2 ice creams, but got {icecream_count}"

    # Ordering a Taxi with the Supportive Tariff
    def test_car_search_model_appears(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.call_a_taxi()

        urban_routes_page.click_on_plan()

        urban_routes_page.enter_phone_number_click_next(data.PHONE_NUMBER)

        sms_code = helpers.retrieve_phone_code(urban_routes_page.driver)

        urban_routes_page.enter_code_and_confirm(sms_code)

        urban_routes_page.leave_comment_for_driver(data.MESSAGE_FOR_DRIVER)

        urban_routes_page.click_on_order_button()

        car_modal = urban_routes_page.car_search_modal_displayed()

        assert car_modal is True, f"Expected car modal to be True, but got {car_modal}"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
