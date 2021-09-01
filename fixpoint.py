# Aitken fixed point acceleration method.

from utils import eps


def fixpoint(f, x, args=(), tol=1e-5, maxi=48):
  for i in range(maxi):
    a = f(x, *args)
    b = f(a, *args)
    d = x + b - 2.0 * a
    if abs(d) <= eps:
      raise Exception('Divide by zero!')
    dx = b - a
    x = b - dx * dx / d
    if abs(x - b) < tol:
      return x
  raise Exception('Max its reached!')
