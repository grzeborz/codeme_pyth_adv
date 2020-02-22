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


if __name__ == '__main__':
    data = read_json()

    klient = {'imie': 'Antoni', 'numer_telefonu': 123123123}
    data.append(klient)

    write_json(data)
