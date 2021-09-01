# Bisection method (from Lawrence Atkinson).


def fsolve(f, x0, args=(), tol=1e-5, maxi=98):
  if len(x0) != 2:
    raise Exception("Need two guesses!")
  x1, x2 = x0
  f1 = f(x1, *args)
  for i in range(maxi):
    x = 0.5 * (x1 + x2)
    fx = f(x, *args)
    if f1 * fx <= 0.0:
      x2 = x
    else:
      x1, f1 = x, fx
    if abs(x2 - x1) <= tol:
      return x
  raise Exception("Max its reached!")
