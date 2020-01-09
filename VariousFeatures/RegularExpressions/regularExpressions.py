import re
stre = "Now you can browse privately, and other people who use this device won’t see your activity. However, downloads and bookmarks will be saved."
strf = "In Python, List is a collection data-type which is ordered and changeable. A list can have duplicate entry as well. "

#searech and replace
pattern = r"is"
newstr = re.sub(pattern, "was", strf)
print(newstr)

#search and locate
patter = r"Python"
matcher = re.search(patter, strf)
if matcher:
    print(matcher.group())
    print(matcher.start())
    print(matcher.end())
    print(matcher.span())

#search all
patte = r"and"
print(re.findall(patte, stre))

#match beginning simular
patt = r"Now"
if re.match(patt, stre):
    print("same at the beginning")
