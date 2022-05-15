'''
program to generate pigLatin equivalent of a user input sentence

if the first letter of each word is consonant :
    move that consonant to the end
    and then add "ay" to the end of the word

if the first letter of each word is vowel:
    simply add "way" to the end of the word
'''
import sys

def pigLatin(sentence):
    '''
    convert a sentence to its pigLatin counterpart
    parameter -- string
    return -- string
    '''
    words = sentence.split()
    pig_latin = ''
    for word in words:
        if word[0].lower() in list('aeiou'):
            pig_latin += word + 'way'
        else:
            pig_latin += word[1:] + word[0]+ 'ay'
        pig_latin += ' '
    return pig_latin

def main():
    '''
    main function. program starts here
    '''
    sentence = input("Enter your sentence : ")
    pig_latin = pigLatin(sentence)
    print(pig_latin, file=sys.stderr)

if __name__ == '__main__':
    main()
