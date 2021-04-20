seq="ATGATATAG"
def DNA_reverse(sequence):
    return sequence[::-1]

def DNA_complement1(sequence):
    comp_dict = {
    "A":"T",
    "T":"A",
    "G":"C",
    "C":"G",
}
sequence_list = list(sequence)
sequence_list = [comp_dict[base] for base in sequence_list]
string = ''.join(sequence_list)
return string

