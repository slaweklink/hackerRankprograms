def count_substring(string, sub_string):
    return sum(string[start:].startswith(sub_string) for start in range(len(string)))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


