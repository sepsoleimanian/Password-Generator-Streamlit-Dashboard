from abc import ABC, abstractmethod
import random
import string
import nltk

nltk.download('words')
words = nltk.corpus.words.words()

class PasswordGenerator(ABC):
  @abstractmethod
  def generate(self):
    pass


class PinGenerator(PasswordGenerator):
  def __init__(self, length: int = 6):
    self.length = length
  
  def generate(self):
    return ''.join([random.choice(string.digits) for _ in range(self.length)])
  
  
class RandomPasswordGenerator(PasswordGenerator):
  def __init__(self, length: int = 8, include_numbers: bool = True, include_symbols: bool = True):
    self.length = length
    self.characters = string.ascii_letters
    if include_numbers:
      self.characters += string.digits
    if include_symbols:
      self.characters += string.punctuation
      
  def generate(self):
    return ''.join([random.choice(self.characters) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenerator):
  def __init__(self, 
               number_of_words: int = 4,
               seperator: str = '-', 
               capitalization: bool = True, 
               vocabulary: list = None
               ):
    
    if vocabulary is None:
      self.vocabulary = words
    else:
      self.vocabulary = vocabulary
    self.num_of_words = number_of_words
    self.capitalization = capitalization
    self.seperator = seperator
  
  def generate(self):
    password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
    if self.capitalization:
      password_words = [word.upper() if random.random() < 0.5 else word.lower() for word in password_words]
    return self.seperator.join(password_words)
  
if __name__ == '__main__':
  pin = PinGenerator()
  random_pass = RandomPasswordGenerator()
  memorable_pass = MemorablePasswordGenerator()
  
  pin_generate = pin.generate()
  random_pass_generate = random_pass.generate()
  memorable_pass_generate = memorable_pass.generate()
  
  print(f'generated pin: {pin_generate}\n'
      f'generated random password: {random_pass_generate}\n'
      f'generated memorable password: {memorable_pass_generate}')

