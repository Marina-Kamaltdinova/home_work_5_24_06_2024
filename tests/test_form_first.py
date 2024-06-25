import time
from selene import browser, command, have, by
import os

def test_registration_demoqa():
        browser.open('/automation-practice-form')
        browser.element('#firstName').type('Kam')
        browser.element('#lastName').type('Mar')
        browser.element('#userEmail').type('m81321184@gmail.com')
        browser.element('[for="gender-radio-2"]').click()
        browser.element("#userNumber").type('1234567890')
        browser.element('#subjectsInput').type('computer').press_enter()
        browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
        browser.element('.react-datepicker__month-select').click().element('[value="3"]').click()
        browser.element('.react-datepicker__year-select').click().element('[value="2000"]').click()
        browser.element('.react-datepicker__day--002').click()
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('#uploadPicture').send_keys(os.path.abspath('../img.png.png'))
        browser.element('#currentAddress').type('ЦАО').press_enter()
        browser.element("#react-select-3-input").type("Rajasthan").press_enter()
        browser.element("#react-select-4-input").type("Jaiselmer").press_enter()
        browser.element('#submit').press_enter()
        time.sleep(5)
        browser.element("#example-modal-sizes-title-lg").should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(have.exact_texts('Kam Mar','m81321184@gmail.com', 'Female', '1234567890', '02 April,2000', 'Computer Science', 'Sports', 'img.png.png', 'ЦАО', 'Rajasthan Jaiselmer'))


