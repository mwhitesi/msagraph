from msa import MSA

def main(msa_f):
    msa = MSA()

    msa.load(msa_f)

if __name__ == "__main__":
    main('data/test/example.msa')
    print('ok')
