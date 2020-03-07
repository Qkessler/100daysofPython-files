import api


if __name__ == '__main__':
    print('---- TALK PYTHON SEARCH ----')
    search_words = input(f'What keywords to search for? <ENTER WORDS>\n')
    list_words = search_words.split()
    list_titles = api.get_dictionaries(list_words)
    print(f'There are {len(list_titles)} matching episodes:')
    for i, title in enumerate(list_titles, 1):
        print(f'{i}. {title}')
