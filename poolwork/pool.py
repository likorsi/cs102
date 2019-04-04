from multiprocessing import Process, cpu_count
from func import counter
import numpy as np
import psutil
import time

class Pool():
	def __init__(self, min_workers=1, max_workers=10, mem_usage=500):
		self.min_workers = min_workers
		self.max_workers = max_workers
		self.mem_usage = mem_usage
		self.max_memory = 0


	def map(self, function, chunks):
		procs = []

		proc = Process(target=function, args=(chunks[0],))
		procs.append(proc)
		proc.start()

		info = psutil.Process()		
		max_memory_count = []

		while proc.is_alive():
			max_memory_count.append(info.memory_info().rss / 1024 / 1024)  # return in Mb
			time.sleep(0.0005)
		
		self.max_memory = max(max_memory_count)
		
		workers = int(self.mem_usage/self.max_memory)
		
		if self.max_memory > self.mem_usage:
			raise Exception('The process is too heavy. Please, delete some data.')

		if workers < self.min_workers or len(chunks) < self.min_workers:
			raise Exception('Number of processes is too small.')

		if workers > self.max_workers: workers = self.max_workers

		for index, chunk in enumerate(chunks[1:workers]):
			proc = Process(target=function, args=(chunk,))
			procs.append(proc)
			proc.start()

		for proc in procs:
			proc.join()

		return workers, self.max_memory

if __name__ == '__main__':

	with open("book.txt") as f:
		big_data = f.read().split()

	big_data = ' '.join(big_data)
	big_data = np.array_split(list(big_data), 8)

	pool = Pool()
	results = pool.map(counter, big_data)
