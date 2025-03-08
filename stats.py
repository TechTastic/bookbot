def get_word_count(book):
    return len(book.split())

def get_unique_character_counts(book):
    counts = {}

    for char in book:
        lowered_char = char.lower()
        if lowered_char in counts:
            counts[lowered_char] += 1
        else:
            counts[lowered_char] = 1
    
    return counts

def split_and_sort_character_counts(counts):
    count_list = []
    for char, count in counts.items():
        count_list.append({
            "char": char,
            "count": count
        })
    
    count_list.sort(reverse=True,key=lambda dict: dict["count"])
    return count_list