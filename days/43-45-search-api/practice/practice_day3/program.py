import api
import webbrowser

if __name__ == '__main__':
    print('---- TALK PYTHON SEARCH ----')
    search_words = input(f'What keywords to search for? <ENTER WORDS>\n')
    list_words = search_words.split()
    list_searches = api.get_searches(list_words)
    print(f'There are {len(list_searches)} matching episodes:')
    for i, search in enumerate(list_searches, 1):
        print(f'{i}. {search.title}')
    print()
    num = input(f'Which one would you like to watch in the browser? <NUMBER>\n')
    print()
    if int(num) - 1 <= len(list_searches) and int(num) - 1 > 0:
        base_url = 'https://talkpython.fm'
        search_url = list_searches[int(num) - 1].url
        full_url = "".join([base_url, search_url])
        print(f'{num}. {full_url}')
        webbrowser.open(full_url, new=2) 
    else:
        print(f'ERROR> The number must be in range.')
        exit(1)
    
    

        
