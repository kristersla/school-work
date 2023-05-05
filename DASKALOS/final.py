import speech_recognition as sr
from selenium import webdriver
from gtts import gTTS
import time
import os
from selenium.webdriver.common.keys import Keys
import string
from selenium.webdriver.common.action_chains import ActionChains
from playsound import playsound
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = 'eskristers05'
password = 'eskristers05'

# fireFoxOptions = webdriver.FirefoxOptions()
# fireFoxOptions.set_headless()

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-dev-shm-usage')

laikapstakli = ["laikapstākļi", "laiks", "temperatūra"]
muzika = ["mūzika", "dziesma", "mūziku", "dziesmu", "spotify"]
eklase = ["vērtējums", "e klase", "ēklase", "atzīme"]
ai = ["gudrais", "sameklē", "atrodi"]
kripto = ["kripto", "kriptovalūtu", "valūta", "valūtu"]
email = ["e-pasts", "vēstuli"]
no = ["nē", "tas viss", "paldies par darbu"]

# tts = gTTS("Mani sauc, Daskalos!", lang='lv')
# tts.save("mytext.mp3")
# os.system("mytext.mp3")
# time.sleep(2)
# tts = gTTS("Esmu gatavs darbam, kā varētu jums šobrīt palīdzēt?", lang='lv')
# tts.save("mytext.mp3")
# os.system("start mytext.mp3")
# time.sleep(4)

r = sr.Recognizer()

