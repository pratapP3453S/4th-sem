# Design a Program for creating machine that accepts the string always ending with 101.

class StringAcceptanceMachine:
    def __init__(self):
        self.transitions = {
            'q0' : {'0': 'q0', '1': 'q1'},
            'q1' : {'0': 'q2', '1': 'q1'},
            'q2' : {'0': 'q0', '1': 'q3'},
            'q3' : {'0': 'q0', '1': 'q1'}
        }
        self.accepting_state = 'q3'
        self.current_state = 'q0'

    def process_input(self, input_string):
        for symbol in input_string:
            if symbol not in {'0', '1'}:
                return False #Reject if the input contains symbols not in the alphabet
            self.current_state = self.transitions[self.current_state].get(symbol, 'q0')

        return self.current_state == self.accepting_state
    
def main():
    machine = StringAcceptanceMachine()

    #Example strings to test 
    test_string1 = "110101"
    test_string2 = "010101"
    test_string3 = "101010"

    #Test and print results
    print("Test String 1 : ",machine.process_input(test_string1))
    print("Test String 2 : ",machine.process_input(test_string2))
    print("Test String 3 : ",machine.process_input(test_string3))

if __name__ == "__main__":
    main()