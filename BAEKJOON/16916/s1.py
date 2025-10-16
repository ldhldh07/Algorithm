import sys

def compute_lps(p):
    lsp = [0] * len(p)
    length = 0
    i = 1
    while i < len(p):
        if p[i] == p[length]:
            length += 1
            lsp[i] = length
            i += 1
            continue
        if length > 0:
            length = lsp[length - 1]
            continue
        lsp[i] = 0
        i += 1
    return lsp

def kmp(s, p):
    lps = compute_lps(p)
    i = j = 0
    while i < len(s):
        if s[i] == p[j]:
            i += 1
            j += 1
            if j == len(p):
                return True
            continue
        if j > 0:
            j = lps[j - 1]
            continue
        i += 1
    return False

S = sys.stdin.readline().strip()
P = sys.stdin.readline().strip()
print(1 if kmp(S, P) else 0)