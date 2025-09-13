import data
import helpers


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):

        # Checks if server URL is reachable
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running.")

    # Add in S8
    def test_set_route(self):
        pass

    # Add in S8
    def test_select_plan(self):
        pass

    # Add in S8
    def test_fill_phone_number(self):
        pass

    # Add in S8
    def test_fill_card(self):
        pass

    # Add in S8
    def test_comment_for_driver(self):
        pass

    # Add in S8
    def test_order_blanket_and_handkerchiefs(self):
        pass

    # Add in S8
    def test_order_2_ice_creams(self):
        # Loop iterates twice
        for i in range(2):
            # Add in S8
            pass

    # Add in S8
    def test_car_search_model_appears(self):
        pass
