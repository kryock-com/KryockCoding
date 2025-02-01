def count_letters(text):
    counter = 0
    for i in range(0,len(text)):
        if text[i].isalpha():
            counter += 1
    return counter

def count_words(text):
    counter = 1
    for i in range(0, len(text)):
        if text[i].isspace():
            counter += 1
    return counter

def count_sentences(text):
    counter = 0 
    for i in range(0, len(text)):
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            counter += 1
    return counter

def index(text):
        #assign the function returns to the variables
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    #compute the index
    index = 0.0588 * (100 * letters / words) - 0.296 * (100 * sentences / words) - 15.8

    if index < 0:
        print("Before grade 1\n")
    elif index > 16:
        print("Grade 16+\n")
    else:
        print(f"Grade {round(index)}\n")

def main():
    #user input
    text = input("Enter the text you want to check: \n")
    index(text)

main()