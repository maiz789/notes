"""

  This program prints a list of numbers, each member also being a list, where the 1st list is [1], 2nd is [1, 2] ... etc until the list reaches [1, 2 ... [user specified]]

"""
import random

def get_user_input():
  user_defined_length = int(input("Please enter maximum length: "))
  return user_defined_length

def generate_random_number_list():
  number_of_elements = random.randrange(0, 10)
  list_of_random_numbers = []
  num = 0
  while num < number_of_elements:
    list_of_random_numbers.append(random.randint(0, 10))
    num+=1
  return list_of_random_numbers

def cumulative_sum_at_index(rand_num_list):
  """ Takes a list of integers as input, and return a list containing cumulative sum at each index

  Arg:
    rand_num_list (list): list of random numbers
  Ret:
    list_of_lists (list): list of number containing cumulative sum at each index

  """
  list_of_lists = []
  if(len(rand_num_list) > 0):
    for row_max_index in range(0, len(rand_num_list)):
      current_list = []
      for current_list_index in range(0, row_max_index+1):
        current_list.append(rand_num_list[current_list_index])
      list_of_lists.append(sum(current_list))
  return list_of_lists

def print_list(input_lists):
  print(input_lists)

def main():
  random_number_list = generate_random_number_list()
  print_list(f'random number list{random_number_list}.')
  lists = cumulative_sum_at_index(random_number_list)
  print_list(f'cumulative list {lists}.')

def test():
  test_length = 3
  list_to_print = generate_list(test_length)
  assert len(list_to_print) == 3, f'List length is wrong'
  assert len(list_to_print[2]) == 3, f'List length of last element is wrong'
  print(list_to_print)

main()