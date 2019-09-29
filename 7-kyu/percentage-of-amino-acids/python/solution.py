def aa_percentage(prot_seq, acids=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    prot_seq = list(prot_seq)
    count = sum(prot_seq.count(acid) for acid in acids)
    return round(count / len(prot_seq) * 100)