def print_upper_words(words):
    '''Take in array of words and loops through to uppercase each string'''
    for word in words:
        print(word.upper())

def only_letter_e(words):
    ''' function prints words that start with the letter "e" - either upper or lower case'''

    for word in words:
      # if(word[0] == "e" or "E"):
      if word.startwith("e") or word.startwith("E"):
        print(word.upper())
      else:
        print("Sorry, your letter must begin with the letter e")


def must_start_with_func(words, words_start_with):
    '''Pass in a set of letters (arguments) and the function will only print out words that start with one of those lettters'''

    for word in words:
      for letter in wowords_start_with: 
        print(word.upper())

