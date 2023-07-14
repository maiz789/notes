"""
import pycodestyle
print(pycodestyle.__file__)
"""


import os
import sys
pipPath = f'{os.path.dirname(sys.executable)}\\Scripts'
os.system(f'setx PATH "%PATH%;{pipPath}"')
"""
    
guess = 5
if guess > 5:
  print("Too large")
  print("Try again")
else:
  print("Ok")
"""