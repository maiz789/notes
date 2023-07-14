def is_palindrome():
  word = input("Please enter a word: ")
  if(word == word[::-1]):
    print("True")
    return
  print("False")
  return
import string

def is_palindrome_advanced(sentence):
  #words = input("Please enter a sentence: ")
  words = sentence
  words = words.lower()
  words = words.strip()
  words_list = []
  words_list_done = []
  words_list = words.split()
  for word in words_list:
    while word[0] in string.punctuation:
      word = word[1:]
    while word[-1] in string.punctuation:
      word = word[:-1]
    words_list_done.append(word)
  together = "".join(words_list_done)
  if(together == together[::-1]):
    print("True")
    return
  print("False")
  return


def blankify():
  words = input("Please enter a sentence: ")
  words_list = list(words)
  for letter_index in range(len(words_list)):
    if(words_list[letter_index] == words[0]):
      words_list[letter_index] = "-"
  print("".join(words_list))
  return

def debug():
  total = 1
  while total < 2 or total > 10:
      breakpoint()
      num = 10 + total
      total = total + num

  print(total)


#is_palindrome()
#blankify()
#debug()
is_palindrome_advanced("Eva, can I see bees in a cave?")