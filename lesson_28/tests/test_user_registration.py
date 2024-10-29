from assertpy import assert_that

from lesson_28.pages.main_page import MainPage
from lesson_28.pages.user_page import UserPage
from lesson_28.test_data.tese_data import TestData


class TestUserRegistration:
    main_page: MainPage
    user_page: UserPage

    def test_that_user_able_to_register(self, web_driver):
        self.main_page = MainPage(web_driver)
        self.main_page.new_user_registration()

        self.user_page = UserPage(web_driver)
        self.user_page.click_on_my_profile_menu()

        assert_that(web_driver.current_url,
                    f"GARAGE_PATH ends differently").contains(TestData.GARAGE_PATH)
        assert_that(self.user_page.logout_button,
                    f"The logout button doesn't exist").is_not_none()

        user_name: str = self.user_page.get_profile_name_text()

        (assert_that(user_name,
                    f"User name is not equal to {TestData.USER_FIRST_NAME}").
            contains(TestData.USER_FIRST_NAME))






