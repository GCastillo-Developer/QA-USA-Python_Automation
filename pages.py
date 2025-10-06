import time
import logging
from selenium.webdriver.common.by import By


class UrbanRoutesPage:
    # Setting Address Locators
    FROM_ADDRESS_LOCATOR = (By.ID, 'from')
    TO_ADDRESS_LOCATOR = (By.ID, 'to')

    # Selecting Supportive Plan Locators
    CALL_A_TAXI_LOCATOR = (By.XPATH, '// button[text() = "Call a taxi"]')
    SUPPORTIVE_PLAN_ACTION_LOCATOR = (By.XPATH,
                                      '// div[ @class = "tcard-icon"] // img[@ src="/static/media/kids.27f92282.svg"]')
    TCARD_ACTIVE_LOCATOR = (By.CSS_SELECTOR, "div.tcard.active div.tcard-title")

    # Filling in the Phone Number Field Locators
    PHONE_NUMBER_FIELD_LOCATOR = (By.XPATH, '//div[@class = "np-button"]')
    PHONE_NUMBER_POP_UP_LABEL_LOCATOR = (By.XPATH, '//div[@class = "input-container"]//label[@for = "phone"]')
    PHONE_NUMBER_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input#phone.input')
    CLICK_NEXT_BUTTON_LOCATOR = (By.XPATH, '//div[@class = "buttons"]//button[text() = "Next"]')
    CODE_LABEL_FIELD_LOCATOR = (By.XPATH, '//div[@class = "input-container"]//label[@for = "code"]')
    CODE_INPUT_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input#code.input')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//div[@class = "buttons"]//button[text() = "Confirm"]')

    # Adding a Credit Card locators
    PAYMENT_METHOD_FIELD_LOCATOR = (By.XPATH, '//div[@class = "pp-button filled"]')
    CLICK_ON_ADD_CARD_LOCATOR = (By.XPATH, '//div[contains(text(), "Add card")]')
    CLICK_ON_CARD_NUMBER_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input#number.card-input')
    CLICK_ON_CARD_CODE_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input#code.card-input')
    CLICK_ON_ADD_CARD_TEXT_LOCATOR = (By.XPATH, '//div[text() = "Adding a card"]')
    CHECK_IF_LINK_BUTTON_IS_DISABLED_AND_CLICK_LOCATOR = (By.XPATH, '//button[@type = "submit" and text() = "Link"]')
    CLICK_ON_X_BUTTON = (By.XPATH,
                         '//div[@class = "section active"]//div[@class = "head" and text() = "Payment method"]')
    GET_PAYMENT_METHOD_TEXT = (By.XPATH, '//div[@class = "pp-value-text"]')

    # Writing a comment to the driver locators
    CLICK_ON_COMMENT_LABEL_LOCATOR = (By.XPATH, '//label[@for = "comment"]')
    CLICK_ON_COMMENT_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input#comment.input')

    # Ordering a blanket and handkerchiefs locators
    CLICK_ON_ADD_BLANKET_AND_HANDKERCHIEFS_SLIDER_LOCATOR = (By.CSS_SELECTOR, 'div.r-sw-container .slider.round')
    VERIFY_TOGGLE_SWITCH_LOCATOR = (By.CSS_SELECTOR, 'input[type="checkbox"].switch-input')

    # Ordering two ice creams(supportive taxi) locators
    SCROLL_TO_ICECREAM_BUCKET_LOCATOR = (By.XPATH, '//div[@class = "r-group-title"]')
    INCREMENTING_ICECREAM_COUNT_LOCATOR = (By.XPATH, '//div[@class = "counter-plus"]')
    RETRIEVE_ICECREAM_COUNTER_VALUE_LOCATOR = (By.XPATH, '//div[@class = "counter-value"]')

    # Car search model locators
    CLICK_ON_THE_ORDER_BUTTON = (By.CLASS_NAME, 'smart-button')
    VERIFY_CAR_SEARCH_MODAL = (By.CLASS_NAME, "order-progress")

    ########################################################################################################################
    # This method initializes the driver

    # initializes the driver
    def __init__(self, driver):
        self.driver = driver

    ########################################################################################################################
    # Ensure that users can correctly set pickup and destination addresses and that they are properly recorded.

    # Sends keys to from address locator and asserts value in input box
    def enter_from_location(self, from_address):
        self.driver.find_element(*self.FROM_ADDRESS_LOCATOR).send_keys(from_address)
        from_value = self.driver.find_element(*self.FROM_ADDRESS_LOCATOR).get_attribute("value")

        assert from_address == from_value, f"Expected '{from_address}', but got '{from_value}'"

    # Sends to keys to address locator and asserts value in input field
    def enter_to_location(self, to_address):
        self.driver.find_element(*self.TO_ADDRESS_LOCATOR).send_keys(to_address)
        to_value = self.driver.find_element(*self.TO_ADDRESS_LOCATOR).get_attribute("value")

        assert to_address == to_value, f"Expected '{to_address}', but got '{to_value}'"

    ########################################################################################################################
    # Ensure users can choose the Supportive plan and validate their selection without hardcoding values.

    # Clicks call a taxi button
    def call_a_taxi(self):
        self.driver.find_element(*self.CALL_A_TAXI_LOCATOR).click()

    # Clicks supportive plan option
    def click_on_plan(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN_ACTION_LOCATOR).click()

    # Finds the active tcard selection and asserts expected selection
    def find_active_selection(self):
        active_selection = self.driver.find_element(*self.TCARD_ACTIVE_LOCATOR).text
        expected_selection = "Supportive"

        assert expected_selection in active_selection, f"Expected '{expected_selection}', but got '{active_selection}'"

    #######################################################################################################################
    # Ensure that users can enter their phone number, receive a confirmation SMS code, and validate their login.

    # click on the phone number field
    def click_on_phone_number_field(self):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD_LOCATOR).click()

    # Clicks on the pop-up phone number field
    def click_on_secondary_phone_number_field(self):
        self.driver.find_element(*self.PHONE_NUMBER_POP_UP_LABEL_LOCATOR).click()

    # Enters phone number on pop-up field and asserts value in input field
    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_INPUT_LOCATOR).send_keys(phone_number)
        user_phone_number_field = self.driver.find_element(*self.PHONE_NUMBER_INPUT_LOCATOR).get_attribute("value")

        assert phone_number == user_phone_number_field, f"Expected '{phone_number}', but got '{user_phone_number_field}'"

    # Clicks the next button on pop-up phone number field
    def click_next_button(self):
        self.driver.find_element(*self.CLICK_NEXT_BUTTON_LOCATOR).click()

    # Clicks on the pop-up code label field
    def click_on_code_label(self):
        self.driver.find_element(*self.CODE_LABEL_FIELD_LOCATOR).click()

    # Sends the code to the input field
    def enter_code(self, code):
        self.driver.find_element(*self.CODE_INPUT_FIELD_LOCATOR).send_keys(code)

    # Clicks the confirm button
    def confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    ########################################################################################################################
    # Here is where combine methods are

    # Combine methods for the from and to address
    def enter_locations(self, from_address, to_address):
        self.enter_from_location(from_address)
        self.enter_to_location(to_address)

    # Combines methods to enter sms code and confirm
    def click_on_code_label_enter_code_and_confirm(self, code):
        self.click_on_code_label()
        time.sleep(2)
        self.enter_code(code)
        time.sleep(2)
        self.confirm_button()

    # Combines method to enter phone number and click next button
    def enter_phone_number_click_next(self, phone_number):
        self.click_on_secondary_phone_number_field()
        time.sleep(2)
        self.enter_phone_number(phone_number)
        time.sleep(2)
        self.click_next_button()

    # Enters card information
    def enter_card_information(self, card_number, card_code):
        self.enter_card_number(card_number)
        time.sleep(2)
        self.enter_card_code(card_code)
        time.sleep(2)

    # Completes addition of a card
    def complete_addition_of_card(self, card_number, card_code):
        self.enter_card_information(card_number, card_code)
        self.click_on_payment_method_text()
        self.verify_link_clickable()
        self.click_link_button()

    # Leaves a comment for the driver
    def leave_comment_for_driver(self, comment_text):
        self.click_on_comment_input()
        self.fill_comment_input(comment_text)

    ###########################################################################################################################

    # Verify that users can add a valid credit card and that the "Link" button becomes clickable only after a valid input.

    # Click on Payment Method
    def click_on_payment_field(self):
        self.driver.find_element(*self.PAYMENT_METHOD_FIELD_LOCATOR).click()

    # Click on Add Card
    def click_on_add_card(self):
        self.driver.find_element(*self.CLICK_ON_ADD_CARD_LOCATOR).click()

    # Enter a valid Card Number.
    def enter_card_number(self, card_number):
        self.driver.find_element(*self.CLICK_ON_CARD_NUMBER_INPUT_LOCATOR).click()
        self.driver.find_element(*self.CLICK_ON_CARD_NUMBER_INPUT_LOCATOR).send_keys(card_number)

        valid_card_number = self.driver.find_element(*self.CLICK_ON_CARD_NUMBER_INPUT_LOCATOR).get_attribute("value")

        if card_number == valid_card_number:
            pass
        else:
            logging.error(f"Invalid card number: {card_number}")

    # Enter card code
    def enter_card_code(self, card_code):
        self.driver.find_element(*self.CLICK_ON_CARD_CODE_INPUT_LOCATOR).click()
        self.driver.find_element(*self.CLICK_ON_CARD_CODE_INPUT_LOCATOR).send_keys(card_code)

        valid_card_code = self.driver.find_element(*self.CLICK_ON_CARD_CODE_INPUT_LOCATOR).get_attribute("value")

        if card_code == valid_card_code:
            pass
        else:
            logging.error(f"Invalid card number: {card_code}")

    # Use TAB or simulate a click outside to change focus from the Code field.
    def click_on_payment_method_text(self):
        self.driver.find_element(*self.CLICK_ON_ADD_CARD_TEXT_LOCATOR).click()

    # Ensure the "Link" button becomes clickable.
    def verify_link_clickable(self):
        link_button = self.driver.find_element(*self.CHECK_IF_LINK_BUTTON_IS_DISABLED_AND_CLICK_LOCATOR)
        link_button = link_button.get_attribute("disabled")

        if link_button == "true":
            print("Link button is disabled")
        else:
            print("Link button is enabled")

    # Click "Link" and verify that the card is added successfully.
    def click_link_button(self):
        self.driver.find_element(*self.CHECK_IF_LINK_BUTTON_IS_DISABLED_AND_CLICK_LOCATOR).click()

    # Click to close window on add a card feature
    def click_on_x_button(self):
        self.driver.find_element(*self.CLICK_ON_X_BUTTON).click()

    # Card is added successfully when payment method changes from “Cash” to “Card”.
    def check_payment_method(self):
        payment_method_text = self.driver.find_element(*self.GET_PAYMENT_METHOD_TEXT)
        payment_method_text = payment_method_text.text

        expected_value = 'Card'

        assert expected_value == payment_method_text, f"Expected '{expected_value}', but got '{payment_method_text}'"

    ####################################################################################################################

    # Ensure that users can leave a comment for the driver before confirming the order.

    # Locate the comment input field.
    def click_on_comment_input(self):
        # Scroll down to the appropriate container
        comment_field = self.driver.find_element(*self.CLICK_ON_COMMENT_LABEL_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", comment_field)
        time.sleep(5)
        self.driver.find_element(*self.CLICK_ON_COMMENT_LABEL_LOCATOR).click()

    # Use the custom message from data.py
    def fill_comment_input(self, comment_text):
        self.driver.find_element(*self.CLICK_ON_COMMENT_INPUT_LOCATOR).send_keys(comment_text)

        # Retrieve and assert that the message is stored correctly.
        comment = self.driver.find_element(*self.CLICK_ON_COMMENT_INPUT_LOCATOR).get_attribute("value")

        assert comment_text == comment, f"Expected '{comment_text}', but got '{comment}'"

    ####################################################################################################################

    # Ensure users can order additional items and that they are properly displayed.

    # Click on the "Add Blanket and Handkerchiefs" slider.
    def add_blanket_and_handkerchief(self):

        # Scroll down to appropriate container
        slider = self.driver.find_elements(*self.CLICK_ON_ADD_BLANKET_AND_HANDKERCHIEFS_SLIDER_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", slider[0])

        time.sleep(5)
        slider[0].click()  # Clicks on toggle switch
        time.sleep(5)

        # Verify that the selection is confirmed using the correct assertion.
        toggle_switch = self.driver.find_elements(*self.VERIFY_TOGGLE_SWITCH_LOCATOR)
        toggle_switch = toggle_switch[0].get_property("checked")

        assert toggle_switch is True, f"Slider is not checked: {toggle_switch}"

    ####################################################################################################################

    # Ensure that selecting 2 ice creams is reflected on the screen.

    # Select "Order Ice Cream" twice.
    def increment_icecream(self):
        # Scroll down to the appropriate container
        scroller = self.driver.find_elements(*self.INCREMENTING_ICECREAM_COUNT_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", scroller[0])
        time.sleep(5)

        # Loop iterates twice
        for i in range(2):
            scroller[0].click()

    def retrieve_icecream_count(self):
        # Retrieve the count displayed.
        icecream_count = self.driver.find_elements(*self.RETRIEVE_ICECREAM_COUNTER_VALUE_LOCATOR)[0].text

        # Assert that the displayed count matches 2.
        assert icecream_count == "2", f"Expected 2 ice creams, but got {icecream_count}"

    ####################################################################################################################

    # Verify that selecting the Supportive tariff correctly triggers the car search process.

    # Click "Order" button.
    def click_on_order_button(self):
        scroller = self.driver.find_element(*self.CLICK_ON_THE_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", scroller)

        self.driver.find_element(*self.CLICK_ON_THE_ORDER_BUTTON).click()

        # Sleep until car modal is visible
        time.sleep(5)
        is_visible = self.driver.find_element(*self.VERIFY_CAR_SEARCH_MODAL)
        is_visible = is_visible.is_displayed()

        # Assert that the car search modal appears.
        assert is_visible is True, f"Visibility is not displayed: {is_visible}"
