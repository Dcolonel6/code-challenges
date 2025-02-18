from collections import Counter


def duplicate_count(text):
    # Your code goes here
    lower_text = text.lower()
    freq_counter = Counter(lower_text)

    filter_object = [k for k in freq_counter if freq_counter[k] > 1]

    return len(filter_object)


if __name__ == "__main__":
    print(duplicate_count("dennis"))