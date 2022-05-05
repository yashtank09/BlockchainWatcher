from mnemonic import Mnemonic
my_mnemonic = Mnemonic("english")
Word = my_mnemonic.generate(128)

print(Word)