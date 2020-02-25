# tutaj wpisz swoje imię i nazwisko


def strip_extensions(files):
    files_names_list = ['.'.join(str(name).split('.')[:1]) for name in files]
    return files_names_list
    # pass


if __name__ == '__main__':
    files = ['spreadsheet.xlsx', 'music.mp3', 'backup.log', None, 'temp', 'archive.tar.gz']

    print(strip_extensions(files))
