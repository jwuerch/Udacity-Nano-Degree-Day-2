import os
import urllib

def readText():
    directory = os.getcwd()
    print "Current working directory is " + directory + ".\n"
    quotes = open(directory+"/text_files/movie_quotes.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    checkProfanity(content)

def checkProfanity(textToCheck):
     connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+textToCheck)
     output = connection.read()
     print "\n"
     if output == "true":
         print "Profanity!"
     else:
         print "Safe."
     connection.close()
readText()
