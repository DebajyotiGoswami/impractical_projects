'''
program that takes a sentence as input and returns a bar chart type
count of characters from the sentence
'''
import pprint

def show_chart(chart):
    '''
    print the dictionary of character wise count as a bar chart
    attribute -- dictionary
    return -- None
    '''
    for key, value in chart.items():
        chart[key] = list(key * value)

    pprint.pprint(chart)

def create_chart(sentence):
    '''
    takes an strings as input and returns a character wise count
    attribute -- strings
    return -- dictionary
    '''
    letters = list('abcdefghijklmnopqrstuvwxyz')
    chart = {}

    for character in sentence:
        character = character.lower()
        if character in letters:
            chart.setdefault(character, 0)
            chart[character] += 1

    return chart

def main():
    '''
    main function. our program starts here
    '''
    sentence = input("Enter your sentence : ")
    chart = create_chart(sentence)
    show_chart(chart)

if __name__ == '__main__':
    main()
