from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from sys import argv


the_url = "https://hrsa.cunyfirst.cuny.edu/psc/cnyhcprd/GUEST/HRMS/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL"
source = ""
change = False
driver = webdriver.PhantomJS()
driver.set_window_size(1024, 2048) # to keep large page visible including links at the bottom

def compare_source(driver):
    return source != driver.page_source

def wait_a_sec():
    source = driver.page_source
    WebDriverWait(driver, 2).until(compare_source)
#    sleep(3)

def save_html(name):
    f = open(name, 'w')
    container = driver.find_element_by_id("PAGECONTAINER")
    f.write(container.get_attribute("innerHTML"))
    f.close()
    
def crawl(url):
    print "Starting"
    driver.get(url)
    print "Landing page loaded."
    loc_select = Select(driver.find_element_by_name('CLASS_SRCH_WRK2_INSTITUTION$42$'))
    term_select = Select(driver.find_element_by_name('CLASS_SRCH_WRK2_STRM$45$'))

    print "Locs: ", len(loc_select.options)
    print "Terms: ", len(term_select.options)
    loc_select.select_by_index(3)
    term_select.select_by_index(1)

    wait_a_sec()
    subj_select = Select(driver.find_element_by_name('SSR_CLSRCH_WRK_SUBJECT_SRCH$0'))
    print "Subjs: ", len(subj_select.options)
    subj_select.select_by_index(8)
    print "Params selected, searching"
    driver.find_element_by_id('CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH').click()

    i = 0
    while i < 9:
        wait_a_sec()
        print "Processing Id = ", i
        id = 'MTG_CLASSNAME$' + str(i)
        try:
            link = driver.find_element_by_id(id)
            name = link.text + "_isolated.html"
            name.replace(" " , "_")
            print "Name: ", name
            link.click()
            wait_a_sec()
            save_html(name)
            driver.find_element_by_id('CLASS_SRCH_WRK2_SSR_PB_BACK').click()
        except:
            save_html("error.html")
            raise
        i = i + 1


if __name__ == '__main__':
    if len(argv) < 2:
        print "Please provide target URL as an argument."
    else:
        crawl(argv[1])

