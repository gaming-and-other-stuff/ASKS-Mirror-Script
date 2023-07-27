import subprocess

def mirror_urls_from_file(file_path):
    mirrored_urls = []
    with open(file_path, 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        command = f'wget --spider --server-response "{url}" 2>&1'
        output = subprocess.run(command, shell=True, capture_output=True, text=True)
        if '200 OK' in output.stdout:
            mirrored_urls.append(url)
            mirror_command = f'wget --mirror --convert-links "{url}"'
            subprocess.run(mirror_command, shell=True)
    return mirrored_urls

file_path = 'urls.txt'
mirrored_urls = mirror_urls_from_file(file_path)
print("Mirrored URLs:")
for url in mirrored_urls:
    print(url)
