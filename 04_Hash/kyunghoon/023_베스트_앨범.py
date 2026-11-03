from collections import defaultdict


def solution(genres, plays):
    ans = []
    song = defaultdict(lambda: {"total": 0, "count": {}})

    for i in range(len(genres)):
        song[genres[i]]["count"][i] = plays[i]

    for s in song.values():
        s["total"] = sum(s["count"].values())
        s["count"] = dict(sorted(s["count"].items(), key=lambda x: x[1], reverse=True))

    song = dict(sorted(song.items(), key=lambda x: x[1]["total"], reverse=True))

    for s in song.values():
        ans.extend(list(s["count"])[:2])

    return ans
