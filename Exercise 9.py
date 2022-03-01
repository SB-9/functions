def longest_word(string_list):
    longest = ""
    for word in string_list:
        if len(word) > len(longest):
            longest = word
    return longest


words = []
word_ = ""
while word_ != "1":
    word_ = input("add a word to list (1 to end): ")
print(f"{longest_word(words)}")
