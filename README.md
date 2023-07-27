This is the script I used when mirroring .asks files from the ASK Sound Novel Maker (ASKノベルゲームメーカー). The script notably slowed down my computer and caused the file explorer and most other open apps to become unresponsive, so use the script at your own risk (probably had something to do with me giving the script over 10,000 urls)

## Prerequisites
* wget
* Python 3

## Usage
The script will take URLs from a file called "urls.txt" and run the ``--spider`` command on it. If it returns a ``2XX`` response, it will use wget to mirror the file.
* Put the script and a file called "urls.txt" in the same folder. You can edit the script to change the name of the needed txt.
* Run the script in Python
