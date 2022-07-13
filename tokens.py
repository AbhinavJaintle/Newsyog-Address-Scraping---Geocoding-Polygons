import spacy
from collections import Counter
import json


nlp = spacy.load("en_core_web_sm")

data_file = open(r'D:\Downloads\pincodeDictionary.json')
pincode_dictionary = json.load(data_file)

dict = {}


def get_tokens(doc):

    arr = [""]*20
    count=0
    for token in doc:
      if token.text!="Jaipur"and token.text!="Rajasthan":
        if token.text==","or token.text=="-":   
            count+=1
        else:
            arr[count]+=" "+token.text
      else:
        count-=1

    
    pincode = arr[count]
    
    
    index = str(pincode)
    
    
    count-=1
    while count>0:
#   if arr[count]!=" 560038"or arr[count]!=" Bangalore" :
     try:
        dict[index].append(arr[count])
        count-=1
     except:
        dict[index] = []
        dict[index].append(arr[count])
        count-=1
    return(dict)



for line in pincode_dictionary:
    doc = nlp(line)
    get_tokens(doc)
    
print(dict)