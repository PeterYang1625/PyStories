# Peter Yang
# ITP 115, Spring 2017
# Assignment 3 Part 1
# Cupcake class
# yangpete@usc.edu
import random

def main():
    """Main code

        Return:
            void: Application container
    """
    goAgain = True
    while goAgain:
        isEnglish = chooseTranslator()
        userInput = input("Please enter what you would like to translate")
        # Translates each word individually by splitting into a list
        wordList = userInput.split()
        # Declare empty list as translated words, will append to later
        translatedList = []
        if isEnglish:
            for word in wordList:
                translatedList.append(englishToPig(word))
        else:
            # Reverse the program and create a Pig Elvish to English translator
            for word in wordList:
                translatedList.append(pigToEnglish(word))
        # Join the individually translated words back into one string
        print(" ".join(translatedList))
        # Asks to go again and goes back up to top of while loop if yes
        goAgain = doGoAgain()
    # Once while loop exits, print an exit message
    print("Thank you for using this program - Peter Yang")

def chooseTranslator():
    """Asks user which translator they want to choose from

        Return:
            True if from English to Pig Elvish
            False if from Pig Elvish to English
    """
    message = "Will you be translating from English or Pig Elvish?"
    validInputs = ["english", "pig elvish"]
    userInput = getValidString(message, validInputs)
    return True if userInput == "english" else False

def pigToEnglish(word):
    """Converts Pig Elvish to an English string
        Will not always accurately translate c's and k's

        Arguments:
            word str: Takes a single word and converts it

        Returns:
            str: Translated word
    """
    # Change all k's to c'
    word = word.replace("c", "k")
    word = word.replace("C", "K")

    # Remove all accents
    word = removeAccents(word)

    # Handle capital letters correctly
    isTitle = word[0].isupper()
    if isTitle:
        # Not using .capitalize() because that would strip any capitals in the middle of the word
        word = word[0].lower() + word[1:]

    # Replace final ë with e
    if word[-1] == "ë":
        word = word[:-1] + "e"

    # Remove "en" but only applicable if original word was len 3 (curr word 5 or less)
    if len(word) <= 5 and word[-2:] == "en":
        word = word[:-2]
    # Remove random vowel at end but only if original word was len 4 or greater (curr word 5 or less)
    elif len(word) >= 5 and word[-1] in "aeiou":
        word = word[:-1]
    else:
        return "[not a valid pig elvish word]"

    # Take last letter and move it to the start of the word
    word = word[-1] + word[:-1]
    if isTitle:
        word = word[0].upper() + word[1:]

    return word

def englishToPig(word):
    """Converts a string to Pig Elvish

        Arguments:
            word str: Takes a single word and converts it

        Returns:
            str: Translated word
    """
    # Take the first letter of the word and move it to the end of the word
    isTitle = word[0].isupper()
    if isTitle:
        # Make the first letter not lower
        # Capitalize the translated first letter at the end
        word = word[0].lower() + word[1:]
    # Bring the first letter to the end
    word = word[1:] + word[:1]

    # If the word is four letters or more, append a random vowel to the end of the word)
    if len(word) >= 4:
        word += random.choice("aeiou")

    # If the word is three letters or fewer, append "en" to the end of the word
    elif len(word) > 0:
        word += "en"
    else:
        pass
        print("pass")

    # Is done out of order to make it easier with handling caps
    # If there is an e at the end of the word, replace it with ë
    if word[-1] == "e":
        word = word[:-1] + "ë"

    # Handle capital letters properly:
    #       If the first letter of the English word is capitalized, make it lower case when you append it to the end
    #       Then capitalize the first letter of the Pig Elvish Word
    if isTitle:
        # Not using .capitalize() because that would strip any capital letters in the middle of a word
        word = word[0].upper() + word[1:]

    # Randomly add accents to vowels using random.random() < 0.5
    word = accentRandomVowels(word)

    # Change all k's to c's
    word = word.replace("k", "c")
    word = word.replace("K", "C")

    return word

def accentRandomVowels(word):
    """Randomly chooses letters - if it's a vowel, add an accent
        Only works on lowercase vowels since upper case vowel accents
        were not provided in the assignment

        Arguments:
            word str: the word to be accented

        Returns:
            str: processed word with accents
    """
    # Cast to list
    letters = list(word)
    newLetters = []
    for letter in letters:
        if letter in "aeiou" and random.random() < 0.5:
            newLetters.append(accentVowel(letter, True))
        else:
            newLetters.append(letter)
    return "".join(newLetters)

def removeAccents(word):
    """Removes all accents from vowels

        Arguments:
            word str: the word to be filtered

        Returns:
            str: processed word without accents
    """
    letters = list(word)
    newLetters = []
    for letter in letters:
        if letter in "áéíóú":
            newLetters.append(accentVowel(letter, False))
        else:
            newLetters.append(letter)
    return "".join(newLetters)

def accentVowel(vowel, isAdd):
    """Adds or remove an accent to a vowel

        Precondition:
            Is a vowel

        Argument:
            vowel str:
            isAdd boolean: True if adding accent False if removing accents

        Returns:
            str: Appropriately filtered vowel
    """
    accentList = {"a" : "á", "e" : "é", "i" :"í", "o" : "ó", "u" : "ú" }
    noAccentList = {"á" : "a", "é" : "e", "í" : "i", "ó" : "o", "ú" : "u"}
    return accentList[vowel] if isAdd else noAccentList[vowel]

def doGoAgain():
    """Asks the user if he/she wants to go again

        Returns:
            boolean: true if yes, false if no
    """
    message = "Would you like to go again?"
    validInputs = ["y", "n"]
    userInput = getValidString(message, validInputs)
    return True if userInput == "y" else False

def getValidString(message, inputs):
    """Gets the user input string that's in the list of possible inputs.
        Not case sensitive.

        Arguments:
            message str: prompt to the user
            inputs arr: list of valid inputs

        Return:
            str: of a user input that is within the inputs
    """
    userInput = input(message + " \n"
                                "Acceptable inputs are [" + ", ".join(inputs) + "]")
    isValid = userInput.lower() in inputs
    while not isValid:
        print("That input is not valid. Please try again. [" + ", ".join(inputs) + "]")
        userInput = input(message + "\n"
                                    "Acceptable inputs are [" + ", ".join(inputs) + "]")
        isValid = userInput.lower() in inputs
    return userInput

# Runs the main code
main()