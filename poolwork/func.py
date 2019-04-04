from multiprocessing import current_process
import numpy as np

def counter(data_chunk):
	symbols = 0
	for word in data_chunk:
		for i in word:
			symbols += 1

	proc_name = current_process().name
	#print(" symbols: {} number of process: {}".format(symbols, proc_name))
	return symbols