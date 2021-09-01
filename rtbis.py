# Bisection method (from Numerical Recipes).


def fsolve(f, x0, args=(), tol=1e-5, maxi=98):
  if len(x0) != 2:
    raise Exception("Need two guesses!")
  x1, x2 = x0
  f1 = f(x1, *args)
  f2 = f(x2, *args)
  if f1 * f2 >= 0.0:
    raise Exception("No bracket!")
  if f1 < 0.0:
    dx = x2 - x1
    x = x1
  else:
    dx = x1 - x2
    x = x2
  for i in range(maxi):
    dx *= 0.5
    if abs(dx) < tol:
      return x
    x2 = x + dx
    f2 = f(x2, *args)
    if f2 == 0.0:
      return x2
    if f2 <= 0.0:
      x = x2
  raise Exception("Max its reached!")
