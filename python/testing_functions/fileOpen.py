#! /usr/bin/python
"""
    Goal: Open the Raven poem txt file.

    Referenced: https://docs.python.org/3/howto/unicode.html
"""

inputFile = "raven.txt" #"C:\\Users\\katar\\Documents\\2017\\computerMusic\\projects\\rhymesToMusic\\test_modules\\sample_input\\raven.txt"
#inputFile = inputFile.encode("utf-8")
encodingType = "IBM500" #ascii utf-8
with open(file=inputFile, mode='r', encoding=encodingType) as inputText:
#with open(file=inputFile, mode='r') as inputText:

    toBytes = inputText.encode()
    print(type(toBytes))
    print(toBytes)
    #read_data = inputText.read()
    #print(read_data)
    #print(type(read_data))
    #print(read_data.encode(encodingType))
    print(type(inputText))
    print(inputText.readline())
    print(inputText.readline())
