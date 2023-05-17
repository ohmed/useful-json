import json
# Define the state information
state_data = {
    'name': '',
    'id': '',
    'initials': '',
    'headquarter': '',
    'date_created': '1978-07-01',
    'date_updated': '2018-07-02',
}
# Define a list to store all states
states = []

# Define a function to add a state to the list
def add_state(name, id, initials, headquarter):
    # Create a new state dictionary with the given information
    state = state_data.copy()
    state['name'] = name
    state['id'] = id
    state['initials'] = initials
    state['headquarter'] = headquarter
    # Add the state to the list
    states.append(state)