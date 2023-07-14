"""

  This program prints a list of numbers, each member also being a list, where the 1st list is [1], 2nd is [1, 2] ... etc until the list reaches [1, 2 ... [user specified]]

"""

def get_user_input():
  user_defined_length = int(input("Please enter maximum length: "))
  return user_defined_length

def generate_list(max_length):
  """ Generate n lists, each increment in length, till it reaches n.

  Arg:
    max_length (int): maximum length specifid by the user

  """
  list_of_lists = []
  for num_of_lists in range(1, max_length+1):
    current_list = []
    for current_list_elements in range(1, num_of_lists+1):
      current_list.append(current_list_elements)
    list_of_lists.append(current_list)
  return list_of_lists

def print_list(input_lists):
  print(input_lists)

def main():
  max_length = get_user_input()
  lists = generate_list(max_length)
  print_list(lists)

def test():
  test_length = 3
  list_to_print = generate_list(test_length)
  assert len(list_to_print) == 3, f'List length is wrong'
  assert len(list_to_print[2]) == 3, f'List length of last element is wrong'
  print(list_to_print)

main()