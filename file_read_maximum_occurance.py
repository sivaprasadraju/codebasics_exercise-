def most_occured_word(data):
    words = {}

    words_list = data.split()
    for word in words_list:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    maximum_value = max(words.values())
    most_occured_word_list = []
    for word in words.keys():
        if words[word] == maximum_value:
            most_occured_word_list.append(word)
    return most_occured_word_list

def main():
    with open('poem.txt', 'r') as file:
        file_data = file.read()

    word = most_occured_word(file_data)

    print("Most occured word is: ", word)



if __name__ == '__main__':
    main()