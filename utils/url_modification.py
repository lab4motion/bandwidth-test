def optimize_urls(urls, max_dimension, quality):
    return [optimize_url(url, max_dimension, quality) for url in urls]


def optimize_url(url, max_dimension, quality):
    url = remove_existsing_params(url)
    url = add_param(url, 's', max_dimension)
    url = add_param(url, 'l', quality)
    return url


def remove_existsing_params(url):
    return url.split('=')[0]


def add_param(url, key, value):
    separator = '-' if '=' in url else '='
    return url + f'{separator}{key}{value}'
