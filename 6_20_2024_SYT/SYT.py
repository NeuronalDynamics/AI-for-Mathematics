import itertools
import random
import os
from itertools import permutations
import time

def is_valid_SYT(candidate):
  """
  Check if the given candidate tableau is a valid standard Young tableau.

  Parameters:
  - candidate (Tuple[Tuple[int]]): The tableau to be checked.

  Returns:
  - bool: True if the matrix is valid, False otherwise.

  The function checks if the given matrix is a valid SYT matrix by verifying that:
  1. The elements in each column are in strictly increasing order.
  2. The elements in each row are in strictly increasing order.

  Example:
  >>> is_valid_SYT(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
  True
  >>> is_valid_SYT(((1, 2, 3), (5, 4), (6))
  False
  """
  # Check if each row is strictly increasing
  for row in candidate:
      if not all(row[i] < row[i + 1] for i in range(len(row) - 1)):
          return False

  # Check if each column is strictly increasing
  num_cols = max(len(row) for row in candidate)
  for col in range(num_cols):
      col_elements = []
      for row in candidate:
          if col < len(row):
              col_elements.append(row[col])
      if not all(col_elements[i] < col_elements[i + 1] for i in range(len(col_elements) - 1)):
          return False

  return True

def reshape_perm(perm, shape):
  """
  Reshapes a permutation into a tableau based on the given shape.

  Parameters:
  - perm (Tuple[int]): The permutation to be reshaped.
  - shape (Tuple[int]): The shape of the resulting tableau as a weakly decreasing tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A tuple of tuples representing the reshaped permutation as a tableau.

  Example:
  >>> reshape_perm((1, 2, 3, 4, 5, 6), (3, 2, 1))
  ((1, 2, 3), (4, 5), (6,))
  """
  tableau = []
  index = 0
  for row_length in shape:
      row = tuple(perm[index:index + row_length])
      tableau.append(row)
      index += row_length
  return tuple(tableau)

def SYTs(shape):
  """
  Generates SYTs (Standard Young Tableaux) of on the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYTs as a tuple of integers.

  Returns:
  - List[Tuple[Tuple[int]]]: A list of valid SYTs generated based on the given shape.

  Example:
  >>> SYTs((2, 1))
  [((1, 2), (3,)), ((1, 3), (2,))]
  """

  n = sum(shape)
  results = []

  # Generate all permutations of numbers from 1 to n
  for perm in permutations(range(1, n + 1)):
      # Reshape the permutation to the given shape
      tableau = reshape_perm(perm, shape)
      # Check if the reshaped tableau is a valid SYT
      if is_valid_SYT(tableau):
          results.append(tableau)

  return results

def random_SYT(shape):
  """
  Generates a random Standard Young Tableau (SYT) of the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYT as a tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A random valid SYT generated based on the given shape.

  This function generates a random permutation of numbers from 1 to n+1, where n is the sum of the elements in the `shape` tuple. It then reshapes the permutation into a tableau using the `reshape_perm` function. If the resulting tableau is not valid, it shuffles the permutation and tries again. The function continues this process until a valid SYT is found, and then returns the reshaped permutation as a tableau.

  Example:
  >>> random_SYT((2, 1))
  ((1, 2), (3,))
  """
  n = sum(shape)
  while True:
      perm = list(range(1, n + 1))
      random.shuffle(perm)
      tableau = reshape_perm(perm, shape)
      if is_valid_SYT(tableau):
          return tableau

def random_SYT_2(shape):
  """
  Generates a random Standard Young Tableau (SYT) of the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYT as a tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A random valid SYT generated based on the given shape.

  The function generates a random SYT by starting off with the all zeroes tableau and greedily filling in the numbers from 1 to n. The greedy generation is repeated until a valid SYT is produced.

  Example:
  >>> random_SYT_2((2, 1))
  ((1, 2), (3,))
  """
  n = sum(shape)
  while True:
      tableau = []
      for row_length in shape:
          tableau.append([0] * row_length)

      numbers = list(range(1, n + 1))
      random.shuffle(numbers)
      
      for num in numbers:
          placed = False
          for i, row in enumerate(tableau):
              for j in range(len(row)):
                  if row[j] == 0:
                      tableau[i][j] = num
                      placed = True
                      break
              if placed:
                  break
      
      # Convert the tableau to tuple of tuples
      tableau_tuple = tuple(tuple(row) for row in tableau)

      if is_valid_SYT(tableau_tuple):
          return tableau_tuple
      

def save_SYTs_to_file(shape, directory='data'):
    """
    Generates and saves all valid SYTs for the given shape to a file in the specified directory.

    Parameters:
    - shape (Tuple[int]): The shape of the SYTs.
    - directory (str): The directory to save the files in.
    """
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    
    # Generate SYTs for the given shape
    syt_list = SYTs(shape)
    
    # Convert shape to string format for filename
    shape_str = '_'.join(map(str, shape))
    
    # Define the filename
    filename = os.path.join(directory, f'SYTs_{shape_str}.txt')
    
    # Save SYTs to file
    with open(filename, 'w') as file:
        for syt in syt_list:
            file.write(f'{syt}\n')