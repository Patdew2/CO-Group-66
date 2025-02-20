def decimal_to_binary(n, num_bits=12):
    if n < 0:
        n = (1 << num_bits) + n
    return format(n & ((1 << num_bits) - 1), f'0{num_bits}b')

s_type_func3 = {"sw": "010"}
s_type_opcode = {"sw": "0100011"}

register_map = {"t1": "01001", "t2": "01010", "t3": "01011", "t4": "01100", "t5": "01101", "t6": "01110"}

def assemble_s_type_instruction(parts):
    if len(parts) != 4 or parts[1] not in register_map or parts[3] not in register_map:
        raise ValueError("Invalid S-Type instruction format")

    immediate_value = decimal_to_binary(int(parts[2]), 12)
    func3 = s_type_func3[parts[0]]
    opcode = s_type_opcode[parts[0]]

    return f"{immediate_value[:7]}{register_map[parts[1]]}{register_map[parts[3]]}{func3}{immediate_value[7:]}{opcode}"

def execute_instructions():
    instructions = ["sw t1, 8, t2", "sw t3, -4, t4", "sw t5, 12, t6"]
    
    for instruction in instructions:
        parts = instruction.replace(',', '').split()
        try:
            machine_code = assemble_s_type_instruction(parts)
            print(machine_code)
        except ValueError as error:
            print(f"Error: {error}")

execute_instructions()
