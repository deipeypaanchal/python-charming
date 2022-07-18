'''
-> This program uses a dictionary to encrypt a text file. A dictionary is used for that purpose.
-> This program reads input file, encodes the text using the dictionary, and contents of the file and return the encrypted contents.
-> User is prompted for the name of input and output file.
-> The program runs and gives desired results.
-> The new content is saved in a new file of name of user's choice.
'''

Encrypt_Code = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
 'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
 'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
 'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
 'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
 'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
 'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
 'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
 'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
 '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
 '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
 '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
 ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
 "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
 '{':'[','[':'{','}':']',']':'}'}


file = input("Enter the name of an input file with .txt extension (for example: blah.txt): ")
finalFile = input("Enter the name of an output file with .txt extension (for example: blah.txt): ")

with open(file, "r") as f:
    with open(finalFile, "w") as writeNew:
        for content in f:
            new_content = "".join(str(Encrypt_Code[c]) if c in Encrypt_Code else c for c in content)
            writeNew.write(new_content)
