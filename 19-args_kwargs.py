#args and kwargs
def product(*args):
  result = 1
  for num in args:
  result *= num
  return result

def describe_movie(**kwargs):
  description = ""
  for key, value in kwargs.items():
  description += f"{key.capitalize()}: {value}\n"
  return description

total_product = product(6, 8, 10)
print("Product of numbers:", total_product)
print()
movie_description = describe_movie(title="Mission Kashmir",
                                   director="Vidhu Vinod Chopra",
                                   year=2000,
                                   genre="Action/Thriller")
print("Movie description:\n", movie_description, sep="")
