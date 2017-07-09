#! /usr/bin/python3
"""
    Goal: Open the Raven poem txt file.

    Referenced: https://docs.python.org/3/howto/unicode.html
"""

inputFile = "raven2.txt" #"C:\\Users\\katar\\Documents\\2017\\computerMusic\\projects\\rhymesToMusic\\test_modules\\sample_input\\raven.txt"
#inputFile = inputFile.encode("utf-8")
encodingType = "IBM500" #ascii utf-8
#with open(file=inputFile, mode='r', encoding=encodingType, errors="surrogateescape") as inputText:
with open(file=inputFile, mode='r', encoding=encodingType) as inputText:
#with open(file=inputFile, mode='r',errors="surrogateescape") as inputText:
#with open(file=inputFile, mode='r') as inputText:




    #print(type(inputText))
    #print(inputText.encoding)
    #print(inputText.readable)
    #print(inputText.newlines)
    read_data = inputText.read()
    rText = read_data.encode(encoding=encodingType, errors="strict")
    print(rText)
