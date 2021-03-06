us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ',
                   'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
                   'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL',
                   'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
                   'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                   'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                   'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
                   'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                   'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
                   'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                   'New Mexico': 'NM', 'New York': 'NY',
                   'North Carolina': 'NC', 'North Dakota': 'ND',
                   'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
                   'Pennsylvania': 'PA', 'Rhode Island': 'RI',
                   'South Carolina': 'SC', 'South Dakota': 'SD',
                   'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
                   'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                   'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

states = ['Oklahoma', 'Kansas', 'North Carolina', 'Georgia', 'Oregon',
          'Mississippi', 'Minnesota', 'Colorado', 'Alabama',
          'Massachusetts', 'Arizona', 'Connecticut', 'Montana',
          'West Virginia', 'Nebraska', 'New York', 'Nevada', 'Idaho',
          'New Jersey', 'Missouri', 'South Carolina', 'Pennsylvania',
          'Rhode Island', 'New Mexico', 'Alaska', 'New Hampshire',
          'Tennessee', 'Washington', 'Indiana', 'Hawaii', 'Kentucky',
          'Virginia', 'Ohio', 'Wisconsin', 'Maryland', 'Florida',
          'Utah', 'Maine', 'California', 'Vermont', 'Arkansas', 'Wyoming',
          'Louisiana', 'North Dakota', 'South Dakota', 'Texas',
          'Illinois', 'Iowa', 'Michigan', 'Delaware']

NOT_FOUND = 'N/A'


def get_every_nth_state(states=states, n=10):
    """Return a list with every nth item (default argument n=10, so every
       10th item) of the states list above (remember: lists keep order)"""
    nth_states = []
    counter = 0
    for state in states:
        if counter == n-1:
            counter = 0
            nth_states.append(state)
        else:
            counter += 1
    return nth_states


def get_state_abbrev(state_name, us_state_abbrev=us_state_abbrev):
    """Look up a state abbreviation by querying the us_state_abbrev
       dict by full state name, for instance 'Alabama' returns 'AL',
       'Illinois' returns 'IL'.
       If the state is not in the dict, return 'N/A' which we stored
       in the NOT_FOUND constant (takeaway: dicts are great for lookups)"""
    if state_name not in us_state_abbrev.keys():
        return NOT_FOUND
    else:
        return us_state_abbrev[state_name]


def get_longest_state(data):
    """Receives data, which can be the us_state_abbrev dict or the states
       list (see above). It returns the longest state measured by the length
       of the string"""
    if data == us_state_abbrev:
        max_length = -1
        max_state = ''
        for d in data.keys():
            if len(d) > max_length:
                max_length = len(d)
                max_state = d
        return max_state
    elif data == states:
        max_length = -1
        max_state = ''
        for d in data:
            if len(d) > max_length:
                max_length = len(d)
                max_state = d
        return max_state
    else:
        return None


def combine_state_names_and_abbreviations(us_state_abbrev=us_state_abbrev,
                                          states=states):
    """Get the first 10 state abbreviations ('AL', 'AK', 'AZ', ...) from
       the us_state_abbrev dict, and the last 10 states from the states
       list (see above) and combine them into a new list. The resulting list
       has both sorted, so:
       ['AK', 'AL', 'AZ', ..., 'South Dakota', 'Tennessee', 'Texas', ...]
       (see also test_combine_state_names_and_abbreviations)"""
    list_combined = []
    states.sort()
    abbrev_unsorted = us_state_abbrev.values()
    abbrev_sorted = sorted(abbrev_unsorted)
    pointer = 0
    for abbrev in abbrev_sorted:
        if pointer == 10:
            break
        else:
            list_combined.append(abbrev)
        pointer += 1
    for state in range(len(states) - 10,  len(states), 1):
        list_combined.append(states[state])
    return list_combined


# print(get_every_nth_state(states, 20))
# print(get_state_abbrev('bogus'))
# print(get_longest_state(us_state_abbrev))
expected = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
            'South Dakota', 'Tennessee', 'Texas', 'Utah',
            'Vermont', 'Virginia', 'Washington', 'West Virginia',
            'Wisconsin', 'Wyoming']
print(combine_state_names_and_abbreviations() == expected)
print(combine_state_names_and_abbreviations())
