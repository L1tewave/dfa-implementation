import sys

from dfa.examples import PREDEFINED_FINITE_AUTOMATA, AVAILABLE_FINITE_AUTOMATA_TYPES, PFA_TYPE_INFO

# Program exit codes
TOO_FEW_ARGS = -2
UNDEFINED_FINITE_AUTOMATON_TYPE = -1
ALRIGHT = 0

REQUIRED_ARGC = 2

if __name__ == "__main__":
    if len(sys.argv) != REQUIRED_ARGC:
        print("Required call format: python main.py <type>\n"
              "Example: python main.py a\n"
              "Try again!")
        sys.exit(TOO_FEW_ARGS)

    finite_automation_type = sys.argv[1].lower()

    if finite_automation_type not in AVAILABLE_FINITE_AUTOMATA_TYPES:
        print(f"The type of finite state machine you have selected is not included "
              f"in the available ones: {AVAILABLE_FINITE_AUTOMATA_TYPES}\nTry again!")
        sys.exit(UNDEFINED_FINITE_AUTOMATON_TYPE)

    print(f"\nYour choice is: {PFA_TYPE_INFO[finite_automation_type]}\n")
    print("Note: Press <Ctrl+C> or <Ctrl+Z> to exit from program")  # May not work in IDE, try Ctrl+F2

    finite_automaton = PREDEFINED_FINITE_AUTOMATA[finite_automation_type]

    try:
        while True:
            string_to_check = input(">> ")
            finite_automaton.check_ownership(string_to_check)
    except KeyboardInterrupt:
        print()
    except EOFError:
        pass
    finally:
        print("Bye")
        sys.exit(ALRIGHT)
