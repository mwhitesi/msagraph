import pandas as pd

from io import StringIO
from csv import writer
from itertools import groupby

def fasta_iter(ff):

    fh = open(ff)
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))

    for header in faiter:
        headerStr = header.__next__()[1:].strip()
        seq = "".join(s.strip() for s in faiter.__next__())
        seqSeries = pd.Series(list(seq))

        yield (headerStr, seqSeries)



class MSA:
    def __init__(self):
        None



    def load(self, f):

        seqs = []
        headers = []
        for ff in fasta_iter(f):
            h, s = ff
            seqs.append(s)
            headers.append(s)

        self.df = pd.DataFrame(seqs)
        self.ids = headers
