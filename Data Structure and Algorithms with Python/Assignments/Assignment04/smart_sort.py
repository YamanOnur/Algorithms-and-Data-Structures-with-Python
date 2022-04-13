print("Note that smart_sort should be used in the following manner:"
      "\nseq = sequence_input"
      "\nsmart_sort(seq)"
      "\nprint(seq)")

def insertion_sort(S):
    for i in range(1, len(S)):
        current = S[i]
        j = i
        while j > 0 and S[j - 1] > current:
            S[j] = S[j - 1]
            j -= 1
            S[j] = current

def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i += 1
        else:
            S[i + j] = S2[j]
            j += 1

def merge_sort(S):
    n = len(S)
    if n < 2:
        return
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)

def smart_sort(S):
    if len(S) < 50:
        try:
            insertion_sort(S)
        except TypeError:
            raise TypeError("All elements of sequence must be same type")
    else:
        try:
            merge_sort(S)
        except TypeError:
            raise TypeError("All elements of sequence must be same type")