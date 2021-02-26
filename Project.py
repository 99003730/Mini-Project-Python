"""############################################################################
   AUTHOR           : ARNAV KANDPAL
   PS NO.           : 99003730
   COMPANY          : LTTS, Bangalore
   Date of Creation : 26th February, 2021
   email            : arnav.kandpal@ltts.com
   CONTACT          : 9940791774
   DESCRIPTION      : The program searches for a number of words given as input
                      by the user in a predefined file and gives back the
                      number of time that word was found and each occurrence
                      of it with the line number and previous and next word
                      (A BLANK IN CASE OF LINE END OR LINE START)
    ########################################################################"""
import re       # importing the regex library for performing regex operations


def read_file():       # creating a function that read the external text file
    file_store = []
    '''creating a tuple to store the output of file'''
    with open('syslog.txt', 'rt') as file_content:
        '''opening the source file under the name of file_content'''
        for characters in file_content:
            '''creating a loop to read each characters of file'''
            file_store.append(characters)
            '''updating the file for each character as the loop progress'''
        return file_store  # return updated tuple with the content of file


class SplitWord:
    """A class for splitting the text file into each word so a search could be
       easily implemented"""
    def __init__(self, file_store=0):
        self.file_store = file_store

    def split_words(self, file_store):
        """making a function to split whole text into individual words"""
        self.file_store = file_store
        file_split = re.split("[\\W;.,\\n]", str(self.file_store))
        ''' The function above splits the whole undivided text into
        individual words the criteria being if there is a space,
        new line, full stop or a semicolon separate that text into
         new index'''
        return file_split  # return array with individual words


class WordSearch(SplitWord):
    """Initiating a word search class where our word count function and word
        occurrence function would be implemented, it inherits from SplitWord
        class for invoking the splitting operation from it's object itself"""
    def __init__(self, word='', file_split=0):
        super().__init__()
        self.word = word
        self.file_split = file_split

    def word_count(self, word, file_split):
        """function to count no of occurrences of the given word"""
        self.file_split = file_split
        self.word = word
        count = 0  # indicating the no of occurrence of word initially it is 0
        for finding in range(len(self.file_split)):
            '''loop will keep running till the length of array file_split'''
            if re.fullmatch(self.word, self.file_split[finding], re.M | re.I):
                ''' The above "if" will only pass if each and every character
                of the user input matches with the word in the file_split and
                 this would be repeated for each word in our text file because
                  of the for loop '''
                count += 1      # if the word was found count increases by one
        return count             # return the total no. of occurrences in file

    def line_printing(self, word, file_split):
        """making a func. that will print our values to the .txt files"""
        self.word = word
        self.file_split = file_split
        line_count = 0       # checks the line at which current iteration is at
        occurrence = 1
        '''occurrence of word given 1 because this function will run only when
         there is a occurrence'''
        word_file = self.word+'.txt'
        '''this will give word file name same as the word asked for'''
        new_file = open(word_file, 'a')
        '''opening newly created file under the name of new_file'''
        for find in range(len(self.file_split)):
            '''loop will run till length of array file_split'''
            if re.fullmatch("n", self.file_split[find]):
                line_count += 1
                self.file_split[find] = re.sub("n", ' ', str(self.file_split
                                                             [find]))
            '''The above statement from if will check for the exact single
            character n which i designated for new line as soon as it
            that "n" line_count increases and afterward that n is deleted
               as it is not an actual character of the file rather just a new
                line , so before operating for user input these n's are
                 deleted'''
            if re.fullmatch(self.word, self.file_split[find], re.M | re.I):
                '''matching the exact word in file_split without case'''
                previous_word = self.file_split[find-1]
                """arr[i-1] is the element behind the current one (word)"""
                for search in range(len(self.file_split)):
                    '''The following codes will search for a previous word until
                     the line start is reached, this removes redundancy in if
                    there are special characters such as;  ' " : behind the
                     searched word'''
                    if previous_word == '':
                        previous_word = self.file_split[find-(search+2)]
                    else:
                        break
                next_word = self.file_split[find+1]
                '''arr[i+1] is the element after the current word'''
                for search_two in range(len(self.file_split)):
                    '''The following codes will search for a next word until
                     the line end is reached, this removes redundancy in if
                      there are special characters such as ;  ' " : after the
                       searched word'''
                    if next_word == '':
                        next_word = self.file_split[find+2+search_two]
                    else:
                        break
                current_word = self.file_split[find]
                '''arr[i] is the current word'''
                if next_word != 'n':
                    new_file.write("Occurrence number {0} was at "
                                   "Line number {1} "
                                   ": {2} {3} {4} \n".format(occurrence,
                                                             line_count+1,
                                                             previous_word,
                                                             current_word,
                                                             next_word))
                    '''if the ending word is not 'n' i.e new line
                     print as it is'''

                else:
                    new_file.write("Occurrence number {0} was at"
                                   " Line number {1}"
                                   " : {2} {3} \n".format(occurrence,
                                                          line_count+1,
                                                          previous_word,
                                                          current_word,))

                    '''if the ending word is 'n' i.e new line
                     print nothing at end'''
                ''' Writing into the newly created file no line number ,etc'''
                occurrence += 1                # going onto the next occurrence
        new_file.write("Total Number of Occurrence of the word '{0}' are :"
                       " {1}".format(word, word_search.word_count(self.word,
                                                                  self.
                                                                  file_split)))
        '''above code is to write the total number of counts of the given
         word in the text file and formatted for neatness of code  '''
        new_file.close()                            # close the new text file

    '''///////////////////MAIN PROGRAM STARTS FROM HERE////////////////////'''


