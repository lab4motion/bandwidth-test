import requests
from datetime import datetime

from .utils import convert_to, to_bytes


def start(urls):
    unit = 'KB'
    total_unit = 'MB'

    count = len(urls)
    print(f'Start downloading {count} files.')

    total_size = 0
    start = datetime.now()
    for idx, url in enumerate(urls):
        print(f'{idx}/{count} ... ', end=' ', flush=True)

        response = requests.get(url)
        total_size += len(response.content)

        size = to_bytes(content=response.content, ndigits=2, unit=unit)
        print(f'{size} {unit}')

    end = datetime.now()
    total_size = convert_to(dst=total_unit, src='B', value=total_size)
    total_time = round((end - start).total_seconds(), 2)

    print()
    print(f'Total downloaded data: {total_size} {total_unit}')
    print(f'Total downloading time: {total_time} seconds')
    print()
    print('The bandwidth test is completed successfully.')
