import itertools
import multiprocessing
import os

class LinesIter:
    def __init__(self, lines):
        self._i = 0
        self._lines = lines

    def __iter__(self):
        return self

    def __next__(self):
        if self._i == self._lines:
            raise StopIteration
        self._i += 1
        return f"Line {self._i}"


# Function to write lines to a file
def write_lines(filename, lines):
    with open(filename, 'w') as file:
        try:
            for line in lines:
                file.write(line + '\n')
        except IOError as e:
            errno, strerror = e.args
            print(f"I/O error({errno}): {strerror}")


if __name__ == '__main__':
    # Get the absolute path of the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print('script_dir: ', script_dir)
    # Create a pool of processes`
    with multiprocessing.Pool(2) as pool:
        total_lines = 10000
        chunk_size = 5000
        lines_iter = LinesIter(total_lines)
        for i in range(0, total_lines // chunk_size):
            chunk = itertools.islice(lines_iter, i * chunk_size, (i + 1) * chunk_size)
            file_path = os.path.join(script_dir, f'file-{i}.txt')
            pool.apply_async(write_lines, (file_path, chunk))
        pool.close()
        pool.join()

    print("Writing completed successfully.")
