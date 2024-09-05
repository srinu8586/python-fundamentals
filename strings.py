#String concatination
str1="Sri"
str2="nath"
str3=str1+str2 #concating two string
print(str3)
print("String concatination: "+ str1+str2)
print("Lenght of the str3 string:",len(str3))
print("Upper case:"+str1.upper())
print("Lower case: "+str2.lower())

#String replace
print("Replace string: "+str3.replace("nath"," Ponnam"))

#split a string
text=" Python scripting Learning "
print("Before split:"+text+":")
print("After split:", text.split())

#Stripping
print("strip:"+text.strip()+":")

#substring
substr="scri"
if substr in text:
    print("Substring "+"'"+substr+"'"+" is identified in:"+text)
else:
    print("Substring "+"'"+substr+"'"+" is not identified in:"+text)
