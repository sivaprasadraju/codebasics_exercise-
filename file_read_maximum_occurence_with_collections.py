from collections import Counter

def most_occured_word(data):
    words = data.split()
    word_count = Counter(words)
    most_occured = word_count.most_common(1)
    return most_occured[0][0]

def main():

    with open('poem.txt', 'r') as file:
        file_data = file.read()

    word = most_occured_word(file_data)

    print("The maximum occured word is: ", word)


if __name__ == '__main__':
    main()