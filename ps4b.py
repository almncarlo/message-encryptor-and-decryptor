import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    # __init__ is a special method under the object type
    # tells python when you create an object of type 'Message', call this function
    # self is a parameter referring to an instance of the class
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    # defines method functions for the class

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        copy = self.valid_words.copy()
        return copy

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # assert (0 <= shift < 26), 'Shift value must be from 0 to 25 only'
        # initializing new dictionary to determine cipher
        shift_dict = {}
        # initializing strings of upper and lower case alphabet letters
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        # iterate over each character in the given text
        for x in self.message_text:
            # if character is in uppercase
            if x in upper:
                index = upper.find(x)
                total_shift = index + shift
                # if total shift is more than or equal to 26, subtract 26 from it
                # to determine the index of letter it (char in iteration) will be replaced by
                if total_shift >= 26:
                    total_shift -= 26
                # updates the cipher dictionary with char in iteration as key
                # and the new letter as its value
                shift_dict.update({x:upper[total_shift]})
            # if character is in lowercase 
            elif x in lower:
                index = lower.find(x)
                total_shift = index + shift
                if total_shift >= 26:
                    total_shift -= 26
                shift_dict.update({x:lower[total_shift]})
        # returns dictionary of shifted letters
        return shift_dict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shifted_message = ''
        # builds cipher dictionary
        shift_dict = self.build_shift_dict(shift)
        # initialize string of alphabet characters
        # iterates over each character in input word
        for x in self.message_text:
            # if character is in dictionary (a letter), replace it according to the cipher
            if x in shift_dict:
                shifted_message += shift_dict[x]
            # if char is not in dictionary (not a letter), add char to cipher string
            else:
                shifted_message += x
        # return the encrypted message
        return shifted_message


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        # calls the parent class constructor 
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        copy = self.encryption_dict.copy()
        return copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        assert (0 <= shift < 26), 'Shift value must be from 0 to 25 only'
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        cipher_shifts = {}
        # iterates through every possible shift value
        for i in range(0, 26):
            # applies shift to encrypted message
            deciphered = self.apply_shift(i)
            matched_word = []
            # iterates through every word in encrypted message
            for word in deciphered.split():
                # appends booleans to matched word (True or False)
                # if word in iteration is a valid word
                matched_word.append(is_word(self.valid_words, word))
            # adds items to the dictionary
            # keys: i values (shift value used)
            # values: tuples of (shift value, deciphered message)
            cipher_shifts[sum(matched_word)] = (i, deciphered)
        # returns dictionary item with max i value
        # an cipher_shifts key of more than 0 means that the item
        # contains a valid word, we must return the max value 
        # since that is the given definition of the 'best' shift value
        return cipher_shifts.get(max(cipher_shifts))

    # special method allowing the class to print out a string
    def __str__(self):
        return str(self.decrypt_message())
        

if __name__ == '__main__':

    #Example test case (PlaintextMessage)

    plaintext = PlaintextMessage('hello', 2)
    print('TEST CASE for PlaintextMessage')
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    print('------------------')

    #Example test case (CiphertextMessage)

    ciphertext = CiphertextMessage('jgnnq')
    print('TEST CASE for CiphertextMessage')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
    print('------------------')

    #Decoding story.txt, writing best shift value used to decrypt

    # initializes the encrypted story by loading the string
    # to use the functions inside CiphertextMessage class
    story = CiphertextMessage(get_story_string())
    # sets the tuple returned by decrypt_message function
    # to the variables for decoded story and number of shifts
    num_shifts, decoded_story = story.decrypt_message()
    print('The decoded story: \n', decoded_story)
    print()
    print('The best shift value used to decrypt the story:', num_shifts)
   
     
    '''
    DECIPHERED STORY:

    Jack Florey is a mythical character created on the spur of a 
    moment to help cover an insufficiently planned hack. He has 
    been registered for classes at MIT twice before, but has 
    reportedly never passed aclass. It has been the tradition of 
    the residents of East Campus to become Jack Florey for a few 
    nights each year to educate incoming students in the ways, 
    means, and ethics of hacking.'
    '''
