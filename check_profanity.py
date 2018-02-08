import urllib.request as ur
import urllib.parse as pa

def read_text():
   quotes= open("G:\Python\movie_quotes.txt")
   content=quotes.read()
   print(content)
   quotes.close()
   check_prof(content)

def check_prof(text_to_check):
    url = 'http://www.wdylike.appspot.com/?q='
    q = pa.quote(text_to_check)
    connection = ur.urlopen(url+q)
    output = connection.read().decode()
    print(output)
    connection.close()
    if "true" in output:
        print("Alert!! cursed words found in your document")
    elif "false" in output:
        print("There are no cursed word in your document")

 

read_text()
