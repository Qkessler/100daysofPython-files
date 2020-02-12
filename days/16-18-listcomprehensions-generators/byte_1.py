NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
	"""Should return a list of title cased names,
      	 each name appears only once"""
	dictionary = list(dict.fromkeys(NAMES))
	return [name.title() for name in dictionary]

def sort_function(name):
	return name[0]

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names_splitted = [name.split() for name in names]
    names_splitted.sort(key=sort_function)
    names_joined = [" ".join(name) for name in names_splitted]
    return names_joined

def sort_length(name):
	return len(name[0])

def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    names_splitted = [name.split() for name in names]
    names_splitted.sort(key=sort_length)
    names_sorted = [" ".join(name) for name in names_splitted]
    return names_sorted[0]
    

print(dedup_and_title_case_names(NAMES))
print(sort_by_surname_desc(NAMES))
print(shortest_first_name(NAMES))
