from __future__ import annotations
from enum import Enum
from typing import List, Dict, Tuple, Optional


def uniqueness(container):
    """
    Checks if the container is unique.

    In case of uniqueness it returns True
    """
    return len(container) == len(list(set(container)))


class DFAStatus(Enum):
    UNKNOWN_SYMBOL_ERROR = (0, "There is a symbol in the transmitted string that is not in the alphabet")
    NO_TRANSITIONS = (1, "There are no transitions from the current state")
    NOT_REACHED_FINAL_STATE = (2, "The final states has not been reached")
    REACHED_FINAL_STATE = (3, "The final state has been reached")

    def __init__(self, identifier: int, message) -> None:
        self.id = identifier
        self.message = message


class DFA:
    """
    A class that is a deterministic finite state machine
    """
    __transition_function: Dict[Tuple[str, str], str]

    def __init__(self, states: List[str], alphabet: List[str], transition_table: str,
                 start_state: str, accepted_states: List[str]) -> None:

        DFA.data_valid(states, alphabet, start_state, accepted_states)

        self.__states = states
        self.__alphabet = alphabet
        self.__transition_function = dict()
        self.__make_tf_from_string(transition_table)
        self.__start_state = start_state
        self.__current_state = None
        self.__accepted_states = accepted_states

    @property
    def states(self) -> List[str]:
        return self.__states

    @property
    def alphabet(self) -> List[str]:
        return self.__alphabet

    @property
    def transition_function(self) -> Dict[Tuple[str, str], str]:
        return self.__transition_function

    @property
    def start_state(self) -> str:
        return self.__start_state

    @property
    def current_state(self) -> str:
        return self.__current_state

    @property
    def accepted_states(self) -> List[str]:
        return self.__accepted_states

    @staticmethod
    def data_valid(states: List[str], alphabet: List[str], start_state: str, accepted_states: List[str]) -> None:
        """
        Checking states, alphabet, final states for uniqueness,
        initial state and final states for consistency with states
        """
        if not uniqueness(alphabet):
            raise Exception("Some of symbols is defined twice, but the alphabet must be unique!")
        if not uniqueness(states):
            raise Exception("Some of states is defined twice, but they must be unique!")
        if not uniqueness(accepted_states):
            print("Warning. Final states are not unique.")
        if start_state not in states:
            raise Exception(f"Start state ({start_state}) does not correspond to any of the possible states: {states}!")

        for s in accepted_states:
            if s not in states:
                raise Exception(f"Final state ({s}) does not correspond to any of the possible states: {states}!")

    def __transition_valid(self, transition: str) -> None:
        """
        Checking the transition to permissibility
        """
        current_state, symbol, next_state = transition.split("-")

        if current_state not in self.states:
            raise Exception(f"Transmitted a non-existent state: {current_state}!")

        if next_state not in self.states:
            raise Exception(f"Transmitted a non-existent state {next_state}!")

        if symbol not in self.alphabet:
            raise Exception(f"A character ({symbol}) that is not in the alphabet is passed on!")

        if (value := self.transition_function.get((current_state, symbol))) is not None:
            if value != next_state:
                raise Exception(f"Transition <{current_state}-{symbol}> is defined " +
                                f"twice with different end states ({value} != {next_state})!")
            print(f"Warning! Transition {transition} is defined twice")

    def __transition(self, symbol: str) -> DFAStatus:
        """
        Switching to a new state by the symbol
        """
        if symbol not in self.alphabet:
            return DFAStatus.UNKNOWN_SYMBOL_ERROR

        self.__current_state = self.transition_function.get((self.current_state, symbol), None)

        if self.current_state is None:
            return DFAStatus.NO_TRANSITIONS

        if self.current_state not in self.accepted_states:
            return DFAStatus.NOT_REACHED_FINAL_STATE

        return DFAStatus.REACHED_FINAL_STATE

    def __make_tf_from_string(self, string: str) -> None:
        """
        Forming a transition function from a string of a set format:

        state-symbol-next_state,state2-symbol2-next_state2,...,stateN-symbolN-next_stateN
        """
        transitions = string.split(",")
        for t in transitions:
            self.__transition_valid(t)

            current_state, symbol, next_state = t.split("-")

            self.__transition_function[(current_state, symbol)] = next_state

    def check_ownership(self, string) -> bool:
        """
        String affiliation check
        """
        self.__current_state = self.start_state
        result = None
        for symbol in string:
            result = self.__transition(symbol)
            if result in [DFAStatus.UNKNOWN_SYMBOL_ERROR, DFAStatus.NO_TRANSITIONS]:
                print(f"{string}: Rejected")
                return False

        if DFAStatus.NOT_REACHED_FINAL_STATE == result:
            print(f"{string}: Rejected")
            return False

        print(f"{string}: Accepted")
        return True


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

alphabet_b = ['a', 'b', 'c']
states_b = ['q0', 'q1', 'q2']
accepted_states_b = ['q0', 'q2']
start_state_b = 'q0'
transition_table_b = \
    'q0-a-q1,' \
    'q1-b-q2,' \
    'q2-a-q1,q2-c-q0'


class DFAFactory:

    @staticmethod
    def get_dfa(name: str) -> Optional[DFA]:
        if name == "task a":
            return DFA(states_a, alphabet_a, transition_table_a, start_state_a, accepted_states_a)
        if name == "task b":
            return DFA(states_b, alphabet_b, transition_table_b, start_state_b, accepted_states_b)
        return None
