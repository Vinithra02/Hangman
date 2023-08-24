#!/usr/bin/env python
# coding: utf-8

# # hangman game
importing 'random' library to select random word from the list
# In[13]:


import random

function which returns the random word
# In[14]:


def wordis(wordlist):
    return random.choice(wordlist)


# ##### Here, I have made 5 different lists (categories). I got these lists from chatGPT.

# In[1]:


animal_words = [
    "elephant",
    "giraffe",
    "lion",
    "tiger",
    "rhinoceros",
    "zebra",
    "kangaroo",
    "koala",
    "panda",
    "hippopotamus",
    "crocodile",
    "gorilla",
    "orangutan",
    "koala",
    "monkey",
    "jaguar",
    "penguin",
    "cheetah",
    "hyena",
]
bird_words = [
    "eagle",
    "sparrow",
    "owl",
    "parrot",
    "swan",
    "dove",
    "pigeon",
    "peacock",
    "hummingbird",
    "woodpecker",
    "pelican",
    "seagull",
    "vulture",
    "kingfisher",
    "ostrich",
    "penguin",
    "flamingo",
    "cuckoo",
]
fruit_words = [
    "apple",
    "banana",
    "orange",
    "grape",
    "strawberry",
    "kiwi",
    "watermelon",
    "pineapple",
    "pear",
    "peach",
    "cherry",
    "mango",
    "blueberry",
    "raspberry",
    "plum",
    "apricot",
    "pomegranate",
    "grapefruit",
    "lemon",
    "lime",
    "fig",
    "blackberry",
    "cranberry",
]
color_words = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "brown",
    "black",
    "white",
    "gray",
    "gold",
    "silver",
    "indigo",
    "violet",
    "magenta",
    "maroon",
    "olive",
    "navy",
    "teal",
    "beige",
    "coral",
    "lavender",
    "salmon",
]
sports_words = [
    "soccer",
    "basketball",
    "baseball",
    "football",
    "tennis",
    "golf",
    "swimming",
    "hockey",
    "volleyball",
    "cricket",
    "rugby",
    "badminton",
    "cycling",
    "wrestling",
    "boxing",
    "skating",
    "skiing",
    "snowboarding",
    "surfing",
    "karate",
    "judo",
    "gymnastics",
    "archery",
    "fencing",
]


# #### Here is where all the magic happens!

# In[16]:


#initialising variable 'play' for the user to choose at the end if they want to continue playing or not.
play='yes'
while(play=='yes'):
    print("Enter the number of the category you want to play ")
    print("1)animals")
    print("2)birds")
    print("3)fruits")
    print("4)colours")
    print("5)sports")

    cat=int(input())  #takes the number associated with the category.
    if cat==1:
        word=wordis(animal_words)
    if cat==2:
        word=wordis(bird_words)
    if cat==3:
        word=wordis(fruit_words)
    if cat==4:
        word=wordis(color_words)
    if cat==5:
        word=wordis(sports_words)
    #print(word)
    n=len(word)
    temp=n
    gussed=[]
    for i in range (0,n):  #creating an empty array to keep track of the guessed letters.
        gussed.append('_')
    count=6  #6 attempts only to guess
    print(*gussed)
    while(count>0 and n>0):
        gusses=input("Enter any letter: ").lower()
        if gusses in word and gusses not in gussed:  #if the input letter is in the word and not gussed already
            for i in range(0,temp):
                if gusses==word[i]:
                    gussed[i]=gusses
                    n=n-1
                else:
                    continue
            print(*gussed)
            print('Correct guess!\n')
        elif gusses in gussed:
            print("Correct guess but already gussed :)\n")
        else:
            count=count-1
            print("Wrong guess! You have ",count," attempts left!\n")
    if(n==0):
        print("-"*20)
        print("You Guessed the word correctly!\n")
    if(count==0):
        print("-"*20)
        print("Your are hanged :(\n")
        print("Correct answer is: \n",word)
    play=input("Do you want to play again?: Type 'yes' or 'no' ").lower()
    print("\n")
print('-'*20)
print("Thankyou for playing!!")
    

