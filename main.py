import multiprocessing

def process_file(file_path, result_queue):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        count = len(lines)
        result_queue.put(f"{file_path}: {count} lines")


def main():
    file_paths = ["file1.txt", "file2.txt", "file3.txt"]

    result_queue = multiprocessing.Queue()
    processes = []

    for path in file_paths:
        p = multiprocessing.Process(target=process_file, args=(path, result_queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Результаты обработки:")
    while not result_queue.empty():
        print(result_queue.get())


if __name__ == "__main__":
    main()