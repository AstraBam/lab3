def from_string_to_list(string, container):
    container.extend(map(int, string.split()))
