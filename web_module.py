import webbrowser,sys
import pyperclip as pc

sys.argv
#check if cmd arguments are passed

if len(sys.argv)>1:
    address= ' '.join(sys.argv[1:])

else:
    address= pc.paste()

webbrowser.open('https://www.google.co.in/maps/place/'+address)


