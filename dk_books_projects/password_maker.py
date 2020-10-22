import random
import string

print("welcome to password picker")

while True:

    adjectives = ['sleepy', 'slow', 'smelly',
     'wet', 'fat', 'red',
     'orange', 'yellow', 'green',
     'blue', 'purple', 'fluffy',
     'white', 'proud', 'brave']
    
    nouns = ['apple', 'dinosaur', 'ball',
     'toaster', 'goat', 'dragon',
     'hammer', 'duck', 'panda']
    
    random_words = ["dumpling","unity","netflix","color","Bryson","billgates",
         "hallo","mumbo","iskall","grian","until","brother","eclipes",
         "boy"]
    
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    random_word = random.choice(random_words)
    
    
    number = random.randrange(0,200)
    special_char = random.choice(string.punctuation)


    password = adjective + noun + str(number) + random_word + special_char
    print("Your new password is : %s"% password) 
    
    response = input("\nWould you like another password? Type y or n: ")
    
    if response == "n":
        break