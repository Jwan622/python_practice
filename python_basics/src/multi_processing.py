from multiprocessing import pool
import itertools
from pathlib import Path


class LinesIter:
    """
    Class: LinesIter
    This is an iterator class that generates a sequence of lines. Each line is a simple string, "Line {number}".
    __init__(self, lines): Constructor that initializes the iterator. self._i keeps track of the current position in the iteration, and self._lines stores the total number of lines to generate.
    __iter__(self): Returns the iterator object (self), required for an iterator.
    __next__(self): This method is called whenever the next item from the iterator is needed. It increments self._i and returns the corresponding line as a string. If self._i equals self._lines, it raises a StopIteration exception to signal that the iteration is complete.
    """
    def __init__(self, total_lines_count):
        self._i = 0
        self.total_lines_count = total_lines_count

    def __iter__(self):
        return self

    def __next__(self):
        if self._i == self.total_lines_count:
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
    # Get the directory of the script
    script_dir = Path(__file__).resolve().parent
    print(f"script_dir: ", Path(__file__).resolve().parent)
    # Create a Path object for the 'file_output' subdirectory
    output_dir = script_dir / 'file_output'
    print(f"file: {__file__}")
    print('output_dir: ', output_dir)
    # Create a pool of processes`
    with pool.Pool(2) as pool:
        total_lines = 10000
        chunk_size = 5000
        lines_iter = LinesIter(total_lines)
        for i in range(0, total_lines // chunk_size):
            chunk = itertools.islice(lines_iter, i * chunk_size, (i + 1) * chunk_size)
            print(f"chunk:", chunk)
            file_path = output_dir / f'file-{i}.txt'
            pool.apply_async(write_lines, (file_path, chunk))
        pool.close()
        pool.join()

    print("Writing completed successfully.")

"""
- The main part of the script uses the multiprocessing library (imported as pool here) to write lines to files in parallel.
- A pool.Pool object is created to manage a pool of worker processes. Here, the size of the pool is 2, meaning two processes will be running concurrently.
total_lines is the total number of lines to be written, and chunk_size is the number of lines each file will contain.
- LinesIter(total_lines) creates an iterator for the total number of lines.
- A for loop divides the total lines into chunks and uses itertools.islice to create an iterator for each chunk of lines. This iterator is a slice of the lines_iter from the start to the end of the current chunk.
- For each chunk, a separate file is created, named file-{i}.txt.
- pool.apply_async is used to execute write_lines function asynchronously. This means that the function will run in a separate, parallel process, and the main program will not wait for it to complete before moving on to the next iteration of the loop.
- After all tasks are submitted to the pool, pool.close() is called to prevent any more tasks from being submitted to the pool. pool.join() waits for the worker processes to finish.
"""
