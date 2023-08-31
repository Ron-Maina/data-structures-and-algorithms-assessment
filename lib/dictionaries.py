import string

def word_frequency(sentence):

    dict = {}
    for character in sentence:
        if character in string.punctuation:
            str = sentence.replace(character, '')
   
    result = str.split()
    for word in result:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict
        
