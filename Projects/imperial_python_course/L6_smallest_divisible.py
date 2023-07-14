"""

  This program prints the smallest value from a series of values given by use

"""
import random

def compute_min_divisible(number_list, divisor):
  smallest = None
  if(len(number_list) > 0):
    number_list = sorted(number_list)
    for index in range(0, len(number_list)):
      if ((number_list[index] % divisor) == 0):
        smallest = number_list[index]
        break
  print(f'Smallest divisible: {smallest}')

def get_input():
  rand_num_list = []
  number_of_inputs = random.randint(0,10)
  divisor = random.randint(1,10)
  for i in range(0, number_of_inputs):
    generated_num = random.randint(-100, 100)
    rand_num_list.append(generated_num)
  print(f"Number list is: {rand_num_list}. Divisor is: {divisor}.")
  return rand_num_list, divisor

def main():
  num_list, divisor = get_input()
  num_list = [-33, -99, 33]
  divisor = 3
  compute_min_divisible(num_list, divisor)
main()



