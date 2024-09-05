import re

#https://www.w3schools.com/python/python_regex.asp

#Find all
txt = "The rain in Spain"
x = re.findall("bi", txt)
print(x)
print("--------------")
txt="The rain in India"
pattern="^The.*India$"
find_all=re.findall(pattern,txt)
print(find_all)
print("find all is above")

pattern="rain"
find_all=re.findall(pattern,txt)
print("find all is: ",find_all)

#search
pattern="rain"
search=re.search(pattern,txt)
if search:
    print("1 Pattern search found:",search.group())

pattern="^The.*India$"
search = re.search(pattern, txt)
if search:
    print("2 Pattern search found:", search.group())
else:
    print("Pattern not found")

pattern = r"India"
search = re.search(pattern, txt)
if search:
    print("3 Pattern search found:", search.group())
else:
    pr=int("Pattern not found")

#match
pattern=r"The"
match = re.match(pattern, txt)
print(match)
if match:
    print("Match found:", match.group())
else:
    print("No match")

pattern=r"rain"
match = re.match(pattern, txt)
print(match)
if match:
    print("Match found:", match.group())
else:
    print("No match")

# replace
pattern=r"India"
replace_p=re.sub(pattern,"Hyd",txt)
print("Replaced string: ",replace_p)

#split
print (" --- split ---")
text = "apple,banana,orange,grape"
pattern = r","
result=re.split(pattern,text)
print(result)

txt = "The rain in Spain"
x = re.search("\s", txt)
print("--------")
print(x.start())
x = re.search(r"\bS\w+", txt)
print(x.string)

#Replace every white-space character with the number 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#replace first two 2 occurences
txt = "The rain in Spain"
x = re.sub("\s", "9", txt,2)
print(x)




