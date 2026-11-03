from collections import defaultdict


def solution(genres, plays):
    ans = []
    song = defaultdict(lambda: {"total": 0, "count": {}})

    for i in range(len(genres)):
        song[genres[i]]["total"] += plays[i]
        song[genres[i]]["count"][i] = plays[i]

    for s in sorted(song.values(), key=lambda x: x["total"], reverse=True):
        top = sorted(s["count"], key=s["count"].get, reverse=True)
        ans.extend(top[:2])

    return ans
