import urllib.request
import re


def load_file(path):
    with open(path, 'r') as file:
        data = file.read().replace('\n', '')
    return data


if __name__ == '__main__':
    text = load_file('README.md')
    s = re.findall('\((.*?)\)',text)

    broken_links = list()
    for link in s:
        try:
            conn = urllib.request.urlopen(link)
        except urllib.error.HTTPError as e:
            print('HTTPError: {}'.format(e.code) + ', ' + link)
            broken_links.append(link)
        except urllib.error.URLError as e:
            print('URLError: {}'.format(e.reason) + ', ' + link)
        except ValueError as e:
            print('ValueError: {}'.format(e) + ', ' + link)
        else:
            print('good' + ', ' + link)

    with open('broken_links.txt', 'w') as f:
        for line in broken_links:
            f.write(f"{line}\n")