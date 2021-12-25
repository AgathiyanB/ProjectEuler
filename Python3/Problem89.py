value = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,None:10000}
groupings = {1:"A",2:"AA",3:"AAA",4:"AB",5:"B",6:"BA",7:"BAA",8:"BAAA",9:"AZ"}
correspondence = [{"A":"I","B":"V","Z":"X"},{"A":"X","B":"L","Z":"C"},{"A":"C","B":"D","Z":"M"},{"A":"M","B":"MMM"}]
def roman_to_number(x):
    total = 0
    subtractive = None
    for digit in x:
        if value[subtractive] < value[digit]:
            total += (value[digit]-(2*value[subtractive]))
            subtractive == None
        else:
            total += value[digit]
            subtractive = digit
    return total

def number_to_roman(y):
    letters = []
    for digit in range(0,len(y)):
        if y[digit] != "0":
            dictionary = correspondence[len(y)-1-digit]
            for item in groupings[int(y[digit])]:
                letters.append(dictionary[item])
    return "".join(letters)
            
        
        

with open("roman.txt","r") as database:
    TotalChar = 0
    for numberwithline in database:
        number1 = numberwithline[0:-1]
        base10 = roman_to_number(number1)   
        number2 = number_to_roman(str(base10))
        TotalChar += len(number1) - len(number2)
print(TotalChar)
        
        
        
        
            
