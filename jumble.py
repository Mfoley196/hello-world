print ("Hello, world!")

x = input("How are you? ")

if " " not in x:
    print ("What a brief response...")
else:
    words = x.split()
    for word in words:
        for letter in word:
            print(chr(ord(letter)+1),end="")
        print()    
        