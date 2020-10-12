import webbrowser, sys, pyperclip

sys.argv

# Check if commands line arguments were passed.
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()


webbrowser.open('https://www.google.com/maps/places/' + address)
    

