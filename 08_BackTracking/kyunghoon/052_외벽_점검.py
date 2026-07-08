from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    new_weak = weak + [w + n for w in weak]
    
    def dfs(friends, start):
        count = start
        end = start + length
        for f in friends:
            begin = new_weak[count]
            while count < end and new_weak[count + 1] - begin <= f:
                count += 1
            if count >= end:
                return True
            else:
                count += 1
        return count >= end
    
    for friend_count in range(1, len(dist) + 1):
        for team in permutations(dist, friend_count):
            for start in range(length):
                if dfs(team, start):
                    return friend_count
    
    return -1