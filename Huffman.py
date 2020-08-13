
string = 'AAABBBCCD'

class Drvo(object):

    def __init__(self, lijevi=None, desni=None):
        self.left = lijevi
        self.right = desni

    def dijete(self):
        return (self.left, self.right)

    def cvor(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huffmanKodiranje(cvor, left=True, binarniZapis=''):
    if type(cvor) is str:
        return {cvor: binarniZapis}
    (l, r) = cvor.dijete()
    d = dict()
    d.update(huffmanKodiranje(l, True, binarniZapis + '0'))
    d.update(huffmanKodiranje(r, False, binarniZapis + '1'))
    return d

def prebroj_elemente(ulaz):
    novi=ulaz.upper()
    print("Ulaz: "+novi)
    elementi = dict()
    for element in novi:
        if element in elementi:
            elementi[element] += 1
        else:
            elementi[element] = 1

    elementi = {key: value for key, value in elementi.items() if value > 0}
    sortiranoPrebrojano = sorted(elementi.items(), key=lambda i: i[1], reverse=True)
    return sortiranoPrebrojano

freq=prebroj_elemente(string)
cvorovi = freq

while len(cvorovi) > 1:
    (key1, c1) = cvorovi[-1]
    (key2, c2) = cvorovi[-2]
    cvorovi = cvorovi[:-2]
    cvor = Drvo(key1, key2)
    cvorovi.append((cvor, c1 + c2))

    cvorovi = sorted(cvorovi, key=lambda x: x[1], reverse=True)

huffmanCode = huffmanKodiranje(cvorovi[0][0])
print("Kodirana rečenica: ", end="")
for i in string:
    print('%s' % (huffmanCode[i]), end="")
print(' ')
for (slovo, f) in freq:
    print(' %-2r->%2s' % (slovo, huffmanCode[slovo]))

neKompresovaniBit=len(string) * 8
bRezultat=dict()
for (i,f) in freq:
    bRezultat[i]=len(huffmanCode[i])
bRezultat = {key: value for key, value in bRezultat.items() if value > 0}

suma=0
for i in string:
    suma+=bRezultat[i];
print("Stepen kompresije: "+ str(neKompresovaniBit/suma))