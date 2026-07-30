def solution(files):
    
    def make_key(filename):
        i = 0
        while i < len(filename) and not filename[i].isdigit():
            i += 1
        head = filename[:i]

        j = i
        while j < len(filename) and filename[j].isdigit():
            j += 1
        number = filename[i:j]
        
        return (head.lower(), int(number))
        
    return sorted(files, key=make_key)