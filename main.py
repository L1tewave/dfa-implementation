from dfa import DFAFactory

dfa = DFAFactory.get_dfa("task a")
strings_to_check = [
    "1",
    "11101",
    "11011",
    "11010110",
    "1100011100011011",
    "110001110001101",
    "1100011101",
    "10001110011011",
    "1000111011001",
    "000011011",
    "",
]

print("Task a:")
for string in strings_to_check:
    dfa.check_ownership(string)


dfa = DFAFactory.get_dfa("task b")
strings_to_check = [
    "abcababc",
    "abcababca",
    "abcabcacb",
    "a",
    "",
]

print("\nTask b:")
for string in strings_to_check:
    dfa.check_ownership(string)
