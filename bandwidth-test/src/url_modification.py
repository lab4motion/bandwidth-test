def optimize_urls(urls, max_dimension, quality):
    new_list = []
    for url in urls:
        url = remove_existsing_params(url)
        url = add_param(url, 's', max_dimension)
        url = add_param(url, 'l', quality)
        new_list.append(url)
    return new_list


def remove_existsing_params(url):
    return url.split('=')[0]


def add_param(url, key, value):
    separator = '-' if '=' in url else '='
    return url + f'{separator}{key}{value}'
