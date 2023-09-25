import requests

def filter_2xx_urls_from_file(file_path):
    found_urls = []
    with open(file_path, 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        response = requests.head(url)
        if response.status_code // 100 == 2:
            found_urls.append(url)

    return found_urls

file_path = 'urls.txt'
found_urls = filter_2xx_urls_from_file(file_path)

with open('final-urls.txt', 'w') as f:
    f.write('\n'.join(found_urls))

print("Done!")