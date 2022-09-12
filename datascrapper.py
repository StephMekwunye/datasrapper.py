from bs4 import BeautifulSoup
import requests
import csv
import re
import string

def remove_punc(string_pass):
    for ele in string_pass:  
        if ele in string.punctuation:  
            string_pass = string_pass.replace(ele, "") 
    return string_pass

def remove_punc_words(words):
    loop = 0
    while loop < len(words):
        words[loop] = remove_punc(words[loop])
        loop += 1

words = [""]
final_list = [ ["url","Term","Occurrences"] ]

url_file = open("url.txt", "r")
url_lines = url_file.readlines()
url_list = [line.rstrip() for line in url_lines]

search_file = open("search.txt", "r")
search_lines = search_file.readlines()
search_list = [line.rstrip() for line in search_lines]

for i in url_list:
    url = str(i)
    result = requests.get(url)
    doc = BeautifulSoup(result.text.lower(), "html.parser")
    
    for x in search_list:
        holder = 0
        search_term = str(x).lower()
        
        return_value = doc.findAll(text = re.compile((str(search_term))))
        
        for i in return_value:
            words = i.lower().split()
            
            if len(search_term) > 1:
                remove_punc_words(words)
                matches = True
                
                for i in range(len(search_list)):
                    if words.count(search_list[i]) == 1:
                        matches == True
                    else:
                        matches == False
                            
                if matches == True:
                            holder += 1
                else:
                    pass
            else:
                remove_punc_words(words)
                    
                holder += words.count(search_term)
            
        result_list = [url, search_term, holder]
        
        final_list.append(result_list)
        

with open('results.csv', 'w') as result_file:
    write = csv.writer(result_file)
    write.writerows(final_list)