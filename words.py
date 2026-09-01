def lower_case_words(words):
    for i in range(len(words)):
        yield words[i].lower()
        i+=1

x=lower_case_words(["Hello", "world"])
for word in x:
    print(word)