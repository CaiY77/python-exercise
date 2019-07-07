for i in range (10):
    print(i)

# prints every 2nd letter
mess = "This is a string"
for c in range(0, len(mess), 2):
    print(mess[c])

# does cipher left shift

mess = "This is a random Message"
newmessage=""
for c in mess:
    offset=ord(c)-ord("a")+25
    wrap=offset%26
    newchar=chr(ord("a")+wrap)
    newmessage =newmessage+newchar
print("Your new Message: ", newmessage)
