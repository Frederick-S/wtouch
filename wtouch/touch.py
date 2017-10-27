def create_file(file_name):
    try:
        open(file_name, 'x')
    except FileExistsError as e:
        pass
