
Input_Word = input("Enter any word: ")

vowels = ["A","a","E","e","I","i","O","o","U","u"]
numVowels = 0

for i in Input_Word:
    if i in vowels:
        numVowels += len(i)


print("Number of Vowels is: ",numVowels)