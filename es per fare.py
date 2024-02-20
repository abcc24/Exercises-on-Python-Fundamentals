carattere=input("inserire carattere ").lower()
vocali="aeiou"

if carattere in vocali:
    print (f"il carattere" '{carattere}' "è una vocale")
else:
    print (f"il carattere" '{carattere}' "non è una vocale")