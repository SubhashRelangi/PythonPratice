import threading

lock = threading.Lock()

wordCount = {}

def count_words(filename):
    with open(filename, 'r') as f:
        content = f.read()
        words = content.split()
        count = len(words)

        with lock:
            wordCount[filename] = count


files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt" ]

threads = []

for f in files:
    t = threading.Thread(target=count_words, args=(f,))
    threads.append(t)


for t in threads:
    t.start()

for t in threads:
    t.join()

total = 0

for f in files:
    count = wordCount.get(f, 0)
    print(f"word count of the {f}: {count}")
    total += count

print(f"The total word count of these files: {total}")