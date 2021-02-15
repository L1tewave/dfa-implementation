import sys

from dfa import PREDEFINED_FINITE_AUTOMATA, TASK_INFO

AVAILABLE_FINITE_AUTOMATA_TYPES = ["a", "b"]

# Program exit codes
TOO_FEW_ARGS = -2
UNDEFINED_FINITE_AUTOMATON_TYPE = -1
ALRIGHT = 0

REQUIRED_ARGC = 2

if __name__ == "__main__":
    if len(sys.argv) != REQUIRED_ARGC:
        print("Required call format: main.py (a|b)\nTry again!")
        sys.exit(TOO_FEW_ARGS)

    finite_automation_type = sys.argv[1]

    if finite_automation_type.lower() not in AVAILABLE_FINITE_AUTOMATA_TYPES:
        print(f"The type of finite state machine you have selected is not included "
              f"in the available ones: {AVAILABLE_FINITE_AUTOMATA_TYPES}\nTry again!")
        sys.exit(UNDEFINED_FINITE_AUTOMATON_TYPE)

    task = "task " + finite_automation_type

    finite_automaton = PREDEFINED_FINITE_AUTOMATA[task]

    print(f"\nYour choice is: {TASK_INFO[task]}\n")
    print("Note: Press <Ctrl+C> or <Ctrl+Z> to exit from program")  # May not work in IDE

    try:
        while True:
            string_to_check = input(">> ")
            finite_automaton.check_ownership(string_to_check)
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
    finally:
        print("Bye")
        sys.exit(ALRIGHT)
