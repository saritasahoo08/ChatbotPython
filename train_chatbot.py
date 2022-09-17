#perform pre-processing operations on the user input sentence

def clean_up_sentence(sentence,show_details=True): 
    
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    
    if(show_details):
        print("After Tokonize--->",sentence_words)
        
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

sentence = "I am suffering from corona, Whats my daily routine should be?" #Example Sentence
clean_up_sentence(sentence,show_details=True) #Calling Function