with sr.Microphone() as source2:	
    while True:
        
        r.adjust_for_ambient_noise(source2, duration=0.2)
        print("runa!")
        audio2 = r.listen(source2)
        print("raksta...")
        MyText = r.recognize_google(audio2, language='lv')
        
        try:

            if any(word in MyText for word in no):
                print("done!")
                tts = gTTS("Bija prieks palīdzēt! Lai Jums jauka diena!", lang='lv')
                tts.save("mytext.mp3")
                os.system("start mytext.mp3")
                break
            
            print(MyText)
            MyText = MyText.lower()
            
            if any(word in MyText for word in laikapstakli):

                tts = gTTS("Es tūlīt noskaidrošu kādi ir tagadējie laikapstākļi Rīgā, lūdzu uzgaidiet mazliet!", lang='lv')
                tts.save("mytext.mp3")
                os.system("start mytext.mp3")
                driver = webdriver.Chrome(chrome_options=options)
                driver.maximize_window()
                driver.get("https://weather.com/lv-LV/laiks/sodien/l/LGXX0004:1:LG?Goto=Redirected")

                temp =driver.find_element("xpath",'//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[2]/div[1]/div[1]/span')
                wind_speed =driver.find_element("xpath",'//*[@id="todayDetails"]/section/div[2]/div[2]/div[2]/span')
                phrase = driver.find_element("xpath",'//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[2]/div[1]/div[1]/div[1]')

                ftemp = temp.text
                fwind = wind_speed.text
                fphrase = phrase.text
                ftempr = ftemp[:-1]
                fwinds = fwind[:-4]
                print(fphrase)

                if '1' in ftemp:
                    tts = gTTS(f"Pašlaik āra ir {ftempr} grads, ar vēja ātrumu {fwinds} kilometri stunda, kā arī ārā pašlaik ir {fphrase}", lang='lv')
                    tts.save("mytext.mp3")
                    os.system("start mytext.mp3")
                    time.sleep(14)

                tts = gTTS(f"Pašlaik ārā ir {ftempr} grādi, ar vēja ātrumu {fwinds} kilometri stundā, kā arī ārā pašlaik ir {fphrase} ", lang='lv')
                tts.save("mytext.mp3")
                os.system("start mytext.mp3")
                time.sleep(14)
 
                driver.close()
                time.sleep(7)
                tts = gTTS("Kā es jums vēl varētu palīdzēt?", lang='lv')
                tts.save("mytext.mp3")
                os.system("start mytext.mp3")
                time.sleep(4)

            if any(word in MyText for word in muzika):
                
                tts = gTTS("Ko vēlaties, lai es jums atskaņoju?", lang='lv')
                tts.save("mytext.mp3")
                os.system("start mytext.mp3")
                time.sleep(4)
                r8 = sr.Recognizer()
                with sr.Microphone() as source8:
                    r8.adjust_for_ambient_noise(source8, duration=0.2)
                    print("runā!")
                    audio8 = r8.listen(source8)
                    print("raksta")
                    muzika = r8.recognize_google(audio8, language='en')

                    try:
                        tts = gTTS("Lūdzu nedaudz uzgaidiet!", lang='lv')
                        tts.save("mytext.mp3")
                        os.system("start mytext.mp3")
                        print(muzika)
                        driver4 = webdriver.Chrome()
                        driver4.maximize_window()
                        driver4.get("https://accounts.spotify.com/en/login")

                        actions = ActionChains(driver4) 
                        username_field = driver4.find_element("xpath",'//*[@id="login-username"]')
                        password_field = driver4.find_element("xpath",'//*[@id="login-password"]')
                        username_field.send_keys("kristersla@gmail.com")
                        password_field.send_keys("eskristers05")
                        
                        Apply_for = driver4.find_element("xpath",'/html/body/div[1]/div/div[2]/div/div/div[1]/div[3]/div[2]/button/div[1]').click()
                        time.sleep(1)
                        print("1")
                        web_player = driver4.find_element("xpath",'//*[@id="root"]/div/div[2]/div/div/button[2]').click()
                        print("1")
                        time.sleep(3)
                        print("1")
                        cookies = driver4.find_element("xpath", '//*[@id="onetrust-accept-btn-handler"]').click()
                        print("1")
                        time.sleep(1)
                        search= driver4.find_element("xpath",'//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a').click()
                        time.sleep(2)
                        Song_search_field = driver4.find_element("xpath",'//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input')
                        Song_search_field.send_keys(muzika)
                        time.sleep(1)
                        play_button = driver4.find_element("xpath", '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[2]/div/div/section[1]/div[2]/div/div/div/div[3]/div/button')
                        actions.move_to_element(play_button).click().perform()

                        wait_time=driver4.find_element("xpath", '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[2]/div[3]')

                        wait_time2 = wait_time.text

                        ftime = wait_time2
                        time_parts = ftime.split(':')
                        minutes = int(time_parts[0])
                        seconds = int(time_parts[1])
                        total_song_seconds = (minutes * 60) + seconds
                        print(total_song_seconds)
                        time.sleep(total_song_seconds)

                        driver4.close()
                    except:
                        print("nestrada")
                        
            if any(word in MyText for word in eklase):

                tts = gTTS("Nevari pats apskatīties savas atzīmes, tikai nodarbina mani, lai nu kā uzgaidi, kamer apskatos!", lang='lv')
                tts.save("mytext.mp3")
                os.system("start mytext.mp3")
                

                driver2 = webdriver.Chrome(chrome_options=options)
                driver2.maximize_window()
                driver2.get("https://www.e-klase.lv/")

                euser = driver2.find_element("xpath",'/html/body/div[8]/div[3]/aside/div[1]/div[2]/form/div[1]/input')
                euser.send_keys(username)

                epass = driver2.find_element("xpath", '/html/body/div[8]/div[3]/aside/div[1]/div[2]/form/div[2]/input')
                epass.send_keys(password)

                login =driver2.find_element("xpath",'/html/body/div[8]/div[3]/aside/div[1]/div[2]/form/button').click()

                atzime = driver2.find_element("xpath", '//*[@id="recent_scores"]/div[2]/div/div[1]/div[1]/div[3]/span')
                datums = driver2.find_element("xpath", '//*[@id="recent_scores"]/div[2]/div/div[1]/div[1]/div[2]/span[2]')
                prieksmats = driver2.find_element("xpath", '//*[@id="recent_scores"]/div[2]/div/div[1]/div[1]/div[1]/h4')

                fat = atzime.text
                fpr = prieksmats.text
                fda = datums.text

                if fpr == 'Svešvaloda (B1) K':
                    fpr = 'krievu valoda'

                if fpr == 'Svešvaloda (B2) A':
                    fpr = 'krievu valoda'
                
                driver2.close()
                tts = gTTS(f"Jums pēdēja atzīme ir ievietota {fpr[:-1]}, jūsu vērtējums ir {fat}, kas ir ielikts {fda} datumā.", lang='lv')
                tts.save("mytext.mp3")
                os.system("start mytext.mp3")
                time.sleep(10)

                tts = gTTS("Kā es jums vēl varētu palīdzēt?", lang='lv')
                tts.save("mytext.mp3")
                os.system("start mytext.mp3")
                time.sleep(5)
            
            if any(word in MyText for word in ai):
                
                tts = gTTS("Ko vēlies uzzināt?", lang='lv')
                tts.save("mytext.mp3")
                os.system("start mytext.mp3")
                time.sleep(2)
                r7 = sr.Recognizer()
                with sr.Microphone() as source7:
                    r7.adjust_for_ambient_noise(source7, duration=0.2)
                    print("runā!")
                    audio7 = r7.listen(source7)
                    print("raksta")
                    about = r7.recognize_google(audio7, language='lv')

                    try:
                        print(about)
                        tts = gTTS("Tūlīt noskaidrošu vajadzīgo informāciju, nedaudz uzgaidiet!", lang='lv')
                        tts.save("mytext.mp3")
                        os.system("start mytext.mp3")

                        driver = webdriver.Chrome()
                        driver.maximize_window()
                        driver.get(f"https://you.com/search?q=who+are+you&tbm=youchat")
                        time.sleep(2)
                        sending = WebDriverWait(driver, 60).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/section/main/div/div/div[1]/div[2]/div/div/li/div[1]/div[1]/p'))
                        )

                        fsending = sending.text

                        if fsending == '👋 Hello! My name is YouChat, I’m an AI that can answer general questions, explain things, suggest ideas, translate, summarize text, compose emails, and write code for you. I’m powered by artificial intelligence and natural language processing, allowing you to have human-like conversations with me. I am constantly learning from huge amounts of information on the internet, which means I sometimes may get some answers wrong. My AI is always improving and I will often share sources for my answers. Some example queries you can try asking me:':
                            send = driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/section/main/div/div/div[1]/div[2]/div/div/li/div[2]/div[1]/textarea')
                            send.send_keys(about)
                            send.send_keys(Keys.ENTER)
                            element = WebDriverWait(driver, 60).until(
                                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/section/main/div/div/div[1]/div[2]/div/div/li/div[1]/div[2]/div[2]/div[3]'))
                            )
                            tts = gTTS("Vēl meklēju savā prātā. Uzgadi!", lang='lv')
                            tts.save("mytext.mp3")
                            os.system("start mytext.mp3")
                            inner_html = element.get_attribute("innerHTML")
                            if inner_html == '<svg width="28px" height="20px" viewBox="0 0 16 20" fill="none" class="sc-bb59ee19-1 fTDSZX youchat-share-button" xmlns="http://www.w3.org/2000/svg"><path d="M3.29698 19.3333H12.6475C13.5388 19.3333 14.213 19.1048 14.6701 18.6477C15.1272 18.1906 15.3557 17.525 15.3557 16.6508V8.71442C15.3557 7.83451 15.1272 7.16887 14.6701 6.71748C14.213 6.26039 13.5388 6.03184 12.6475 6.03184H10.4791V7.74595H12.5189C12.8789 7.74595 13.156 7.84023 13.3502 8.02878C13.5445 8.21162 13.6416 8.49444 13.6416 8.87726V16.4793C13.6416 16.8564 13.5445 17.1393 13.3502 17.3278C13.156 17.5164 12.8789 17.6107 12.5189 17.6107H3.42554C3.06557 17.6107 2.78846 17.5164 2.59419 17.3278C2.40564 17.1393 2.31137 16.8564 2.31137 16.4793V8.87726C2.31137 8.49444 2.40564 8.21162 2.59419 8.02878C2.78846 7.84023 3.06557 7.74595 3.42554 7.74595H5.49104V6.03184H3.29698C2.41136 6.03184 1.73714 6.25753 1.27433 6.70891C0.817232 7.16029 0.588684 7.8288 0.588684 8.71442V16.6508C0.588684 17.525 0.817232 18.1906 1.27433 18.6477C1.73714 19.1048 2.41136 19.3333 3.29698 19.3333ZM7.9765 12.8197C8.19362 12.8197 8.37932 12.7426 8.53359 12.5883C8.69357 12.4283 8.77356 12.2455 8.77356 12.0398V3.93205L8.705 2.73218L9.18495 3.34068L10.282 4.50628C10.4248 4.66055 10.6019 4.73768 10.8134 4.73768C11.0076 4.73768 11.1733 4.67483 11.3104 4.54913C11.4476 4.41772 11.5161 4.25488 11.5161 4.06061C11.5161 3.87206 11.4447 3.7035 11.3019 3.55495L8.58501 0.940929C8.48216 0.838083 8.37932 0.766662 8.27647 0.726666C8.17934 0.68667 8.07935 0.666672 7.9765 0.666672C7.86794 0.666672 7.76224 0.68667 7.65939 0.726666C7.56226 0.766662 7.46227 0.838083 7.35942 0.940929L4.65113 3.55495C4.50257 3.7035 4.42829 3.87206 4.42829 4.06061C4.42829 4.25488 4.49686 4.41772 4.63399 4.54913C4.77111 4.67483 4.93395 4.73768 5.12251 4.73768C5.33963 4.73768 5.51961 4.66055 5.66245 4.50628L6.75948 3.34068L7.23943 2.73218L7.17087 3.93205V12.0398C7.17087 12.2455 7.248 12.4283 7.40227 12.5883C7.56226 12.7426 7.75367 12.8197 7.9765 12.8197Z" fill="#8b8e8f"></path></svg><div class="sc-37a97b98-1 jIWNMV sc-bb59ee19-4 cGzDqI"><div class="sc-37a97b98-0 sc-37a97b98-2 kQnxvs fgivYs">This answer is helpful and/or accurate. Provide feedback on this result.</div><svg width="24px" height="24px" fill="none" class="sc-bb59ee19-2 dqTSFv you-chat-thumb-up" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M4 13.8231C4 16.2291 5.5568 18.2253 7.47858 18.2253H9.80261C10.7412 18.7095 11.8659 19 13.1173 19H14.0931C14.987 19 15.7542 18.9479 16.2607 18.8212C17.2514 18.5754 17.8696 17.8827 17.8696 17.0037C17.8696 16.825 17.8473 16.6611 17.7952 16.5047C18.2793 16.1397 18.5549 15.6034 18.5549 15.0074C18.5549 14.7244 18.5028 14.4413 18.3985 14.2104C18.7263 13.8752 18.9125 13.3836 18.9125 12.8696C18.9125 12.5345 18.8305 12.1844 18.6816 11.9237C18.8901 11.6406 19.0019 11.2458 19.0019 10.8138C19.0019 9.74115 18.1676 8.89199 17.1024 8.89199H14.4507C14.2868 8.89199 14.175 8.82495 14.1825 8.68343C14.1899 7.92365 15.3743 6.15084 15.3743 4.72067C15.3743 3.72253 14.6741 3 13.7132 3C13.0056 3 12.5289 3.37244 12.067 4.25885C11.203 5.91993 10.1676 7.38734 8.52886 9.39851H7.21043C5.42272 9.39851 4 11.3799 4 13.8231ZM8.18622 13.7784C8.18622 12.2663 8.52886 11.298 9.48231 10.0168C10.5475 8.60149 12.0149 6.89572 13.0801 4.78026C13.3333 4.27374 13.5047 4.15456 13.7505 4.15456C14.041 4.15456 14.2421 4.37058 14.2421 4.74302C14.2421 5.86034 13.0428 7.5959 13.0428 8.71322C13.0428 9.52514 13.7132 10.0317 14.5698 10.0317H17.095C17.5345 10.0317 17.8696 10.3669 17.8696 10.8212C17.8696 11.1415 17.7654 11.3501 17.4972 11.6108C17.3557 11.7523 17.3333 11.9311 17.46 12.0801C17.6834 12.4004 17.7803 12.6089 17.7803 12.8696C17.7803 13.1899 17.6238 13.4655 17.3184 13.6965C17.1248 13.838 17.0428 14.054 17.162 14.2924C17.3259 14.6052 17.4153 14.7542 17.4153 15.0074C17.4153 15.3724 17.1769 15.648 16.6927 15.9013C16.5065 16.0056 16.4618 16.1769 16.5438 16.3482C16.7076 16.7579 16.73 16.825 16.73 16.9963C16.73 17.3315 16.4842 17.5922 15.9851 17.7188C15.568 17.8231 14.905 17.8752 14.0782 17.8603L13.1248 17.8529C10.1825 17.8305 8.18622 16.1695 8.18622 13.7784ZM5.13222 13.8231C5.13222 12.013 6.09311 10.5456 7.17318 10.5307C7.38175 10.5307 7.59032 10.5307 7.79888 10.5307C7.27747 11.514 7.054 12.5419 7.054 13.7635C7.054 15.0819 7.52328 16.2291 8.36499 17.1006C8.05959 17.1006 7.75419 17.1006 7.45624 17.1006C6.21229 17.0857 5.13222 15.6034 5.13222 13.8231Z" fill="#8B8E8F"></path></svg></div><div class="sc-37a97b98-1 jIWNMV sc-bb59ee19-4 cGzDqI"><div class="sc-37a97b98-0 sc-37a97b98-2 kQnxvs fgivYs">This answer is not helpful, accurate, and/or safe. Provide feedback on this result.</div><svg width="24px" height="24px" fill="none" class="sc-bb59ee19-3 ccHXTm you-chat-thumb-down" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M4 13.8231C4 16.2291 5.5568 18.2253 7.47858 18.2253H9.80261C10.7412 18.7095 11.8659 19 13.1173 19H14.0931C14.987 19 15.7542 18.9479 16.2607 18.8212C17.2514 18.5754 17.8696 17.8827 17.8696 17.0037C17.8696 16.825 17.8473 16.6611 17.7952 16.5047C18.2793 16.1397 18.5549 15.6034 18.5549 15.0074C18.5549 14.7244 18.5028 14.4413 18.3985 14.2104C18.7263 13.8752 18.9125 13.3836 18.9125 12.8696C18.9125 12.5345 18.8305 12.1844 18.6816 11.9237C18.8901 11.6406 19.0019 11.2458 19.0019 10.8138C19.0019 9.74115 18.1676 8.89199 17.1024 8.89199H14.4507C14.2868 8.89199 14.175 8.82495 14.1825 8.68343C14.1899 7.92365 15.3743 6.15084 15.3743 4.72067C15.3743 3.72253 14.6741 3 13.7132 3C13.0056 3 12.5289 3.37244 12.067 4.25885C11.203 5.91993 10.1676 7.38734 8.52886 9.39851H7.21043C5.42272 9.39851 4 11.3799 4 13.8231ZM8.18622 13.7784C8.18622 12.2663 8.52886 11.298 9.48231 10.0168C10.5475 8.60149 12.0149 6.89572 13.0801 4.78026C13.3333 4.27374 13.5047 4.15456 13.7505 4.15456C14.041 4.15456 14.2421 4.37058 14.2421 4.74302C14.2421 5.86034 13.0428 7.5959 13.0428 8.71322C13.0428 9.52514 13.7132 10.0317 14.5698 10.0317H17.095C17.5345 10.0317 17.8696 10.3669 17.8696 10.8212C17.8696 11.1415 17.7654 11.3501 17.4972 11.6108C17.3557 11.7523 17.3333 11.9311 17.46 12.0801C17.6834 12.4004 17.7803 12.6089 17.7803 12.8696C17.7803 13.1899 17.6238 13.4655 17.3184 13.6965C17.1248 13.838 17.0428 14.054 17.162 14.2924C17.3259 14.6052 17.4153 14.7542 17.4153 15.0074C17.4153 15.3724 17.1769 15.648 16.6927 15.9013C16.5065 16.0056 16.4618 16.1769 16.5438 16.3482C16.7076 16.7579 16.73 16.825 16.73 16.9963C16.73 17.3315 16.4842 17.5922 15.9851 17.7188C15.568 17.8231 14.905 17.8752 14.0782 17.8603L13.1248 17.8529C10.1825 17.8305 8.18622 16.1695 8.18622 13.7784ZM5.13222 13.8231C5.13222 12.013 6.09311 10.5456 7.17318 10.5307C7.38175 10.5307 7.59032 10.5307 7.79888 10.5307C7.27747 11.514 7.054 12.5419 7.054 13.7635C7.054 15.0819 7.52328 16.2291 8.36499 17.1006C8.05959 17.1006 7.75419 17.1006 7.45624 17.1006C6.21229 17.0857 5.13222 15.6034 5.13222 13.8231Z" fill="#8B8E8F"></path></svg></div>':
                                pra_text = driver.find_element("xpath", '//*[@id="chatHistory"]/div/div[2]/div[1]/p')
                                fpra_text = pra_text.text
                                tts2 = gTTS(f"{fpra_text}", lang='lv')
                                tts2.save("int.mp3")
                                playsound("int.mp3")
                                time.sleep(3)
                                print("gatavs")

                        

                    except:
                        tts = gTTS("Kā es jums vēl varētu palīdzēt?", lang='lv')
                        tts.save("mytext.mp3")
                        os.system("start mytext.mp3")
                        time.sleep(4)

            if any(word in MyText for word in kripto):
                tts = gTTS("Kādas kripto valūtas vērtību Jūs cenšaties noskaidrot?", lang='lv')
                tts.save("mytext.mp3")
                os.system("start mytext.mp3")
                time.sleep(5)
                r1 = sr.Recognizer()
                with sr.Microphone() as source3:
                    r1.adjust_for_ambient_noise(source3, duration=0.2)
                    print("runa!")
                    audio3 = r1.listen(source3)
                    print("raksta")
                    crypto = r1.recognize_google(audio3, language='en')

                    try:
                        print(crypto)
                        tts = gTTS("Tūlīt noskaidrošu tās vērtību, lūdzu uzgaidiet!", lang='lv')
                        tts.save("mytext.mp3")
                        os.system("start mytext.mp3")
                        time.sleep(6)
                        
                        driver = webdriver.Chrome(chrome_options=options)
                        driver.maximize_window()
                        driver.get(f"https://www.google.com/search?q={crypto}+price&rlz=1C1JJTC_enLV1022LV1022&sxsrf=AJOqlzUBPit9yE8oLiDFC6nbDAvP-ldMIg%3A1674420249809&ei=GaDNY86JMe-MrgSYorWIAw&ved=0ahUKEwiO-sbBhdz8AhVvhosKHRhRDTEQ4dUDCA8&uact=5&oq=BTC+price&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIECAAQQzIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIFCAAQgAQyBQgAEIAEOgoIABBHENYEELADOgcIABCwAxBDOhIILhDHARDRAxDIAxCwAxBDGAFKBAhBGABKBAhGGABQqgtYtQ5g8w9oAnABeACAAakBiAGmA5IBAzAuM5gBAKABAcgBC8ABAdoBBAgBGAg&sclient=gws-wiz-serp")
            
                        price = driver.find_element("xpath", '//*[@id="crypto-updatable_2"]/div[3]/div[2]/span[1]')
                        fprice = price.text

                        tts = gTTS(f"Šis kriptovalūtas cena pašlaik ir {fprice} eiro!", lang='lv')
                        tts.save("mytext.mp3")
                        os.system("start mytext.mp3")
                        time.sleep(6)

                        tts = gTTS("Kā es jums vēl varētu palidzēt?", lang='lv')
                        tts.save("mytext.mp3")
                        os.system("start mytext.mp3")
                        time.sleep(5)

                    except:
                        tts = gTTS("Neizdevās atrast tās vērtību, varbūt vēlaties citu, vai mēgināt vēlreiz?", lang='lv')
                        tts.save("mytext.mp3")
                        os.system("start mytext.mp3")
                        time.sleep(8)
   
        except sr.UnknownValueError:
            tts = gTTS("Kā es jums vēl varētu palīdzēt?", lang='lv')
            tts.save("mytext.mp3")
            os.system("start mytext.mp3")
            time.sleep(4)