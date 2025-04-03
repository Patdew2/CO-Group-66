import sys
memory = {}
reg = [0] * 32
reg[2] = 380  #register 2 is sp (initialized to 380)
PC = 0

INPUT_FILE = str(sys.argv[1]) 
OUTPUT_FILE = str(sys.argv[2])

def sign_extend(value, bits):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

def write_memory():
    with open(OUTPUT_FILE, 'a') as f:
        for addr in range(0x00010000, 0x00010080, 4):
            value = memory.get(addr, 0)
            f.write(f"0x{addr:08X}:0b{value:032b}\n")

def write_state():
    with open(OUTPUT_FILE, 'a') as f:
        f.write(f"0b{PC:032b} ")
        for r in reg:
            f.write(f"0b{r:032b} ")
        f.write("\n")

# Clear output file
with open(OUTPUT_FILE, 'w') as f:
    f.write("")

# Read input instructions
with open(INPUT_FILE, 'r') as f:
    instr = f.read().strip().splitlines()

pointer = 0
while 0 <= pointer < len(instr):
    i = instr[pointer]
    opcode = int(i[25:32], 2)

    if opcode == 0b0100011:  # SW
            rs2 = int(i[7:12], 2)
            rs1 = int(i[12:17], 2)
            funct3 = int(i[17:20], 2)
            imm = i[0:7] + i[20:25]
            imm = sign_extend(int(imm, 2), 12)
            if funct3 == 0b010:
                addr = (reg[rs1] + imm) & 0xFFFFFFFF
                memory[addr] = reg[rs2]
            pointer += 1
            PC += 4

        else:
            print(f"[ERROR] Unsupported opcode: {opcode:07b}")
            break
        reg[0] = 0
        write_state()  # write memory state
write_memory()