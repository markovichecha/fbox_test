import re

pattern = re.compile(
    r'^(?:[a-z0-9]'
    r'(?:[a-z0-9-_]{0,61}[a-z0-9])?\.)'
    r'+[a-z0-9][a-z0-9-_]{0,61}'
    r'[a-z0-9]$'
)


def parse_link(link):
    split_arr = link.split('://')
    i = (0, 1)[len(split_arr) > 1]
    domain = split_arr[i].split('?')[0].split('/')[0].split(':')[0].lower()
    if not re.match(pattern, domain):
        raise ValueError
    return domain
