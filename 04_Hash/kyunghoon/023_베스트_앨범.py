from collections import defaultdict


def solution(genres, plays):
    answer = []
    d = defaultdict(lambda: {"total": 0})
    for i, g in enumerate(genres):
        if g not in d:
            d[g] = {"total": 0}
        d[g]["total"] += plays[i]
        d[g][i] = plays[i]

    sorted_genres = sorted(d, key=lambda x: d[x]["total"], reverse=True)

    for g in sorted_genres:
        sorted_songs = sorted(
            {k: v for k, v in d[g].items() if k != "total"}.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        for idx, (song_idx, _) in enumerate(sorted_songs):
            if idx == 2:
                break
            answer.append(song_idx)

    return answer
