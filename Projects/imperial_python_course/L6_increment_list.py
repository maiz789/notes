def increment_list(numbers, step = 1):
  """
  #Why in the following code i is not the object itself (but rather a replica of the object?)
  for i in numbers:
    print(f'i: {i}')
    i += step
    print(f'i after: {i}')
  return numbers
  """
  i = 0
  while (i < len(numbers)):
    numbers[i] += step
    i += 1
  return numbers


numbers = [-2, 5]
incremented_numbers = increment_list(numbers, step=-2)
print(incremented_numbers)  # [-4, 3]
