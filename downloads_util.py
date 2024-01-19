import os
import requests  # efficient for http requests
import shutil  # efficient for downloading large files

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")

os.makedirs(DOWNLOADS_DIR, exist_ok=True)

downloaded_img_path = os.path.join(DOWNLOADS_DIR, "")

# a smallish item
img_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLZprupHLBxt_MHckG8HcXUrKvpU3fuMgJr2Nd0tktI-p-cuoiIu6_kVeX8c3eHeeyHLY&usqp=CAU"
downloaded_img_path = os.path.join(DOWNLOADS_DIR, "img.jpg")

r = requests.get(img_url, stream=True)
r.raise_for_status()
with open(downloaded_img_path, "wb") as f:
    f.write(r.content)


# for a larger item
def download_file(url, directory, fname=None):
    if fname == None:
        fname = os.path.basename(url)
    dl_path = os.path.join(directory, fname)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(dl_path, "wb") as f:
            shutil.copyfileobj(r.raw, f)
