
def T_to_S(s, t, len_s, len_t):
    if len_s == len_t:
        return 1 if s == t else 0

    result = 0
    if t[-1] == 'A':
        result = T_to_S(s, t[:-1], len_s, len_t-1)
    if t[0] == 'B':
        result = result or T_to_S(s, t[::-1][:-1], len_s, len_t-1)
        
    return result

S, T = input(), input()
len_S, len_T = len(S), len(T)

print(T_to_S(S, T, len_S, len_T))