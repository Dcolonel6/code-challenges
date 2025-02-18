def first_dup(s):
    '''
    Your code here
    '''
    tracker = {}
    indices = []

    for index, letter in enumerate(s):
        if letter in tracker:
            indices.append(tracker[letter])
        else:
            tracker[letter] = index

    return s[min(indices)] if indices else None


if __name__ == "__main__":
    print(first_dup("bar"))