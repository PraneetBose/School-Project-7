# Python3 Program to
# check if a given character is a vowel or consonant.

# storing the albhabet in the varialble letter
letter = input("Enter any letter: ")
letter = letter.lower()
# adding if-elif-else statements to find , whether the the alphabet is a vovel or a consonant
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print("Letter is a vowel ")

else:
    print("Letter is a consonant ")
