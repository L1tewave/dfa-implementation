# dfa-implementation

Python version >=3.8 is required to run this program

-----

A class representing a finite automaton is implemented. 
As an example, two finite automata are created, which can also be run with JFLAP.

-----
Sample program launch:
```
 $ python main.py c
 The type of finite state machine you have selected 
 is not included in the available ones: ['a', 'b']
 Try again!
 
 $ python main.py b
 
 Your choice is: A nondeterministic finite automaton with 
 the number of states not exceeding 3 for the language {ab, abc}*.
 
 Note: Press <Ctrl+C> or <Ctrl+Z> to exit from program
 
 >> ababc
 Accepted
 >> ababcb
 Rejected
 >> ^Z
 Bye
 
 $ |
```
