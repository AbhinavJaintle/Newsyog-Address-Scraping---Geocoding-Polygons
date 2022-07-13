import matplotlib.pyplot as plt
import numpy as np
import json
import sys


data_file = open(r'D:\Downloads\pincodeDictionary.json')
pincode_dictionary = json.load(data_file)

a = set()
files = open(r'D:\Documents\codes\Data Science\News Category\outputfile.txt', 'a')
        

for key in pincode_dictionary.keys():
    # print(key)
    for key2 in pincode_dictionary[key].keys():
        a.add(key2)
        
    # print(pincode_dictionary)
print(a, file=files)

files.close()
