def count_word_frequency(word_list):
    word_freq = {}
    for word in word_list:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(count_word_frequency(words))