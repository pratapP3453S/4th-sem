# Design a Program for creating machine that accepts three consecutive one.

class ConsecutiveOnesMachine:
    def __init__(self):
        self.state = 0

    def process_input(self, input_str):
        for char in input_str:
            self.transition(char)
            if self.state == 3:    #Accept state
                return True
        return False
    
    def transition(self, char):
        if char == '1':
            self.state += 1
        else:
            self.state = 0

#Example usage
def main():
    machine = ConsecutiveOnesMachine()

    input_str = input("Enter a binary string : ")

    if machine.process_input(input_str):
        print("Accepted : The string contains three consecutive ones.")
    else:
        print("Rejected : The string does not contain three consecutive ones.")
    
if __name__ == "__main__":
    main()