def RemovingprefixOfWord(setofprefixs, w):
    for p in setofprefixs:
        if w.startswith(p):
            yield w[len(p):]

def CodeWordprefix(setofprefixs, ws):
    setofsuffixes = set()
    for w in ws:
        for q in RemovingprefixOfWord(setofprefixs, w):
            setofsuffixes.add(q)
    if setofsuffixes:
        print("setofsuffixes = ", str(setofsuffixes))
    return setofsuffixes

def IsTheCodeUniquelyDeciperable(cs):
    s = CodeWordprefix(cs, cs)  # S1
    # Check for non-trivial prefix overlaps ('' from distinct codewords)
    has_overlap = False
    for w1 in cs:
        for w2 in cs:
            if w1 != w2 and w2.startswith(w1):
                has_overlap = True
                break
    if '' in s and has_overlap:
        print('Prefix overlap in S1 → not uniquely decodable.')
        return False
    s = {x for x in s if x != ''}  # Filter '' for next steps
    if not s and not has_overlap:
        print('Uniquely decipherable (no overlaps).')
        return True
    previous_sets = {frozenset(cs)}
    while True:
        if s & cs:
            for x in s & cs:
                print(f'Dangling suffix: {x}')
            return False
        t = CodeWordprefix(cs, s) | CodeWordprefix(s, cs)
        if '' in t:
            print('Empty suffix in later set → not uniquely decodable.')
            return False
        if not t or frozenset(t) in previous_sets:
            print('Uniquely decodable.')
            return True
        previous_sets.add(frozenset(t))
        s = t

if __name__ == '__main__':
    SetOfCodewords = {'xxxy', 'yyxx', 'xxxyy', 'xyyx', 'yyyyx', 'xxyyx', 'yxyxyy', 'xyx'}
    print('The Set of Codewords', SetOfCodewords)
    IsTheCodeUniquelyDeciperable(SetOfCodewords)
    print("\nTest case {'0', '01'}:")
    IsTheCodeUniquelyDeciperable({'0', '01'})
    print("\nTest case {'0', '10', '110'}:")
    IsTheCodeUniquelyDeciperable({'0', '10', '110'})