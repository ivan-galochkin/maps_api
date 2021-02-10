import requests
import io


def get_map(cords, zoom_level: int = 10, map_type: str = 'map') -> io.BytesIO():
    url = requests.get('https://static-maps.yandex.ru/1.x',
                       params={'ll': f'{cords[0]},{cords[1]}', 'l': map_type, 'z': zoom_level})
    if url.status_code != 200:
        raise ConnectionError(url.reason)
    return io.BytesIO(url.content)


if __name__ == '__main__':
    a = get_map((37.620070, 55.753630), 10)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(a.read())
