##!FAIL: SideEffectWarning[append]@4:4
def f(ll : List[List[int]]) -> int:
    """"""
    (ll + [])[0].append(1)
    return 0
