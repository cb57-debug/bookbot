def count_words(file):
    return len(file.split())

def count_characters(file):
    file = file.lower()
    counts = {}
    for c in file:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    return counts

def sort_dict(dict):
    dict.pop(" ")
    dict = sorted(dict.items(), reverse=True, key=lambda items:items[1])
    return dict