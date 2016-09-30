from pytest import raises
from binsearch import binary_search
import numpy as np

input = list(range(10))

def test_binary_search():
	assert binary_search(input,5) == 5

def test_dne():
	assert binary_search(input,4.5) < 0

def test_dne2():
	assert binary_search(input,10) < 0

def test_empty():
	assert binary_search([],7) < 0

def test_one_elem():
	assert binary_search([5], 5)

def test_type_mismatch():
	with raises(TypeError):
		binary_search([1],'b')

def test_inf():
	assert binary_search([1,2,np.inf], 2) == 1

def test_inf2():
	assert binary_search([1,2,np.inf], np.inf) == 2

def test_high_needle():
	assert binary_search(input,5,0,2) < 0

def test_low_needle():
	binary_search(input,3,5,9) < 0

def test_search_bounds_high():
	with raises(ValueError):
		binary_search(input,5,0,11)

def test_search_bounds_low():
	with raises(ValueError):
		binary_search(input,5,-2,9)

def test_backward_bounds():
	with raises(ValueError)
		binary_search(input,5,7,2)

def test_nan():
	binary_search([1,2,np.nan,8],2) == 1

def test_nan_2():
	binary_search([1,2,np.nan,8],np.nan) == 2

def test_str():
	binary_search(['a','b','c','d'],'d') == 3

def test_repeat():
	binary_search([1,2,2,3],2) in [1,2]




