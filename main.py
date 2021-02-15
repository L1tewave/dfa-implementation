from dfa import DFA

# Task a
alphabet = ['0', '1']
states = ['qxx00', 'qx001', 'qx010', 'q0011', 'q0101', 'q1011',
          'q0111', 'q0110', 'q1101', 'q1110', 'qLOCK', ]
accepted_states = ['qxx00', 'qx001', 'qx010', 'q0011', 'q0101',
                   'q1011', 'q0111', 'q0110', 'q1101', 'q1110', ]
start_state = 'qxx00'
transition_table = \
    'qxx00-0-qxx00,qxx00-1-qx001,' \
    'qx001-0-qx010,qx001-1-q0011,' \
    'qx010-0-qxx00,qx010-1-q0101,' \
    'q0011-0-q0110,q0011-1-q0111,' \
    'q0101-0-qx010,q0101-1-q1011,' \
    'q0110-0-qxx00,q0110-1-q1101,' \
    'q0111-0-q1110,q0111-1-qLOCK,' \
    'q1011-0-q0110,q1011-1-qLOCK,' \
    'q1101-0-qx010,q1101-1-qLOCK,' \
    'q1110-0-qxx00,q1110-1-qLOCK'

dfa = DFA(states, alphabet, transition_table, start_state, accepted_states)
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


# Task b
alphabet = ['a', 'b', 'c']
states = ['q0', 'q1', 'q2']
accepted_states = ['q0', 'q2']
start_state = 'q0'
transition_table = \
    'q0-a-q1,' \
    'q1-b-q2,' \
    'q2-a-q1,q2-c-q0'

dfa = DFA(states, alphabet, transition_table, start_state, accepted_states)
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
