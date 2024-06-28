def tr_lower(text):
    tr_dict = {'I':'ı', 'İ':'i', 'Ç':'ç', 'Ş':'ş', 'Ö':'ö', 'Ü':'ü', 'Ğ':'ğ'}
    for key, value in tr_dict.items():
        text = text.replace(key, value)
    return text.lower()

# • = 0
# – = 1
LetterDict = {
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
mors = ['11', '0', '010', '0000', '01', '1000', '01', '100', '0011', '10', '1011', '01']

def decode_to_text(text):
    text = ""
    unknown = []
    for i in mors:
        for key in LetterDict:
            if LetterDict[key] == i:
                text += key
            else:
                unknown.append(i)
                text += "?"
                text += " "
    return [text,unknown]



def change_format(x,y):#–,• = 0,1 || x,y etc.
    for i in LetterDict:
        LetterDict[i] = LetterDict[i].replace("0",x).replace("1",y)
        
text = "Merhaba dünya"
def text_to_mors(text):
    print("wich pair do you prefer ?")
    print("1: 0,1")
    print("2: •,–")
    print("3","special")
    selection = int(input("\n>>"))

    if selection <1 or selection>3:
        print("Wrong selection, Retry")
        text_to_mors(text)
        
    elif selection == 2:
        change_format("•","–")
    elif selection == 3:
        x = input("Enter first character (•): ")
        y = input("Enter second character (–): \n>>")
        change_format(x,y)
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
    
def mors_to_text():
    mors = input("Type mors text here:\n>>")
    x = input("First variable:")
    y = input("Second variable:")
    change_format("0","1")
    change_format(x,y)
    mors = mors.split(" ")
    
    output = decode_to_text(mors)
    translated = output[0]
    unknown = output[1]
    
            
    print(translated)
    if unknown != []:
        print("Unknown characters: ", unknown)



def operations():
    selection = int(input("select the operation you want\n1. Text to mors\n2. Mors to text\n>> "))
    if selection == 1:
        text_to_mors(text)#encrypt
    elif selection == 2:
        mors_to_text()#decode

    else:
        print("invalid selection")
        operations
    continueOp = input("do you want to do another operation ?\n1. Yes\n>> ")
    if continueOp in ["Yes","yes","1"]:
        operations()
    else:
        pass
    
operations()

#uncomplated
