import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_welcome_screen():
    with allure.step('Нажатие кнопки Continue на первой странице'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

    with allure.step('Проверка перехода на вторую страницу'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
                have.text('New ways to explore'))

    with allure.step('Нажатие кнопки Continue на второй странице'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

    with allure.step('Проверка перехода на третью страницу'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
                have.text('Reading lists with sync'))

    with allure.step('Нажатие кнопки Continue на третьей странице'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

    with allure.step('Проверка перехода на четвертую страницу'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text('Data & Privacy'))

    with allure.step('Нажатие кнопки Get started на четвертой странице'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")).click()
