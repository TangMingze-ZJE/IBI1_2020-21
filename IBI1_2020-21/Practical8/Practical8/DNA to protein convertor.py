Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
seq ='ATGCGACTACGATCGAGGGCC'
ans= ''
code={
	"TTT":'F',"TTC":'F',"TTA":'L',"TTG":'L',
	"TCT":'S',"TCC":'S',"TCA":'S',"TCG":'S',
	"TAT":'Y',"TAC":'Y',"TAA":'O',"TAG":'U',
	"TGT":'C',"TGC":'C',"TGA":'X',"TGG":'W',
	"CTT":'L',"CTC":'L',"CTA":'L',"CTG":'L',
	"CCT":'P',"CCC":'P',"CCA":'P',"CCG":'P',
	"CAT":'H',"CAC":'H',"CAA":'Q',"CAG":'Z',
	"CGT":'R',"CGC":'R',"CGA":'R',"CGG":'R',
	"ATT":'I',"ATC":'I',"ATA":'J',"ATG":'M',
	"ACT":'T',"ACC":'T',"ACA":'T',"ACG":'T',
	"AAT":'N',"AAC":'B',"AAA":'K',"AAG":'K',
	"AGT":'S',"AGC":'S',"AGA":'R',"AGG":'R',
	"GTT":'V',"GTC":'V',"GTA":'V',"GTG":'V',
	"GCT":'A',"GCC":'A',"GCA":'A',"GCG":'A',
	"GAT":'D',"GAC":'D',"GAA":'E',"GAG":'E',
	"GGT":'G',"GGC":'G',"GGA":'G',"GGG":'G',
}
for i in range(0,len(seq),3):
	ans = ans + code[seq[i:i+3]]
print(ans)
