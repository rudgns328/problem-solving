def solution(genres, plays):
    answer = []
    genre_total = {}
    genre_songs = {}

    for genre, play in zip(genres, plays):
        genre_total[genre] = genre_total.get(genre, 0) + play

    for i in range(len(genres)):
        if genres[i] not in genre_songs:
            genre_songs[genres[i]] = []
        genre_songs[genres[i]].append([plays[i], i])

    genre_order = list(genre_total.items())
    genre_order.sort(key=lambda x: -x[1])

    for genre, total in genre_order:
        sorted_songs = list(genre_songs[genre])
        sorted_songs.sort(key=lambda x: (-x[0], x[1]))

        for play, idx in sorted_songs[:2]:
            answer.append(idx)

    return answer
