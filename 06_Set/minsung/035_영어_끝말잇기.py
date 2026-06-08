def solution(n, words):
    set_words = set()
    last_word = words[0][0]
    
    for i, word in enumerate(words):
        if word in set_words or word[0] != last_word:
            return [(i % n) + 1, (i // n) + 1]
        set_words.add(word)
        last_word = word[-1]
    return [0, 0]