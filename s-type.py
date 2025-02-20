def int_to_bin(n, bits=12):
    if n < 0:
        n = (1 << bits) + n
    return format(n & ((1 << bits) - 1), f'0{bits}b')

func3_s = {"sw": "010"}
opcode_s = {"sw": "0100011"}

registers = {"t1": "01001", "t2": "01010", "t3": "01011", "t4": "01100", "t5": "01101", "t6": "01110"}

def convert_s_type(parts):
    if len(parts) != 4 or parts[1] not in registers or parts[3] not in registers:
        raise ValueError("Invalid S-Type instruction")
    imm_val = int_to_bin(int(parts[2]), 12)
    return f"{imm_val[:7]}{registers[parts[1]]}{registers[parts[3]]}{func3_s[parts[0]]}{imm_val[7:]}{opcode_s[parts[0]]}"

def main():
    instructions = ["sw t1, 8, t2", "sw t3, -4, t4", "sw t5, 12, t6"]
    for inst in instructions:
        parts = inst.replace(',', '').split()
        try:
            print(convert_s_type(parts))
        except ValueError as e:
            print(f"Error: {e}")

main()