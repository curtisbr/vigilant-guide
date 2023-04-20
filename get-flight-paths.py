import wget
import urllib3
import time

http = urllib3.PoolManager()

with open("ual-flight-paths.txt", 'r') as f:
    lines = f.readlines()
    for line_no, content in enumerate(lines):
        url = f"{content}"
        print("checking url: " + url)
        lst = url.split("/")
        filename = "flight-paths/" + lst[5] + "_" + lst[7] + "_" + lst[8] + "_" + lst[9] + "_" + lst[10] + ".kml"
        r = http.request('GET', url)
        if r.status == 200:
            print("file found. downloading... " + filename)
            wget.download(url, out=filename)
        else:
            print("file not found. skipping...")
        time.sleep(1)

