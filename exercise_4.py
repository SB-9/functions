def starts_with_a(word):
    word_to_check = list(input("What word to check: "))
    if word_to_check[0] == word:
        return "true"
    else:
        return "false"


what_letter_to_check = input("what letter to check: ")
print(f"{starts_with_a(what_letter_to_check)}")
