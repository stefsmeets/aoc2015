import time


def timeit(func):
    def wrapper(*args, **kw):

        t0 = time.time()
        result = func(*args, **kw)
        t1 = time.time()

        print(f'> {func.__name__} took: {t1-t0:.3f} s, result: {result}')

        return result

    return wrapper


def download(day: int, year: int = 2022) -> str:
    from cookie import cookie
    import requests

    url = f'https://adventofcode.com/{year}/day/{day}/input'

    headers = {'Cookie': cookie}
    r = requests.get(url, headers=headers)

    return r.text


def download_entry():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--day', type=int)
    parser.add_argument('-y', '--year', type=int, default=2022)
    args = parser.parse_args()

    s = download(day=args.day, year=args.year)

    with open('data.txt', 'w') as f:
        f.writelines(s)

    lines = s.splitlines()

    for i, line in enumerate(lines):
        if len(line) > 80:
            print(f'{line[:75]} ...')
        else:
            print(line)

        if i == 10:
            print('...')
            break


def remove_tags(text: str) -> str:
    from xml.etree import ElementTree
    return ''.join(ElementTree.fromstring(text).itertext())


def submit(answer: int, part: int, day: int, year: int = 2022):
    from cookie import cookie
    import re
    import requests

    re_ANSWER = re.compile(r'<article>(<p>.*?></p>)')

    url = f'https://adventofcode.com/{year}/day/{day}/answer'

    data = {'level': part, 'answer': answer}

    headers = {'Cookie': cookie}
    r = requests.post(url, headers=headers, data=data)

    match = re_ANSWER.search(r.text)
    if match:
        print(remove_tags(match[1]))
    else:
        # Unexpected output
        print(r.text)


def submit_entry():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--day', type=int)
    parser.add_argument('-y', '--year', type=int, default=2022)
    parser.add_argument('-p', '--part', type=int, choices=(1, 2))
    parser.add_argument('-a', '--answer', type=int)

    args = parser.parse_args()

    submit(
        answer=args.answer,
        part=args.part,
        day=args.day,
        year=args.year,
    )
