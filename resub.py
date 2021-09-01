# Successive re-substitution (most basic fixed point method).


def fixpoint(f, x, args=(), tol=1e-5, maxi=98):
  for i in range(maxi):
    y = f(x, *args)
    if abs(x-y) <= tol:
      return y
    x = y
  raise Exception("Max its reached!")
