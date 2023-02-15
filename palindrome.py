def palindrome(word):
    wordcheck = True

    #clean up the word by removing any uppercases, commas, spaces, punctuation
    wordclean= word.replace(" ", "").replace(",", "").replace("!","").replace(".","").replace("?","").lower()

    #check for each letter if it matches the other end of the word
    for i in range(round(len(wordclean)/2)):
        if wordclean[i-1] != wordclean[-i]:
            wordcheck= False
            break

    #output the result in a user-friendly message
    if wordcheck:
        print("'{}' is a palindrome".format(word))
    else: 
        print("'{}' is not a palindrome".format(word))


