def reduce_file_path(path):
    parts = path.split('/')
    current_path = []
    for part in parts:
        if not part or part == '.':
            continue
        elif part == '..':
            if current_path:
                current_path.pop()
        else:
            current_path.append(part)
    return '/' + '/'.join(current_path)

if __name__ == "__main__":
    path = str(input())
    print(reduce_file_path(path))