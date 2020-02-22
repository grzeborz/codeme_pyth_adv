import json


def read_json():
    try:
        file = open('data.json', mode='r')
        data = json.load(file)
        file.close()
        return data
    except FileNotFoundError:
        return []


def write_json(data):
    file = open('data.json', mode='w')
    json.dump(data, file)
    file.close()


class JSONData:
    def __enter__(self):
        return read_json()

    def __exit__(self, *args):
        pass


if __name__ == '__main__':
    with JSONData() as data:
        klient = {'imie': 'Antoni', 'numer_telefonu': 123123123}
        data.append(klient)

        write_json(data)
