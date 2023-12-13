# Write a program for generating derivation sequence / language for the given sequence of productions

def generate_derivation_sequence(start_symbol, production_rules, depth):
    sequence = [start_symbol]

    for _ in range(depth):
        current_sequence = sequence[-1]
        new_sequence = apply_production_rules(current_sequence, production_rules)
        sequence.append(new_sequence)
    return sequence

def apply_production_rules(sequence, production_rules):
    result = ""
    for symbol in sequence:
        if symbol in production_rules:
            result += production_rules[symbol]
        else:
            result += symbol
    return result

#Example usage:
start_symbol = 'S'
production_rules = {'S': 'AB', 'A': 'aA', 'B': 'bB'}
depth = 5

derivation_sequence = generate_derivation_sequence(start_symbol, production_rules, depth)

for i, step in enumerate(derivation_sequence):
    print(f"Step {i+1} : {step}")