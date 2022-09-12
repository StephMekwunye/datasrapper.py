import PyPDF2
import csv
import string

def remove_punc(string_pass):
    for ele in string_pass:  
        if ele in string.punctuation:  
            string_pass = string_pass.replace(ele, " ") 
    return string_pass

words = [""]
counter = 0
final_list = [ ["Term","Occurences"] ]

search_file = open("search.txt", "r")
search_lines = search_file.readlines()
search_list = [line.rstrip() for line in search_lines] 

pdffileobj = open('ai.pdf','rb')

pdfreader = PyPDF2.PdfFileReader(pdffileobj)

x = pdfreader.numPages

pageobj = pdfreader.getPage(x-1)

text = pageobj.extractText().lower().replace('\n', ' ')
text = text.replace("  ", " ")
text_list = text.split()

for i in search_list:
    holder = 0
    holder2 = 0
    search_term = str(i).lower()
    search_term = search_term.replace("  ", " ")
    search_list = search_term.split()
    
    if len(search_list) > 1:
        text = remove_punc(text)
        
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
        holder = text.count(search_term)

    result_list = [search_term, holder]

    final_list.append(result_list)
    

with open('ai.csv', 'w') as result_file:
    write = csv.writer(result_file)
    write.writerows(final_list)