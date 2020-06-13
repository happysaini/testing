import re
import  json

def update_iterator(updating_iterator, current_value):
    #function to increment the iterator
    testdata_file = open("../TestData/TestData.py", 'r')
    testdata = testdata_file.read()
    old_value = updating_iterator +" = "+str(current_value)
    new_value = updating_iterator +" = "+str(current_value+1)
    testdata = re.sub(old_value,new_value, testdata)
    testdata_file = open("../TestData/TestData.py", 'w')
    testdata_file.write(testdata)