try:                                # try and except code for error redundancy
    print("############### WELCOME TO WORD SEARCH PROGRAM ############### \n")
    word_search = WordSearch()
    no_of_words = int(input("Enter the number of words you want to find : \n"))
    '''above code is to take the number of words that are to be found'''
    if no_of_words <= 0:  # if user tries to enter -ve numbers exit
        raise Exception("======================================="
                        "  POSITIVE NUMBERS ONLY PLEASE!!!!  "
                        "============================================")
    print("Remember to enter exact letters words license and licenses"
          " ARE NOT SAME ")
    for finding_words in range(no_of_words):
        '''the loop will run for the number of words to be found'''
        find_words = input("Enter word number {0} you want to find : "
                           .format(finding_words+1))
        '''above code is for taking the word to be found per iteration'''
        for error_search in range(len(find_words)):
            if (find_words[error_search] == '[' or
                    find_words[error_search] == ']' or
                    find_words[error_search] == '(' or
                    find_words[error_search] == ')' or
                    find_words[error_search] == '{' or
                    find_words[error_search] == '}' or
                    find_words[error_search] == '!' or
                    find_words[error_search] == '@' or
                    find_words[error_search] == '#' or
                    find_words[error_search] == '$' or
                    find_words[error_search] == '%' or
                    find_words[error_search] == '^' or
                    find_words[error_search] == '&' or
                    find_words[error_search] == '*' or
                    find_words[error_search] == '_' or
                    find_words[error_search] == '-' or
                    find_words[error_search] == '\\' or
                    find_words[error_search] == ':' or
                    find_words[error_search] == ';' or
                    find_words[error_search] == '|' or
                    find_words[error_search] == ',' or
                    find_words[error_search] == '.' or
                    find_words[error_search] == '`' or
                    find_words[error_search] == '~' or
                    find_words[error_search] == '?' or
                    find_words[error_search] == '<' or
                    find_words[error_search] == '>' or
                    find_words[error_search] == "'" or
                    find_words[error_search] == '"' or
                    find_words[error_search] == '+' or
                    find_words[error_search] == '=' or
                    find_words[error_search] == '/'):
                """If user tries to enter special characters and pass them as words
                throw an exception and exit the program"""
                raise Exception("====================="
                                "  WE DON'T SEARCH FOR BRACKETS OR SPECIAL "
                                "CHARACTERS AS THEY ARE NOT WORDS!!!!  "
                                "===================================")
        base_file = read_file()
        '''calling read file function and storing into base_file'''
        individual_words_tuple = word_search.split_words(base_file)
        '''calling split_words function to split text into words'''
        count_words = word_search.word_count(find_words,
                                             individual_words_tuple)
        '''above function is to call function word_call to count number
         and save it to new variable'''
        if count_words != 0:  # case will not run if there were no words found
            word_search.line_printing(find_words, individual_words_tuple)
            '''calling function for writing the occurrence in file'''
            print('Your word occurrence list was successfully saved at root'
                  ' folder named as "{0}.txt\n"'
                  .format(find_words))
            '''confirmation to user that the code was success'''
        else:
            print("No Words found, So no file was created!\n")
            '''if no matching words were found this would execute'''
except ValueError:                   # if user enter string in place of integer
    print("Oops! you were supposed to enter a number!!!\n")
    '''message to user the committed a value error'''
except IndexError:
    print('Type a word we CANNOT SEARCH FOR "NOTHING"!!!!!\n')
finally:                               # this section will run no matter what
    print("############### THANK YOU FOR USING THE PROGRAM ############## \n")
    '''thank you message'''
'''/////////////////////////////CODE END////////////////////////////////////'''
