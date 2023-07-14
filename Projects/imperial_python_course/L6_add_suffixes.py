"""

Adds suffixes to the end of each word from input list

"""

def load_verbs_from_file(filename):
  verbs = []
  textfile = open(filename)
  for line in textfile:
    verb = line.strip()
    verbs.append(verb)
  return verbs

def add_suffixes(verbs, suffixes):
  verbs_with_suffixes = []
  for suffix in suffixes:
    verbs_with_one_suffix = []
    for verb in verbs:
      verbs_with_one_suffix.append(verb + suffix)
    verbs_with_suffixes.append(verbs_with_one_suffix)
  return verbs_with_suffixes

def print_list(word_list):
  for word in word_list:
    print(word)

def main():
  verbs = load_verbs_from_file(path_to_file)
  verbs_with_suffixes = add_suffixes(verbs, suffixes)
  #print_list(verbs_with_suffixes)
  print(verbs_with_suffixes)


path_to_file = "verbs2.txt"
suffixes = ["ing", "ed"]
main()