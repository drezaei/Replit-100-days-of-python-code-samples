import getpass, random
print("PASSWORD GENERATOR")

def get_word():
    word1=getpass.getpass("Type the first word to form the first half of your password:     ").strip().lower()
    word2=getpass.getpass("Type the second word to form the second half of your password:   ").strip().lower()
    return word1, word2

def get_password():
    dictionary = {
        'a': ['4', '@', '/\\'],
        'e': ['3', '&', '€', 'ë'], 
        'l': ['1', '|', '7', '\\'],
        'o': ['0', '()', 'ø'], 
        't': ['7', 't', '~I~'], 
        's': ['5', 'z', '$'],
    }

    words_combined = word1+word2
    password = ""
    
    for new_word in words_combined:
        if new_word in dictionary:
            substitution = random.choice(dictionary[new_word])
            password += substitution
        else:
            password += new_word
            
    print(f"Your new password is: {password}")
    

    
word1, word2=get_word()
get_password()