#input for the string which is gonna be reversed
string=input("Give ur string to be reversed:")

string2=("")
for i in string:
    string2 = i+string2

print("\n your string:", string)
print("its reversed:", string2)
