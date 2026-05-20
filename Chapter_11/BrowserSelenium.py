from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('bookcover')
    print('element with <%s>  the given class name found!' %
          (elem.tag_name))
except:
    print('No element with the given class name could be found.')
