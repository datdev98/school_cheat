from splinter import Browser

browser = Browser('chrome')


def setup():
    browser.visit('http://sis.hust.edu.vn')


def login(username, password):
    username_input = browser.find_by_xpath('//*[@id="cLogIn1_tb_cLogIn_User_I"]')[0]
    password_input = browser.find_by_xpath('//*[@id="cLogIn1_tb_cLogIn_Pass_I"]')[0]
    login_button = browser.find_by_xpath('//*[@id="cLogIn1_tb_cLogIn_Pass_I"]')[0]

    username_input.fill(username)
    password_input.fill(password)
    login_button.click()


def get_timetable(student_id):
    browser.visit('http://sis.hust.edu.vn/ModulePlans/Timetables.aspx')

    student_id_input = browser.find_by_xpath('//*[@id="MainContent_Studentid_I"]')
    find_button = browser.find_by_xpath('//*[@id="MainContent_btFind_B"]')

    student_id_input.fill(student_id)
    find_button.click()

if __name__ == '__main__':
    # setup()
    # login("20165963", "PaV9iFkTyJQG7oCh")
    get_timetable("20165963")
