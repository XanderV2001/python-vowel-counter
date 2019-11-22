vowels = {'a', 'e', 'o', 'i', 'u'}

print("This program counts the vowels in a word or sentence you enter.")
print("You can also import a .txt file to count vowels.")
txtfile = input("Do you want to get vowels from a file? [y/n]")

count = 0
string = ''

if txtfile == 'y' or txtfile == 'Y':
    print("To count the vowels in your text file, please enter the path to your file.")
    path = input("Path to file: ")
    f = open(path, 'r')
    string = f.read()
elif txtfile == 'n' or txtfile == 'N':
    print("Please enter a word or sentence from wich the program counts the vowels")
    string = input("Enter your word or sentence: ")


for char in string:
    for vowel in vowels:
        if char.lower == vowel.lower:
            count += 1
print("In the word or sentence you entered there were {} vowels found.".format(count))
