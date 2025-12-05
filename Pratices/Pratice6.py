import threading
import requests

def fetch(url):
    
    response = requests.get(url)

    print(f"Fetched {url} with status code {response}")

def main():

    urls = [
    "https://httpbin.org/get",
    "https://httpbin.org/uuid",
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://example.com",
    "https://api.github.com",
           ]

    Threads = []

    for url in urls:
        t = threading.Thread(target=fetch, args=(url,))
        Threads.append(t)

    for t in Threads:
        t.start()

    for t in Threads:
        t.join()

if __name__ == "__main__":
    main()