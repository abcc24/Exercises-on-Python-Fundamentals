carattere=input("inserire carattere ").lower()
vocali="aeiou"

if carattere in vocali:
    print ("il carattere", carattere, "è una vocale")
else:
    print ("il carattere", carattere, "non è una vocale")