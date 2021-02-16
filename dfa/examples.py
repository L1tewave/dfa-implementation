from typing import Dict

from dfa.core import DFA

alphabet_a = ['0', '1']
states_a = ['qxx00', 'qx001', 'qx010', 'q0011', 'q0101', 'q1011',
            'q0111', 'q0110', 'q1101', 'q1110', 'qLOCK', ]
accepted_states_a = ['qxx00', 'qx001', 'qx010', 'q0011', 'q0101',
                     'q1011', 'q0111', 'q0110', 'q1101', 'q1110', ]
start_state_a = 'qxx00'
transition_table_a = \
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

dfa = DFA(states_a, alphabet_a, transition_table_a, start_state_a, accepted_states_a)

alphabet_b = ['a', 'b', 'c']
states_b = ['q0', 'q1', 'q2']
accepted_states_b = ['q0', 'q2']
start_state_b = 'q0'
transition_table_b = 'q0-a-q1,q1-b-q2,q2-a-q1,q2-c-q0'

nfa = DFA(states_b, alphabet_b, transition_table_b, start_state_b, accepted_states_b)

PREDEFINED_FINITE_AUTOMATA: Dict[str, DFA] = {"a": dfa, "b": nfa}
# Predefined finite automata types
PFA_TYPES = list(PREDEFINED_FINITE_AUTOMATA.keys())
# Predefined finite automata info
PFA_INFO = {
    "a": "A deterministic finite automaton admitting in the alphabet {0, 1} all strings "
         "in which each block of five consecutive characters contains at least two 0's.",
    "b": "A nondeterministic finite automaton with the number of states not exceeding 3 "
         "for the language {ab, abc}*."
}
