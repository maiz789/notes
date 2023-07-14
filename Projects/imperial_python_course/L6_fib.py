"""

  This program prints Fibonnaci numbers up to the given length of list

"""
import random

def get_user_input():
  user_defined_length = int(input("Please enter maximum length: "))
  return user_defined_length

def generate_fibonacci(max_length):
  fib_seq = [0, 1]
  while len(fib_seq) < max_length:
    next_fib = fib_seq[len(fib_seq) - 1] + fib_seq[len(fib_seq) - 2]
    fib_seq.append(next_fib)
  return fib_seq

def print_list(input_lists):
  print(input_lists)

def main():
  max_length = get_user_input()
  fibonacci_list = generate_fibonacci(max_length)
  print_list(fibonacci_list)

main()