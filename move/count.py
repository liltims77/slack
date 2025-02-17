def freq(string, passedkey):
    words = []
    words = string.split()


    Dict = {}
    for key in words:
        if (key == passedkey):
            Dict[key] = words.count(key)
    print("Total count:", Dict)

    print(words)

freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go","lamb")   

# def freq(strings, passedkey):
#     words = strings.split()  # Split the string into words

#     count = words.count(passedkey)
#     print("Total count:", {passedkey: count})
#     print(words)

# freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
# Everywhere that Mary went The lamb was sure to go", "lamb")



