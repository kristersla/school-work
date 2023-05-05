from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')
# options.add_argument('start-maximized')
# options.add_argument('disable-infobars')
# options.add_argument('--disable-dev-shm-usage')
# Start a web browser
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://you.com/search?q=who+are+you&tbm=youchat")


# Wait for the element to load
# while True:





sending = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/section/main/div/div/div[1]/div[2]/div/div/li/div[1]/div[1]/p'))
)

fsending = sending.text


if fsending == '👋 Hello! My name is YouChat, I’m an AI that can answer general questions, explain things, suggest ideas, translate, summarize text, compose emails, and write code for you. I’m powered by artificial intelligence and natural language processing, allowing you to have human-like conversations with me. I am constantly learning from huge amounts of information on the internet, which means I sometimes may get some answers wrong. My AI is always improving and I will often share sources for my answers. Some example queries you can try asking me:':
    print("ready")
    x = 'tell me about something'
    send = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/section/main/div/div/div[1]/div[2]/div/div/li/div[2]/div[1]/textarea')
    send.send_keys(x)
    send.send_keys(Keys.ENTER)
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/section/main/div/div/div[1]/div[2]/div/div/li/div[1]/div[2]/div[2]/div[3]'))
    )


        # if driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/section/main/div/div/div[1]/div[2]/div/div/li/div[1]/div[3]/div[2]/div[3]/div[1]/svg'):

        #     break



    # Get the inner HTML property
    inner_html = element.get_attribute("innerHTML")
    # Do something with the inner HTML


    if inner_html == '<div class="sc-37a97b98-1 jIWNMV sc-75c1638a-3 bouEwf"><div class="sc-37a97b98-0 sc-37a97b98-2 kQnxvs fgivYs">This answer is helpful and/or accurate. Provide feedback on this result.</div><svg width="24px" height="24px" fill="none" class="sc-75c1638a-1 hXyIvg you-chat-thumb-up" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M4 13.8231C4 16.2291 5.5568 18.2253 7.47858 18.2253H9.80261C10.7412 18.7095 11.8659 19 13.1173 19H14.0931C14.987 19 15.7542 18.9479 16.2607 18.8212C17.2514 18.5754 17.8696 17.8827 17.8696 17.0037C17.8696 16.825 17.8473 16.6611 17.7952 16.5047C18.2793 16.1397 18.5549 15.6034 18.5549 15.0074C18.5549 14.7244 18.5028 14.4413 18.3985 14.2104C18.7263 13.8752 18.9125 13.3836 18.9125 12.8696C18.9125 12.5345 18.8305 12.1844 18.6816 11.9237C18.8901 11.6406 19.0019 11.2458 19.0019 10.8138C19.0019 9.74115 18.1676 8.89199 17.1024 8.89199H14.4507C14.2868 8.89199 14.175 8.82495 14.1825 8.68343C14.1899 7.92365 15.3743 6.15084 15.3743 4.72067C15.3743 3.72253 14.6741 3 13.7132 3C13.0056 3 12.5289 3.37244 12.067 4.25885C11.203 5.91993 10.1676 7.38734 8.52886 9.39851H7.21043C5.42272 9.39851 4 11.3799 4 13.8231ZM8.18622 13.7784C8.18622 12.2663 8.52886 11.298 9.48231 10.0168C10.5475 8.60149 12.0149 6.89572 13.0801 4.78026C13.3333 4.27374 13.5047 4.15456 13.7505 4.15456C14.041 4.15456 14.2421 4.37058 14.2421 4.74302C14.2421 5.86034 13.0428 7.5959 13.0428 8.71322C13.0428 9.52514 13.7132 10.0317 14.5698 10.0317H17.095C17.5345 10.0317 17.8696 10.3669 17.8696 10.8212C17.8696 11.1415 17.7654 11.3501 17.4972 11.6108C17.3557 11.7523 17.3333 11.9311 17.46 12.0801C17.6834 12.4004 17.7803 12.6089 17.7803 12.8696C17.7803 13.1899 17.6238 13.4655 17.3184 13.6965C17.1248 13.838 17.0428 14.054 17.162 14.2924C17.3259 14.6052 17.4153 14.7542 17.4153 15.0074C17.4153 15.3724 17.1769 15.648 16.6927 15.9013C16.5065 16.0056 16.4618 16.1769 16.5438 16.3482C16.7076 16.7579 16.73 16.825 16.73 16.9963C16.73 17.3315 16.4842 17.5922 15.9851 17.7188C15.568 17.8231 14.905 17.8752 14.0782 17.8603L13.1248 17.8529C10.1825 17.8305 8.18622 16.1695 8.18622 13.7784ZM5.13222 13.8231C5.13222 12.013 6.09311 10.5456 7.17318 10.5307C7.38175 10.5307 7.59032 10.5307 7.79888 10.5307C7.27747 11.514 7.054 12.5419 7.054 13.7635C7.054 15.0819 7.52328 16.2291 8.36499 17.1006C8.05959 17.1006 7.75419 17.1006 7.45624 17.1006C6.21229 17.0857 5.13222 15.6034 5.13222 13.8231Z" fill="#8B8E8F"></path></svg></div><div class="sc-37a97b98-1 jIWNMV sc-75c1638a-3 bouEwf"><div class="sc-37a97b98-0 sc-37a97b98-2 kQnxvs fgivYs">This answer is not helpful, accurate, and/or safe. Provide feedback on this result.</div><svg width="24px" height="24px" fill="none" class="sc-75c1638a-2 gIaneP you-chat-thumb-down" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M4 13.8231C4 16.2291 5.5568 18.2253 7.47858 18.2253H9.80261C10.7412 18.7095 11.8659 19 13.1173 19H14.0931C14.987 19 15.7542 18.9479 16.2607 18.8212C17.2514 18.5754 17.8696 17.8827 17.8696 17.0037C17.8696 16.825 17.8473 16.6611 17.7952 16.5047C18.2793 16.1397 18.5549 15.6034 18.5549 15.0074C18.5549 14.7244 18.5028 14.4413 18.3985 14.2104C18.7263 13.8752 18.9125 13.3836 18.9125 12.8696C18.9125 12.5345 18.8305 12.1844 18.6816 11.9237C18.8901 11.6406 19.0019 11.2458 19.0019 10.8138C19.0019 9.74115 18.1676 8.89199 17.1024 8.89199H14.4507C14.2868 8.89199 14.175 8.82495 14.1825 8.68343C14.1899 7.92365 15.3743 6.15084 15.3743 4.72067C15.3743 3.72253 14.6741 3 13.7132 3C13.0056 3 12.5289 3.37244 12.067 4.25885C11.203 5.91993 10.1676 7.38734 8.52886 9.39851H7.21043C5.42272 9.39851 4 11.3799 4 13.8231ZM8.18622 13.7784C8.18622 12.2663 8.52886 11.298 9.48231 10.0168C10.5475 8.60149 12.0149 6.89572 13.0801 4.78026C13.3333 4.27374 13.5047 4.15456 13.7505 4.15456C14.041 4.15456 14.2421 4.37058 14.2421 4.74302C14.2421 5.86034 13.0428 7.5959 13.0428 8.71322C13.0428 9.52514 13.7132 10.0317 14.5698 10.0317H17.095C17.5345 10.0317 17.8696 10.3669 17.8696 10.8212C17.8696 11.1415 17.7654 11.3501 17.4972 11.6108C17.3557 11.7523 17.3333 11.9311 17.46 12.0801C17.6834 12.4004 17.7803 12.6089 17.7803 12.8696C17.7803 13.1899 17.6238 13.4655 17.3184 13.6965C17.1248 13.838 17.0428 14.054 17.162 14.2924C17.3259 14.6052 17.4153 14.7542 17.4153 15.0074C17.4153 15.3724 17.1769 15.648 16.6927 15.9013C16.5065 16.0056 16.4618 16.1769 16.5438 16.3482C16.7076 16.7579 16.73 16.825 16.73 16.9963C16.73 17.3315 16.4842 17.5922 15.9851 17.7188C15.568 17.8231 14.905 17.8752 14.0782 17.8603L13.1248 17.8529C10.1825 17.8305 8.18622 16.1695 8.18622 13.7784ZM5.13222 13.8231C5.13222 12.013 6.09311 10.5456 7.17318 10.5307C7.38175 10.5307 7.59032 10.5307 7.79888 10.5307C7.27747 11.514 7.054 12.5419 7.054 13.7635C7.054 15.0819 7.52328 16.2291 8.36499 17.1006C8.05959 17.1006 7.75419 17.1006 7.45624 17.1006C6.21229 17.0857 5.13222 15.6034 5.13222 13.8231Z" fill="#8B8E8F"></path></svg></div>':
        pra_text = driver.find_element("xpath", '//*[@id="chatHistory"]/div/div[2]/div[1]/p')
        fpra_text = pra_text.text
        print(fpra_text)

time.sleep(40)
# Close the web browser
driver.quit()