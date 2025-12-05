import threading
import requests
import os

def download_image(url, filename):
    print(f"Image File name: {filename}")
    response = requests.get(url)

    if os.path.exists("images"):

        with open(filename, "wb") as img:
            img.write(response.content)
    else:

        os.mkdir("images")

        with open(filename, "wb") as img:
            img.write(response.content)

    print("Image Saved Succesfully")

def main():

    urls = [
    "https://picsum.photos/id/10/500/300",
    "https://picsum.photos/id/20/500/300",
    "https://picsum.photos/id/30/500/300",
    "https://picsum.photos/id/40/500/300",
    "https://picsum.photos/id/50/500/300",
    "https://picsum.photos/id/60/500/300",
    "https://picsum.photos/id/70/500/300",
    "https://picsum.photos/id/80/500/300",
    "https://picsum.photos/id/90/500/300",
    "https://picsum.photos/id/100/500/300"]

    Threads = []
    i = 0

    for url in urls:

        t = threading.Thread(target=download_image, args=(url, f"images/url{i}.png"))
        i += 1
        Threads.append(t)

    for t in Threads:
        t.start()

    for t in Threads:
        t.join()

if __name__ == "__main__":
    main()