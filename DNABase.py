class DNABase:
    bases = ['adenine', 'cytosine', 'guanine', 'thymine']

    def __init__(self, nucleotide):
        self.base = nucleotide

    def get_nucleotide(self):
        return self._nucleotide

    def set_nucleotide(self, base):
        if base.lower() not in self.bases and base.lower() not in list(map(lambda x: x[0], self.bases)):
            raise ValueError(f"Invalid Base: {base} provided")

        else:
            self._nucleotide = "".join(list(filter(lambda x: x[0] == base[0], self.bases)))

    base = property(fget=get_nucleotide, fset=set_nucleotide)

d1 = DNABase('c')

# d2 = DNABase('h')
print(d1.base)
d1.base='a'
print(d1.base)

print(d1.__dict__)
