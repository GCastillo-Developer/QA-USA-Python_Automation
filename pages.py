import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import data


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
        WebDriverWait(self.driver,3)
        self.driver.find_element(*self.FROM_ADDRESS_LOCATOR).send_keys(from_address)

    def get_from_location(self):
        return self.driver.find_element(*self.FROM_ADDRESS_LOCATOR).get_attribute("value")

    # Sends to keys to address locator and asserts value in input field
    def enter_to_location(self, to_address):
        WebDriverWait(self.driver,3)
        self.driver.find_element(*self.TO_ADDRESS_LOCATOR).send_keys(to_address)

    def get_to_location(self):
        return self.driver.find_element(*self.TO_ADDRESS_LOCATOR).get_attribute("value")

    ########################################################################################################################
    # Ensure users can choose the Supportive plan and validate their selection without hardcoding values.

    # Clicks call a taxi button
    def call_a_taxi(self):
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.CALL_A_TAXI_LOCATOR))
        self.driver.find_element(*self.CALL_A_TAXI_LOCATOR).click()

    # Clicks supportive plan option
    def click_on_plan(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.SUPPORTIVE_PLAN_ACTION_LOCATOR))
        self.driver.find_element(*self.SUPPORTIVE_PLAN_ACTION_LOCATOR).click()

    # Finds the active t-card selection and asserts expected selection
    def find_active_selection(self):
        return self.driver.find_element(*self.TCARD_ACTIVE_LOCATOR).text

    #######################################################################################################################
    # Ensure that users can enter their phone number, receive a confirmation SMS code, and validate their login.

    # click on the phone number field
    def click_on_phone_number_field(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.PHONE_NUMBER_FIELD_LOCATOR))
        self.driver.find_element(*self.PHONE_NUMBER_FIELD_LOCATOR).click()

    # Clicks on the pop-up phone number field
    def click_on_secondary_phone_number_field(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.PHONE_NUMBER_POP_UP_LABEL_LOCATOR))
        self.driver.find_element(*self.PHONE_NUMBER_POP_UP_LABEL_LOCATOR).click()

    # Enters phone number on pop-up field and asserts value in input field
    def enter_phone_number(self, phone_number):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.PHONE_NUMBER_INPUT_LOCATOR))
        self.driver.find_element(*self.PHONE_NUMBER_INPUT_LOCATOR).send_keys(phone_number)

    def retrieve_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_INPUT_LOCATOR).get_attribute("value")

    # Clicks the next button on pop-up phone number field
    def click_next_button(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.CLICK_NEXT_BUTTON_LOCATOR))
        self.driver.find_element(*self.CLICK_NEXT_BUTTON_LOCATOR).click()

    # Clicks on the pop-up code label field
    def click_on_code_label(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.CODE_LABEL_FIELD_LOCATOR))
        self.driver.find_element(*self.CODE_LABEL_FIELD_LOCATOR).click()

    # Sends the code to the input field
    def enter_code(self, code):
        self.driver.find_element(*self.CODE_INPUT_FIELD_LOCATOR).send_keys(code)

    # Clicks the confirm button
    def confirm_button(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.CONFIRM_BUTTON_LOCATOR))
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    ########################################################################################################################
    # Here is where combine methods are

    # Combine methods for the from and to address
    def enter_locations(self, from_address, to_address):
        self.enter_from_location(from_address)
        self.enter_to_location(to_address)

    # Combines methods to enter sms code and confirm
    def enter_code_and_confirm(self, sms_code):
        self.click_on_code_label()
        self.enter_code(sms_code)
        self.confirm_button()

    # Combines method to enter phone number and click next button
    def enter_phone_number_click_next(self, phone_number,):
        self.click_on_phone_number_field()
        self.click_on_secondary_phone_number_field()
        self.enter_phone_number(phone_number)
        self.click_next_button()

    # Enters card information
    def enter_card_information(self, card_number, card_code):
        self.click_card_number_field()
        self.enter_card_number(card_number)
        validate_card = self.retrieve_card_number()
        self.validate_card_number(validate_card)
        self.click_card_code_field()
        self.enter_card_code(card_code)
        validate_code = self.retrieve_card_code()
        self.validate_card_code(validate_code)

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
    def click_on_payment_method(self):
        WebDriverWait(self.driver,3).until(EC.visibility_of_element_located(self.PAYMENT_METHOD_FIELD_LOCATOR))
        self.driver.find_element(*self.PAYMENT_METHOD_FIELD_LOCATOR).click()

    # Click on Add Card
    def click_on_add_card(self):
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.CLICK_ON_ADD_CARD_LOCATOR))
        self.driver.find_element(*self.CLICK_ON_ADD_CARD_LOCATOR).click()

    # Enter a valid Card Number.
    def click_card_number_field(self):
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.CLICK_ON_CARD_NUMBER_INPUT_LOCATOR))
        self.driver.find_element(*self.CLICK_ON_CARD_NUMBER_INPUT_LOCATOR).click()

    def enter_card_number(self, card_number):
        self.driver.find_element(*self.CLICK_ON_CARD_NUMBER_INPUT_LOCATOR).send_keys(card_number)

    def retrieve_card_number(self):
        return self.driver.find_element(*self.CLICK_ON_CARD_NUMBER_INPUT_LOCATOR).get_attribute("value")

    @staticmethod
    def validate_card_number(card_number):
        if data.CARD_NUMBER == card_number:
            pass
        else:
            logging.error(f"Invalid card number: {card_number}")

    def click_card_code_field(self):
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.CLICK_ON_CARD_CODE_INPUT_LOCATOR))
        self.driver.find_element(*self.CLICK_ON_CARD_CODE_INPUT_LOCATOR).click()

    def enter_card_code(self, card_code):
        self.driver.find_element(*self.CLICK_ON_CARD_CODE_INPUT_LOCATOR).send_keys(card_code)

    def retrieve_card_code(self):
        return self.driver.find_element(*self.CLICK_ON_CARD_CODE_INPUT_LOCATOR).get_attribute("value")

    @staticmethod
    def validate_card_code(card_code):
        if data.CARD_CODE == card_code:
            pass
        else:
            logging.error(f"Invalid card number: {card_code}")

    # Use TAB or simulate a click outside to change focus from the Code field.
    def click_on_payment_method_text(self):
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.CLICK_ON_ADD_CARD_TEXT_LOCATOR))
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
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.CHECK_IF_LINK_BUTTON_IS_DISABLED_AND_CLICK_LOCATOR))
        self.driver.find_element(*self.CHECK_IF_LINK_BUTTON_IS_DISABLED_AND_CLICK_LOCATOR).click()

    # Click to close window on add a card feature
    def click_on_x_button(self):
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.CLICK_ON_X_BUTTON))
        self.driver.find_element(*self.CLICK_ON_X_BUTTON).click()

    # Card is added successfully when payment method changes from “Cash” to “Card”.
    def check_payment_method(self):
        return self.driver.find_element(*self.GET_PAYMENT_METHOD_TEXT).text

    ####################################################################################################################

    # Ensure that users can leave a comment for the driver before confirming the order.

    # Locate the comment input field.
    def click_on_comment_input(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.CLICK_ON_COMMENT_LABEL_LOCATOR))
        # Scroll down to the appropriate container
        self.driver.find_element(*self.CLICK_ON_COMMENT_LABEL_LOCATOR).click()

    # Use the custom message from data.py
    def fill_comment_input(self, comment_text):
        self.driver.find_element(*self.CLICK_ON_COMMENT_INPUT_LOCATOR).send_keys(comment_text)

    def retrieve_comment_input(self):
        # Retrieve and assert that the message is stored correctly.
        return self.driver.find_element(*self.CLICK_ON_COMMENT_INPUT_LOCATOR).get_attribute("value")

    ####################################################################################################################

    # Ensure users can order additional items and that they are properly displayed.

    # Click on the "Add Blanket and Handkerchiefs" slider.
    def click_on_blanket_and_handkerchief(self):
        # Scroll down to appropriate container
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.CLICK_ON_ADD_BLANKET_AND_HANDKERCHIEFS_SLIDER_LOCATOR))
        slider = self.driver.find_elements(*self.CLICK_ON_ADD_BLANKET_AND_HANDKERCHIEFS_SLIDER_LOCATOR)

        slider[0].click()  # Clicks on toggle switch

    def return_toggle_switch(self):
        toggle_switch = self.driver.find_elements(*self.VERIFY_TOGGLE_SWITCH_LOCATOR)
        return toggle_switch[0].get_property("checked")

    ####################################################################################################################

    # Ensure that selecting 2 ice creams is reflected on the screen.

    # Select "Order Ice Cream" twice.
    def increment_icecream(self):
        # Scroll down to the appropriate container
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.INCREMENTING_ICECREAM_COUNT_LOCATOR))
        scroller = self.driver.find_elements(*self.INCREMENTING_ICECREAM_COUNT_LOCATOR)

        # Loop iterates twice
        for i in range(2):
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.INCREMENTING_ICECREAM_COUNT_LOCATOR))
            scroller[0].click()

    def retrieve_icecream_count(self):
        # Retrieve the count displayed.
        return self.driver.find_elements(*self.RETRIEVE_ICECREAM_COUNTER_VALUE_LOCATOR)[0].text

    ####################################################################################################################

    # Verify that selecting the Supportive tariff correctly triggers the car search process.

    # Click "Order" button.
    def click_on_order_button(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.CLICK_ON_THE_ORDER_BUTTON))
        self.driver.find_element(*self.CLICK_ON_THE_ORDER_BUTTON).click()

    def car_search_modal_displayed (self):
        WebDriverWait(self.driver,3).until(EC.visibility_of_element_located(self.VERIFY_CAR_SEARCH_MODAL))
        is_visible = self.driver.find_element(*self.VERIFY_CAR_SEARCH_MODAL).is_displayed()
        return is_visible