"""

  This program prints the smallest value from a series of values given by use

"""


def compute_min(num_list):
  current_smallest = None
  if(len(num_list) > 0):
    current_smallest = num_list[0]
    for list_index in range(0, len(num_list)):
      if(num_list[list_index] < current_smallest):
        current_smallest = num_list[list_index]
  print(current_smallest)

def take_input():
  user_input = input("Enter an integer: ")
  return user_input

def take_inputs_continually():
  num_list = []
  to_continue = True
  while(to_continue == True):
    current_input = take_input()
    if(str(current_input) == "q"):
      break
    else:
      num_list.append(int(current_input))
  return num_list

def main():
  num_list = take_inputs_continually()
  compute_min(num_list)

main()



