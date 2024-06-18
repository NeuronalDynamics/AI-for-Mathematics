import itertools

def parenthesizations(n):
  """
  Returns a list of all possible parenthesizations of length n.

  Parameters:
    n (int): The length of the parenthesizations.

  Returns:
    A list of strings, where each inner string represents a valid parenthesization of length n.
  
  Example:
  >>> parenthesizations(3)
  {'((()))', '(()())', '(())()', '()(())', '()()()'}
  """
  if n == 0:
    return {""}
  else:
    result = set()
    for i in range(n):
      for left in parenthesizations(i):
        for right in parenthesizations(n - 1 - i):
          result.add(f"({left}){right}")
    return result

def product_orders(n):
  """
  Returns a list of all possible ways to multiply of n elements.

  Parameters:
    n (int): The number of elements multiplied.

  Returns:
    A set of strings where each string represents a way to multiply n elements.
  
  Example:
  >>> product_orders(4)
  {'((?*?)*?)*?', '(?*(?*?))*?', '(?*?)*(?*?)', '?*((?*?)*?)', '?*(?*(?*?))'}
  """
  if n == 0:
    return {""}
  elif n == 1:
    return {"?"}
  elif n == 2:
    return {"?*?"}
  else:
    result = set()
    for i in range(1, n):
      for left in product_orders(i):
        for right in product_orders(n - i):
          result.add(f"({left}*{right})")
    return result

def permutations_avoiding_231(n):
  """
  Returns a list of permutations of length n avoiding the pattern 2-3-1.
  
  Parameters:
    n (int): The length of the permutation.
  
  Returns:
    A list of permutations of length n that do not contain the pattern 2-3-1.
  
  Example:
  >>> permutations_avoiding_231(4)
  {(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (3, 1, 2, 4), (3, 2, 1, 4), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 3, 1, 2), (4, 3, 2, 1)}
  """
  if n < 3:
    return set(itertools.permutations(range(1, n+1)))
  else:
    result = set()
    for perm in itertools.permutations(range(1, n+1)):
        valid = True
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if perm[i] < perm[k] < perm[j]:
                        valid = False
                        break
                if not valid:
                    break
            if not valid:
                break
        if valid:
            result.add(perm)
    return result

def triangulations(n):
  """
  Returns a list of all possible triangulations of an n-sided polygon. A triangulation
  is represented as a list of internal edges. Vertices are labeled 0 through n-1 clockwise.

  Parameters:
    n (int): The number of sides of the polygon.

  Returns:
    A set of tuple of pairs, where each pair represents an internal edge in the triangulation.
  
  Example:
  >>> triangulations(3)
  {((0, 3), (1, 3)), ((1, 4), (2, 4)), ((1, 3), (1, 4)), ((0, 2), (2, 4)), ((0, 2), (0, 3))}
  """
  if n < 3:
    return set()
  elif n == 3:
    return {tuple()}
  else:
    result = set()
    for k in range(1, n-1):
        left_triangulations = triangulations(k+1)
        right_triangulations = triangulations(n-k)
        for left in left_triangulations:
            for right in right_triangulations:
                triangulation = tuple(sorted(list(left) + list(((0, k),)) + [(i + k, j + k) for i, j in right]))
                result.add(triangulation)
    return result