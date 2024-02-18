import os

lines = []

arm_funcs = [
    "0x08000000",
    "0x080000c0",
]

def write_config():
     with open('sa1.cfg', 'w') as config:
        config.write("\n".join(lines))

def test():
    return os.system("./gbadisasm sa1.gba -c sa1.cfg > sa1.s")

with open('sa1_functions.csv') as functions_file:
    for line in functions_file.readlines():
        parsed = line.split(',')[1].split('\"')[1]
        address = f"0x{parsed}"
        print(address)

        type = "thumb_func" if address not in arm_funcs else "arm_func"
        lines.append(f"{type} {address} sub_{parsed[1:].upper()}")

    write_config()
    
    error = test()
    if error:
        print(error)
