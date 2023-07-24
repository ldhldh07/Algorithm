def T_to_S(s, t, len_s, len_t):
    if len_s == len_t:
        return s == t
    if t[-1] == 'A' and T_to_S(s, t[:-1], len_s, len_t-1):
        return 1
    if t[0] == 'B' and T_to_S(s, t[:0:-1], len_s, len_t-1):
        return 1
    return 0

S, T = input(), input()
len_S, len_T = len(S), len(T)

print(T_to_S(S, T, len_S, len_T))
