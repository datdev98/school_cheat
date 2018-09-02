from splinter import Browser
from splinter import exceptions
import re


def result(browser):
    try:
        result = browser.find_by_xpath('/html/body/script[2]')[0]
        print(re.search('[\d|]+', result.html).group(0).split('|'))
    except exceptions.ElementDoesNotExist:
        print('Question does not exsits')


def main():
    with Browser() as browser:
        browser.visit('http://test.vst.edu.vn/thisinh/test/chuong/?edit=155')
        while (True):
            i = int(input('Enter number: '))
            browser.find_by_css(
                'html body div#body div.body-frame div#main-content.border.pattern.active div.grid-view-container table.grid-view tbody tr')[i-1].click()
            result(browser)
            exit = input('Exit (y): ')
            if exit == 'y':
                return
            browser.visit(
                'http://test.vst.edu.vn/thisinh/test/chuong/?edit=155')


if __name__ == "__main__":
    main()
