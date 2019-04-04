import unittest
from pool import Pool
from func import counter
import numpy as np

class TestPool(unittest.TestCase):

	def data(self, step):
		with open("book.txt") as f:
			big_data = f.read().split()
		big_data = ' '.join(big_data)
		big_data = np.array_split(list(big_data), step)
		return big_data

	def test_func(self):
		word = 'K3140'
		result = counter(word)
		self.assertEqual(5, result)

	def test_worker_default(self):
		proc = Pool()
		big_data = self.data(40)
		func = proc.map(counter, big_data)
		self.assertEqual(10, func[0])

	def test_workers_less_than_min(self):
		proc = Pool(4, 7, 500)
		with self.assertRaises(Exception) as context: 
			proc.map(counter, self.data(3))
		self.assertTrue('Number of processes is too small.' in str(context.exception))
		
	def test_workers_more_than_max(self):
		proc = Pool(4, 7, 500)
		big_data = self.data(10)
		func = proc.map(counter, big_data)
		self.assertEqual(7, func[0])

	def test_mem_usage_error(self):
		proc = Pool(4, 7, 10)
		with self.assertRaises(Exception) as context: 
			proc.map(counter, self.data(6))
		self.assertTrue('The process is too heavy. Please, delete some data.' in str(context.exception))
		
	def test_mem_usage(self):
		proc = Pool(4, 7, 500)
		big_data = self.data(5)
		func = proc.map(counter, big_data)
		self.assertGreaterEqual(500, func[0]*func[1])

if __name__ == '__main__':
	unittest.main()