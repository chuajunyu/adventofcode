
def extract_input(filename):
    """
    Reads a text file into a list of strings, where each string corresponds
    to a line in the text file.

    Removes the trailing newline at the end of each string.
    """
    with open(filename) as file:
        input = file.readlines()

    # To remove the newline    
    for i in range(len(input)):
        input[i] = input[i].strip('\n')
    
    return input


def convert_map_dict(input):
    """
    Converts a nested list map into a dictionary
    With key value pairs of tuple coordinates to int values
    """
    map_dict = {}
    for y, row in enumerate(input):
        for x, value in enumerate(row):
            map_dict[(x, y)] = int(value)
    return map_dict 
    