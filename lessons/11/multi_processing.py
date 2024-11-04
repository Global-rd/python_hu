import time
import multiprocessing

def is_prime(n):
    
    if n<=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes_in_range(lower_limit, upper_limit):
    return sum(1 for n in range(lower_limit, upper_limit) if is_prime(n))

def worker(lower_limit, upper_limit, queue):
    result = count_primes_in_range(lower_limit, upper_limit)
    queue.put(result)


def single_process_execution(limit):

    print("Counting primes using a single process")
    start_time = time.time()
    result_single = count_primes_in_range(0, limit)
    end_time = time.time()
    print(f"number of primes up to {limit} (single process): {result_single}")
    print(f"Time taken (single process): {end_time - start_time:.2f} seconds\n")

def multi_process_execution(limit):

    print("Counting primes using multiple processes")
    start_time = time.time()

    queue = multiprocessing.Queue()
    processes = []
    
    cpu_count = multiprocessing.cpu_count()
    print(cpu_count)
    step = limit // cpu_count

    for i in range(cpu_count):
        lower_limit = i * step
        upper_limit = limit if i == cpu_count -1 else (i + 1) * step
        process = multiprocessing.Process(target=worker, args=(lower_limit, upper_limit, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    result_multiple = [queue.get() for _ in processes]
    total_primes = sum(result_multiple)
    
    end_time = time.time()
    print(f"number of primes up to {limit} (multiple processes): {total_primes}")
    print(f"Time taken (multiple processes): {end_time - start_time:.2f} seconds\n")

def main():
    limit = 100000

    single_process_execution(limit)
    multi_process_execution(limit)

if __name__ == "__main__":
    main()