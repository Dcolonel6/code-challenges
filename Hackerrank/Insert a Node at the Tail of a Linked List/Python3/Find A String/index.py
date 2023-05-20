# the key here is to maintain two pointers
# the two pointers act as a sliding window and will help us
# get the characters, new_sub_str, in the string that we can compare with the substring
# note new_sub_str must be equal in length with the sub_string

def count_substring(string, sub_string):
    length_substring = len(sub_string)
    length_str = len(string)
    starting_index = 0
    end_index_substring = starting_index + length_substring
    count = 0
    while end_index_substring <= length_str:
        new_sub_str = string[starting_index:end_index_substring] 
        if new_sub_str == sub_string:
            count += 1
        starting_index += 1
        end_index_substring = starting_index + length_substring
    return count