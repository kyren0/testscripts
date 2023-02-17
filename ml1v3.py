#This code uses selenium, natural language toolkit(nltk), and webbrowser to generate a random madlib template
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser
import nltk

#Variable setup for selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

#Sending browser to website
driver.get("https://randomwordgenerator.com/paragraph.php") 

#grabbing the random paragraph that the website gives us as 'content'
content = driver.find_element(By.CLASS_NAME, "support-paragraph")

#outputting our paragraph to a txt to save it externally
with open('madlib_websource.txt', 'w') as web:
    web.write(content.text)

#saving random paragraph in string format
paragraph= content.text

#closing selenium so that it doesn't interfere with next steps
driver.quit()

#defining sentence part codes for nltb
usable_CODES = {
    'VB',   # Vrb, base
    'VBD',  # Vrb, past
    'VBG',  # Vrb, -ing
    'VBN',  # Vrb, past participle
    'VBP',  # Vrb, non-3rd person singular present
    'VBZ',  # Vrb, 3rd person singular present
    'NN',   # Noun, singular
    'NNS',  # Noun, plural
    'NNP'   # Proper Noun, singular
    'NNPS', # Proper Noun, plural
    'JJ',   # Adj
    'JJS',  # Adj, superlative
    'JJR',  # Adj, comparative
    'CD',   # Number
    'RB',   #Adv
    'RBS',  #Adv, superlative
    'RBR',  #Adv, comparative
}


#turning the paragraph into a list of words so that each word has an index
paragraph_list= paragraph.split(' ')

#tagging each word in paragraph for sentence structure
paragraph_tagged = nltk.pos_tag(paragraph_list)

#choosing the words to replace from the list and asking the user to replace them
mad_lib_list=[]

for i in range(len(paragraph_list)):
    if paragraph_tagged[i][1] in usable_CODES and (i)%3==0:
        if paragraph_tagged[i][1] == 'VB' or paragraph_tagged[i][1] == 'VBP':
            mad_lib_list.append(str(input("verb?")))
        elif paragraph_tagged[i][1] == 'VBD' or paragraph_tagged[i][1] =='VBN':
            mad_lib_list.append(str(input("verb (past)?")))
        elif paragraph_tagged[i][1] == 'VBG':
            mad_lib_list.append(str(input("verb (-ing)?")))
        elif paragraph_tagged[i][1] == 'VBZ':
            mad_lib_list.append(str(input("verb (-s)?")))
        elif paragraph_tagged[i][1] == 'NNS' or paragraph_tagged[i][1] =='NNP':
            mad_lib_list.append(str(input("noun?")))
        elif paragraph_tagged[i][1] == 'NNS' or paragraph_tagged[i][1] =='NNPS':
            mad_lib_list.append(str(input("noun (plural)?")))
        elif paragraph_tagged[i][1] == 'JJ' or paragraph_tagged[i][1] =='JJS' or paragraph_tagged[i][1] =='JJR':
            mad_lib_list.append(str(input("Adjective?")))
        elif paragraph_tagged[i][1] == 'RB' or paragraph_tagged[i][1] =='RBS' or paragraph_tagged[i][1] =='RBR':
            mad_lib_list.append(str(input("Adverb?")))
        elif paragraph_tagged[i][1] == 'CD':
            mad_lib_list.append(str(input("number?")))

    else:
        mad_lib_list.append(paragraph_list[i])

#merging the paragraph back into a single string
madlib= ' '.join(mad_lib_list)

 #outputting the madlib paragraph to a new txt file   
with open('madlib_filled.txt', 'w') as blank:
    blank.write(madlib)
    
webbrowser.open('madlib_filled.txt')


