'''
-> This program accepts and reads the text file having .txt extension as input.
-> It converts each word to pig latin and writes the result into another file.
-> We are moving the first letter to the end of word and adding a suffix "ay".
-> User is prompted for the name of input and output file.
-> The program runs and gives desired results.
-> To satisfy our needs, functions such as len(), split(), with open('','r') as x:, readlines() etc are used.
'''

file = input("Enter the name of an input file with .txt extension (for example: blah.txt): ")
finalFile = input("Enter the name of an output file with .txt extension (for example: blah.txt): ")

with open (file, 'r') as f:
    content = f.readlines()
    
for inner_content in content:
    sentences = inner_content.split()
    content2 = []
    
    for words in sentences:
        if len(words) == 1:
            newSentence = words + "ay"
            content2.append(newSentence)

        elif len(words) > 1:
            newSentence = words[1:] + words[0] + "ay"
            content2.append(newSentence)
        
        content3 = " ".join(content2)

    with open(finalFile, 'a') as output:
        output.write(content3)
        output.write("\n")
