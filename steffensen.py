# Steffensen's method (fixed point acceleration method).


def fixpoint(f, p0, args=(), tol=1e-6, maxi=48):
  for i in range(maxi):
    p1 = f(p0, *args)
    p2 = f(p1, *args)
    dp = p1 - p0
    if abs(dp) < tol:
      return 0.5 * (p1 + p0)
    p = p0 - dp * dp / (p2 - 2.0 * p1 + p0)
    p0 = p
  raise Exception('Max its reached!')
