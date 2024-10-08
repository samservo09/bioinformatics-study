# Count protein sequence
def count_protein(seq):
    # Remove any whitespace characters (spaces, newlines, tabs, etc.)
    cleaned_sequence = ''.join(seq.split())
    return len(cleaned_sequence)

seq = "MTAKMETTFYDDALNASFLPSESGPYGYSNPKILKQSMTLNLAD PVGSLKPHLRAKNSDLLTSPDVGLLKLASPELERLIIQSSNGHITTTPTPTQFLCPKN VTDEQEGFAEGFVRALAELHSQNTLPSVTSAAQPVNGAGMVAPAVASVAGGSGSGGFS ASLHSEPPVYANLSNFNPGALSSGGGAPSYGAAGLAFPAQPQQQQQPPHHLPQQMPVQ HPRLQALKEEPQTVPEMPGETPPLSPIDMESQERIKAERKRMRNRIAASKCRKRKLER IARLEEKVKTLKAQNSELASTANMLREQVAQLKQKVMNHVNSGCQLMLTQQLQTF"

print(count_protein(seq))

