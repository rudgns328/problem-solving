def solution(word):
    words = []
    vowels = ["A", "E", "I", "O", "U"]

    def dfs(word):
        if len(word) > 5:
            return
        if word:
            words.append(word)
        for v in vowels:
            dfs(word + v)

    dfs("")
    return words.index(word) + 1
