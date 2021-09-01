# Polynomial root by newtons method (Lawrence Atkinson).

from utils import eps


def polyroot(a, x, tol=1e-6, maxi=24):

  def evalpoly(a, b, n, x):
    """returns p=poly(x) and b=slope"""
    b[n-1] = a[n]
    for i in range(n-2, -1, -1):
      b[i] = a[i+1] + x*b[i+1]
    return a[0] + x*b[0]

  def poly(a, n, x):
    """returns p where p=poly(x)"""
    p = a[n]
    for i in range(n-1, -1, -1):
      p = p*x + a[i]
    return p

  n = len(a)-1
  b = [0.0 for _ in range(n)]
  y = evalpoly(a, b, n, x)
  for i in range(maxi):
    if abs(x) <= eps:
      raise Exception("Too near zero!")
    dy = poly(b, n-1, x)
    if abs(dy) <= eps:
      raise Exception("Curve too flat!")
    xo = x
    x -= y/dy
    y = evalpoly(a, b, n, x)
    if abs(x-xo) <= tol:
      return x
  raise Exception("Max its reached!")
