import string
def main():
  text = readText('books/frankenstein.txt')
  report(text)


def readText(path):
  with open(path) as f:
    text = f.read()
  return text

def count_words(text):
  print(f"{len(text.split())} words found in document")

def count_characters(text):
  letters = sum(c.isalpha() for c in text)
  return letters

def report(text):
  alphabets = list(string.ascii_lowercase)
  print('--- Begin report of books/frankenstein.txt ---')
  count_words(text)
  print()
  for i in alphabets:
    number_of_times = text.lower().find(i)
    print(f"The {i} character was found {number_of_times} times")

main()