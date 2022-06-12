"""
Randomly changes the case of a string's letters. The change of each letter
occurs with the given probability.
"""


from argparse import ArgumentParser
from random import random


_DEFAULT_PROB = 0.5
_EMPTY_STR = ""


def rand_switch_case(text, prob=_DEFAULT_PROB):
	"""
	Randomly changes the case of a string's letters. The change of each letter
	occurs with the given probability.

	Args:
		text (str): the string that will undergo random case changes
		prob (float): the probability that each letter in text have its case
			changed. It must range from 0.0 to 1.0. Defaults to 0.5.

	Returns:
		str: the given text, but with random case changes

	Except:
		ValueError: if prob is less than 0.0 or greater than 1.0
	"""
	if prob < 0.0 or 1.0 < prob:
		raise ValueError("The probability must range from 0.0 to 1.0.")

	chars = list()

	for char in text:
		if random() < prob:
			chars.append(_switch_case(char))
		else:
			chars.append(char)
	
	return _EMPTY_STR.join(chars)


def _switch_case(c):
	sc = c

	if c.islower():
		sc = c.upper()

	elif c.isupper():
		sc = c.lower()

	return sc


if __name__ == "__main__":
	arg_parser = ArgumentParser(description=__doc__)
	arg_parser.add_argument("-t", "--text", required=True,
		help="the string that will undergo random case changes")
	arg_parser.add_argument("-p", "--probability",
		type=float, default=_DEFAULT_PROB,
		help="the probability that each letter in text have its case changed."
			+ " It must range from 0.0 to 1.0. Defaults to 0.5.")

	args = arg_parser.parse_args()
	text = args.text
	prob = args.probability

	try:
		rand_case_text = rand_switch_case(text, prob)
		print(rand_case_text)
	except ValueError as ve:
		print(f"ERROR! {ve}")
