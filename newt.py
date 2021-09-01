# Newton root finder method
# Needs an error function that returns f(x) and the slope at x.

from utils import eps


def fsolve(f, x, args=(), maxi=24, tol=1e-6):
  for i in range(maxi):
    fx, dfx = f(x, *args)
    if abs(dfx) <= eps:
      raise Exception('Curve too flat!')
    x -= fx / dfx
    if abs(fx) <= tol:
      return x
  raise Exception('Max its reached!')
