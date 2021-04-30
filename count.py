file= open("text.txt","r")
data=file.read()
words=data.split()

print("Number of words in a text file :",len(words))