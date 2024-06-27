def tr_lower(text):
    tr_dict = {'I':'ı', 'İ':'i', 'Ç':'ç', 'Ş':'ş', 'Ö':'ö', 'Ü':'ü', 'Ğ':'ğ'}
    for key, value in tr_dict.items():
        text = text.replace(key, value)
    return text.lower()
# • = 0
# – = 1
LetterDict={
    "a":"01",
    "b":"1000",
    "c":"1010",
    "d":"100",
    "e":"0",
    "f":"0010",
    "g":"110",
    "h":"0000",
    "ı":"00",
    "i":"00",
    "j":"0111",
    "k":"101",
    "l":"0100",
    "m":"11",
    "n":"10",
    "o":"111",
    "p":"0110",
    "q":"1101",
    "r":"010",
    "s":"000",
    "t":"1",
    "u":"001",
    "v":"0001",
    "w":"011",
    "x":"1001",
    "y":"1011",
    "z":"1100",
    "ö":"1110",
    "ü":"0011",
    "ç":"10100",
    "ş":"01100",
    "ğ":"11010",
    ".":"010101",
    ",":"110011",
    "?":"001100",
    "-":"100001",
    "/":"10010",
    "0":"11111",
    "1":"01111",
    "2":"00111",
    "3":"00011",
    "4":"00001",
    "5":"00000",
    "6":"10000",
    "7":"11000",
    "8":"11100",
    "9":"11110",
    " ":" ",
    
}

def replaceDict(x,y):
    for i in LetterDict:
        LetterDict[i] = LetterDict[i].replace("0",x).replace("1",y)
        
text="Merhaba dünya"
def translator(text):
    print("wich pair do you prefer ?")
    print("1: 0,1")
    print("2: •,–")
    print("3","special (DIY)")
    selection = int(input("\n>>"))

    if selection <1 or selection>3:
        print("Wrong selection, Retry")
        translator(text)
        
    elif selection==2:
        replaceDict("•","–")
    elif selection==3:
        x = input("Enter first character: ")
        y = input("Enter second character: \n>>")
        replaceDict(x,y)
    text = tr_lower(text)
    translated = ""
    unknown = []
    for i in text:
        if i in LetterDict:
            translated += LetterDict[i]
            translated += " "
        else:
            unknown.append(i)
            translated += "?"
            translated += " "
            
    print(translated)
    if unknown != []:
        print("Unknown characters: ", unknown)
    

translator(text)