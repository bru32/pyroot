# Illinois method (modified secant).


def fsolve(f, x0, args=(), tol=1.0e-6, maxi=48):
  if len(x0) != 2:
    raise Exception("Two guesses needed!")
  x1, x2 = x0
  f1 = f(x1, *args)
  f2 = f(x2, *args)
  for i in range(maxi):
    x3 = x2 - f2 * (x1 - x2) / (f1 - f2)
    f3 = f(x3, *args)
    if f2 * f3 < 0:  # x2 and x3 straddle root
      x1, f1 = x2, f2
      if abs(f2) <= tol:
        return x2
    else:
      f1 = 0.5 * f1  # reduce slope
    x2, f2 = x3, f3
    if abs(f2) <= tol:
      return x2
  raise Exception("Max its reached!")
