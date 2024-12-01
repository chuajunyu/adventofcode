from tools import extract_input

input = extract_input(r"input07.txt")


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Folder:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.folders = list()
        self.files = list()

    @property
    def size(self):
        total_size = 0
        for folder in self.folders:
            total_size += folder.size

        for file in self.files:
            total_size += file.size
        return total_size


def build_filesystem(input):
    root = Folder(None, '/')
    curr = root
    for line in input[1:]:
        if '$' in line:
            if 'cd ..' in line:
                curr = curr.parent
            elif 'cd' in line:
                _, _, folder_name = line.split(' ')
                new_folder = Folder(curr, folder_name)
                curr.folders.append(new_folder)
                curr = new_folder
        elif 'dir' not in line:
            file_size, filename = line.split(' ')
            file_size = int(file_size)
            new_file = File(filename, file_size)
            curr.files.append(new_file)
    return root


def find_sum(root, max_size):
    total_size = 0
    if root.size < max_size:
        total_size += root.size
    
    for folder in root.folders:
        total_size += find_sum(folder, max_size)
    
    return total_size


def find_smallest_directory(root, min_size):
    possible_sizes = list()
    if root.size > min_size:
        possible_sizes.append(root.size)
    
    for folder in root.folders:
        smallest = find_smallest_directory(folder, min_size)
        if smallest:
            possible_sizes.append(smallest)

    if possible_sizes:
        return min(possible_sizes)


root = build_filesystem(input)
root_size = root.size

print("Part 1: ", find_sum(root, 100000))
print("Part 2: ", find_smallest_directory(root, 30000000 - (70000000 - root_size)))
