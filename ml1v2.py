#This code uses selenium, natural language toolkit(nltk), and webbrowser to generate a random madlib template
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser
import nltk

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://randomwordgenerator.com/paragraph.php") #Browser goes to website

content = driver.find_element(By.CLASS_NAME, "support-paragraph")

with open('madlib_websource.txt', 'w') as web:
    web.write(content.text)


paragraph= content.text

#exclusion words
exclusionwords= ['where', 'when', 'what', 'from', 'could', '''couldn't''', 'would', '''wouldn't''', 'place']

#turning the paragraph into a list of words so that each word has an index
paragraph_list= paragraph.split(' ')

#choosing the words to blank out from the list
mad_lib_list=[]
for i in range(len(paragraph_list)):
    if paragraph_list[i] not in exclusionwords and (i)%3==0 and len(paragraph_list[i]) >3:
        mad_lib_list.append("{}")
    else:
        mad_lib_list.append(paragraph_list[i])

#merging the paragraph back into a single string
madlib= ' '.join(mad_lib_list)

 #outputting the madlib paragraph to a new txt file   
with open('madlib_blank.txt', 'w') as blank:
    blank.write(madlib)
    
webbrowser.open('madlib_blank.txt')


