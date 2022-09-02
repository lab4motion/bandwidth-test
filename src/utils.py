def urljoin(*args):
    return '/'.join(str(s).strip('/') for s in args if s)


def is_successful(response):
    return response.status_code in [200, 201, 202]


def print_response(response, url):
    print(f'{url} response:')
    try:
        print(json.dumps(response.json(), indent=4))
    except Exception:
        print(f'code: {response.status_code}')


def to_bytes(content, ndigits=2, unit='B'):
    power = {
        'B': 0,
        'KB': 1,
        'MB': 2,
        'GB': 3,
    }[unit]
    return round(len(content) / pow(1024, power), ndigits)


def convert_to(dst, src, value, ndigits=2):
    power = {
        'B': 0,
        'KB': 1,
        'MB': 2,
        'GB': 3,
    }
    return round(value * pow(1024, power[src] - power[dst]), ndigits)
