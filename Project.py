import re                                                 # importing the regex library for performing regex operations


def read_file():                                          # creating a function that read the external text file
    file_store = []                                       # creating a tuple to store the output of file
    with open('syslog.txt', 'rt') as file_content:        # opening the source file under the name of file_content
        for characters in file_content:                   # creating a loop to read each characters of file
            file_store.append(characters)                 # updating the file for each character as the loop progress
        return file_store                                 # return the updated tuple with the content of file


def split_words(file_store):                              # making a function to split whole text into individual words
    file_split = re.split("[\\W;.,\\n]", str(file_store))
    ''' The function above splits the whole undivided text into individual words the criteria being if there is a space,
     new line, full stop or a semicolon separate that text into new index'''
    return file_split                                     # returns the array with individual words as it's values


def word_count(word, file_split):                          # function to count no of occurrences of the given word
    count = 0                                              # indicating the no of occurrence of word initially it is 0
    for finding in range(len(file_split)):                 # loop will keep running till the length of array file_split
        if re.fullmatch(word, file_split[finding], re.M | re.I):
            ''' The above "if" will only pass if each and every character of the user input matches with the word 
            in the file_split and this would be repeated for each word in our text file because of the for loop '''
            count += 1                                     # if the word was found count increases by one
    return count                                           # return the total no. of occurrences in file


def line_printing(word, file_split):
    line_count = 0
    k = 1
    word_file = word+'.txt'
    new_file=open(word_file,'a')
    for i in range(len(file_split)):
        if re.fullmatch("n", file_split[i]):
            line_count += 1
            file_split[i] = re.sub('n', '', str(file_split[i]))
        if re.fullmatch(word, file_split[i], re.M | re.I):
            previous_word = file_split[i-1]
            next_word = file_split[i+1]
            current_word = file_split[i]
            new_file.write("Occurrence number {0} was at Line number {1} : {2} {3} {4} \n".format(k, line_count+1, previous_word,
                                                                                   current_word, next_word))
            k += 1
            ''' new_file=open(word_file, 'a') # opening the source file under the name of file_content
            new_file.write(a)
            new_file.close()'''
    new_file.write("Total Number of Occurrence of {0} are : {1}".format(word,word_count(word,file_split)))
    new_file.close()

user_input=int(input())
for i in range(user_input):

    b = input()
    a = read_file()
    c = split_words(a)
    line_printing(b, c)
    word_count(b, c)
