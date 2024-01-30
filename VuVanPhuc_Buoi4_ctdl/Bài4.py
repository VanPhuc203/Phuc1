def are_anagrams(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()  

    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    if sorted_word1 == sorted_word2:
        return True
    else:
        return False
word1 = "restful"
word2 = "fluster"
print(are_anagrams(word1, word2))  