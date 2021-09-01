# polynomial root (from Conte and de Boor).

from utils import eps

def polyroot(a, x, tol=1e-6, maxi=24):
  n = len(a) - 1  # high index
  for i in range(maxi):
    p = a[n]
    q = p
    for k in range(n-1, 0, -1):
      p = a[k] + x*p
      q = p + x*q
    p = a[0] + x*p
    if abs(q) <= eps:
      raise Exception("Curve too flat!")
    dx = p/q
    if abs(dx) <= tol:
      return x
    x -= dx
  raise Exception("Max its reached!")
