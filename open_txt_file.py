#function to open read and store data

def open_txt_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        return file_content
