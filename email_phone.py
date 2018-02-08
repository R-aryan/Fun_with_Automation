import re
import pyperclip as pclip

#to create regex of phone numbers re.verbose is used to reduce th complexity of the regular expressions

phregex= re.compile(r'''(((\d\d\d)|(\(\d\d\d\)))?  #area code (may be optional)
(\s|-)     #first seperator  
\d\d\d - \d\d\d\d # first 3 digits and last four digits 
(((ext(\.)?\s)|x) # extension word part optioanal
(\d{2,5}))?|\d\d\d\d\d\d\d\d\d\d) #extension number part optional
''' , re.VERBOSE)

#email regex i.e checking for the email part

emregex= re.compile(r''' 
[a-zA-Z0-9_.+]+#name part
 @ # symbol part
 [a-zA-Z0-9_.+]+ # domain name part
''' , re.VERBOSE)

#getting text from the clipboard

text=pclip.paste()

#getting phone numbers from the text

phn= phregex.findall(text)

#getting email address from the text

email=emregex.findall(text)

allphone=[]

for ph in phn:
    allphone.append(ph[0])
#print(allphone)
#print(email)

resultant_phoneno= '\n'.join(allphone)+ '\n'+'\n'.join(email)
print('Extracted details from the document are ')
print(resultant_phoneno)

#to copy all the text to the clipboard just uncomment the line below and use ctrl+v to the destination file 
#pclip.copy(resultant_phoneno) 

