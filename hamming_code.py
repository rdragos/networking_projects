
def is_power_of_two(x):
    return (x & (x - 1)) == 0

def calculate_log(num):
    log = 0
    while num > 0:
        num >>= 1
        log += 1
    return log


class Decoder(object):

    wrong_position = 0

    def __init__(self, binary_data):
        self.data = [int(bit) for bit in binary_data]

    def fetch_wrong_position(self):
        index_parity = 1
        while index_parity <= len(self.data):
            partial_parity = self.data[index_parity - 1]
            for idx_bit in range(index_parity, len(self.data)):
                if index_parity & (idx_bit+1):
                    partial_parity ^= (self.data[idx_bit])

            if partial_parity != 0:
                self.wrong_position |= index_parity

            index_parity <<= 1

    "Assuming that meaning in life is to find the wrong encoded bit"
    def meaning_in_life(self):
        if (self.wrong_position == 0):
            return "You're lucky, no noise here"
        else:
            return "Not so lucky, noise on bit %s", self.wrong_position
class Encoder(object):

    def __init__(self, binary_data):
        self.data = binary_data

    def encode(self):
        self.encoded_data = []

        parity_bits = [0] * (calculate_log(len(self.data)) + 2)

        # see the parity of each position
        idx_bit = 0
        total_index = 1
        idx_parity = 0

        while idx_bit < len(self.data):

            if is_power_of_two(total_index):
                self.encoded_data.append(0)
            else:
                self.encoded_data.append(int(self.data[idx_bit]))
                idx_bit += 1

            total_index += 1
        # set the parity bits after encoding

        index_parity = 1
        while index_parity <= len(self.encoded_data):
            partial_parity = 0
            for idx_bit in range(index_parity, len(self.encoded_data)):
                if index_parity & (idx_bit+1):
                    partial_parity ^= (self.encoded_data[idx_bit])

            self.encoded_data[index_parity - 1] = partial_parity
            index_parity <<= 1

    def see_encoded(self):
        return "Encoded string looks like this", self.encoded_data

def main():
    E = Encoder('1011')
    E.encode()
    print (E.see_encoded())
    encoded_string = E.see_encoded()[1]
    D = Decoder(encoded_string)
    D.fetch_wrong_position()
    print (D.meaning_in_life())

main()
