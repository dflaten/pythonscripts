#!/usr/bin/env python3
from learning.state_machine.tranisitions import Transitions 
class StateMachine:
    def __init__(self):
        self.states = {}  # Dictionary to store states and their transitions
        self.current_state = None  # Current state of the machine

    def add_state(self, state, transitions):
        self.states[state] = transitions

    def set_state(self, state):
        self.current_state = state

    def process(self, input_data):
        if self.current_state is None:
            print("Error: No initial state set.")
            return

        if input_data in self.states[self.current_state]:
            self.current_state = self.states[self.current_state][input_data]
            print(f"Transitioned to state: {self.current_state}")
        else:
            print("Invalid input for the current state.")
if __name__ == "__main__":
    # Create an instance of the state machine
    sm = StateMachine()

    # Define states and transitions
    sm.add_state("A", {"input_1": "B", "input_2": "C"})
    sm.add_state("B", {"input_3": "A"})
    sm.add_state("C", {"input_4": "A"})

    # Set initial state
    sm.set_state("A")

    # Process inputs
    sm.process("input_1")  # Transition to state B
    sm.process("input_3")  # Transition back to state A
    sm.process("input_4")  # Transition to state A
    sm.process("invalid_input")  # Invalid input