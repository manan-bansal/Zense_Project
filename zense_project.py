from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

no_products = []
l1 = []

#takes input of the flipkart id and password
email1 = input("Enter your Flipkart Email ID: ")
password1 = input("Enter your FLipkart Password: ")

#list of daily needed products
daily_products = ["Surf Excel Matic Detergent Powder Top load ( 2 kg ) 2 kg Washing Powder","xiaomi mi 4","Pears Pure & Gentle Bathing Bar  (375 g, Pack of 3)","Dove Daily Shine Shampoo  (650 ml)","Joy Honey & Almonds Advanced Nourishing Body Lotion(Pack of 2 x 300 ml)  (600 ml)","Vim Dish Cleaning Gel  (Lemon)"]


browser1 = webdriver.Chrome(executable_path = r"./chromedriver")
browser1.get("https://web.whatsapp.com/")  #Opens Whatsapp Web
time.sleep(12)

#Searches a group named Flipkart in whatsapp web
browser1.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").click()
group = browser1.find_element_by_css_selector("input.jN-F5.copyable-text.selectable-text")
group.send_keys("Flipkart")
time.sleep(5)

#opens the flipkart whatsapp group
browser1.find_element_by_class_name('dIyEr').click()
time.sleep(2)

#displays the list of daily products to the rest of the group members
#the serial numbers of the products correspond to the number by which the members can order stuff
fgroup5 = browser1.find_element_by_css_selector("div._2S1VP.copyable-text.selectable-text")
for i in range(len(daily_products)):
    fgroup5.send_keys(str(i) + ") " + daily_products[i])
    fgroup5.send_keys(Keys.ENTER)
    time.sleep(2)

#this displays that portal is open to take orders
fgroup4 = browser1.find_element_by_css_selector("div._2S1VP.copyable-text.selectable-text")
fgroup4.send_keys("OPEN")
fgroup4.send_keys(Keys.ENTER)


#this list contains the text on the page
p = browser1.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")

time.sleep(2)
product = p[-1].text

#this loop is basically to check the OPEN text
while(product == "OPEN"):
        p = browser1.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
        time.sleep(2)
        product = p[-1].text


#main loop
while(product[0] != "OPEN"):
    no_products = []
    #this displays that your order is in process
    fgroup1 = browser1.find_element_by_css_selector("div._2S1VP.copyable-text.selectable-text")
    fgroup1.send_keys("ORDER IN PROCESS")
    time.sleep(2)
    fgroup1.send_keys(Keys.ENTER)
    time.sleep(2)

    #opens flipkart
    browser = webdriver.Chrome(executable_path = r"./chromedriver")
    browser.get("https://www.flipkart.com/")
    time.sleep(2)
    
    #enters email id
    email = browser.find_element_by_css_selector("input._2zrpKA")
    email.send_keys(email1)

    
    time.sleep(2)

    #enters password
    try:
        browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").click()
        password = browser.find_element_by_css_selector("input._2zrpKA._3v41xv")
        password.send_keys(password1)
        time.sleep(2)

    except:

        browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/button").click()
        password2 = browser.find_element_by_css_selector("input._2zrpKA._3v41xv")
        password2.send_keys(password1)
        time.sleep(2)
        
    browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()

    time.sleep(2)
    #for searching in the search bar
    browser.find_element_by_xpath("//*[@id='container']/div/header/div[1]/div/div[2]/form/div/div[1]/div/input")

    time.sleep(2)

    i = 0;
    j = 0;
    #loop for multiple item orders
    while(product[i] != 'S'):
        item = browser.find_element_by_css_selector("input.LM6RPg")
        item.send_keys(daily_products[int(product[i])])
        item.send_keys(Keys.ENTER)
        time.sleep(8)
        browser.find_element_by_xpath("//*[@id='container']/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div/a[2]").click()
        time.sleep(8)
        #this is basically changing the browser window 
        l =  (browser.window_handles)
        browser.switch_to_window(l[j+1])
        time.sleep(5)
        try:
            browser.find_element_by_xpath("//*[@id='container']/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[1]/button").click()
        except:
            no_products.append(int(product[i]))

        i+=2
        j+=1
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='container']/div/div[1]/div/div[1]/div/div[3]/form/button").click()

    time.sleep(3)

    browser1.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").click()
    time.sleep(2)

    fgroup3 = browser1.find_element_by_css_selector("div._2S1VP.copyable-text.selectable-text")
    
    #this will display products that are not available 
    if(len(no_products) > 0):
        for i in range(len(no_products)):
            fgroup3.send_keys("Product with code " + str(no_products[i]) + " is not available")
            fgroup3.send_keys(Keys.ENTER)


    #this will send the link of the checkout in the whatsapp group to the user
    fgroup = browser1.find_element_by_css_selector("div._2S1VP.copyable-text.selectable-text")
    fgroup.send_keys(browser.current_url)
    time.sleep(2)
    fgroup.send_keys(Keys.ENTER)
    
    #quits the flipkart browser
    browser.quit()



    
    fgroup2 = browser1.find_element_by_css_selector("div._2S1VP.copyable-text.selectable-text")
    fgroup2.send_keys("Please proceed for checkout by clicking the above link.")
    time.sleep(2)
    fgroup2.send_keys(Keys.ENTER)
    fgroup2.send_keys("OPEN")
    fgroup2.send_keys(Keys.ENTER)
    time.sleep(2)


    p = browser1.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
    time.sleep(2)
    product = p[-1].text

    time.sleep(2)
    
    #checks for more orders
    while(product == "OPEN"):
        p = browser1.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
        time.sleep(2)
        product = p[-1].text

