from tools import extract_input
from math import prod

FILENAME = "input.txt"
input = extract_input(FILENAME)

TID_FUNC = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: 1 if x[0] > x[1] else 0,
    6: lambda x: 1 if x[0] < x[1] else 0,
    7: lambda x: 1 if x[0] == x[1] else 0,
}


def get_version(packet):
    version = packet[:3]
    return int(version, 2)


def is_literal(packet):
    if packet[3:6] == '100':
        return True
    else:
        return False


def get_tid_func(packet):
    tid = int(packet[3:6], 2)
    return TID_FUNC[tid]


def decode_literal(literal):
    """
    Decodes a literal packet
    Returns version, literal number, rest of packet (if any)
    """
    version = get_version(literal)

    num = ''
    literal = literal[6:]
    while literal[0] != '0':  # While not the last group
        num += literal[1:5]
        literal = literal[5:]
    num += literal[1:5]  
    rest = literal[5:]
    num = int(num, 2)  
    
    if rest == '' or int(rest, 2) == 0:
        return version, num, None
    else:
        return version, num, rest


def decode(packet):
    """
    Decodes ONLY 1 packet.
    Returns: Version/Version_sum, Evaluated literal, rest of the packet (if any)
    """
    if is_literal(packet):
        return decode_literal(packet)
    
    else:
        version_sum = get_version(packet)
        num_list = []
        func = get_tid_func(packet)
        len_id = int(packet[6], 2)
        
        if len_id == 0:
            length = int(packet[7:22], 2)
            subpacket = packet[22: 22+length]
            while subpacket:  # Decodes packets one by one until subpackets empty
                version, num, rest = decode(subpacket)
                version_sum += version
                num_list.append(num)
                subpacket = rest  # Continue from the rest in the next iteration
            return version_sum, func(num_list), packet[22+length:]

        else:
            num_packet = int(packet[7:18], 2)
            subpacket = packet[18:]
            while num_packet > 0:  # Decodes packets one by one until num_packet reached
                version, num, rest = decode(subpacket)
                version_sum += version
                num_list.append(num)
                subpacket = rest  # Continue from the rest in the next iteration
                num_packet -= 1
            return version_sum, func(num_list), rest


# convert hex input to binary, ensuring that no 0s are stripped from the front.
blen = len(input[0]) * 4
input = str(bin(int(input[0], 16)))[2:]
while len(input) < blen:
    input = '0' + input

version_sum, final, _ = decode(input)
print('Part 1: ', version_sum)
print('Part 2: ', final)
