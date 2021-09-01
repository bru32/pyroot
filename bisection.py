# Bisection method.


def fsolve(f, x, args=(), tol=1e-4, maxi=98):
  a, b = x
  for i in range(maxi):
    m = 0.5 * (a + b)
    fm = f(m, *args)
    fa = f(a, *args)
    if (fm > 0 > fa) or (fm < 0 < fa):
      b = m
    else:
      a = m
    if (b - a) < tol:
      return 0.5 * (a + b)
  raise Exception('Max its reached!')
