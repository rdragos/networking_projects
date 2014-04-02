"Consider using CRC-32"


def BinToInt(x):
    answer = int(x[0])
    for idx_bit in range(1,len(x)):
        answer <<= 1
        answer |= int(x[idx_bit])
    return answer
class CRC32(object):

    " No magic here "
    polynomial_coefficents = [dict({
        32: 1, 26: 1, 23: 1, 22: 1,
        16: 1, 12: 1, 11: 1, 10: 1,
        8: 1, 7: 1, 5: 1, 4: 1,
        2: 1, 1: 1, 0: 1,
        }),
        dict({0:1},)
        ]
    def __init__(self, text, maxbit):
        sentence_in_binary = "".join(
                bin(ord(letter))[2:] for letter in text)

        self.final_poly = 0
        for key in self.polynomial_coefficents[0]:
            self.final_poly |= (1 << (maxbit - key))

        rolling_hash = BinToInt("".join( [_ for _ in reversed(sentence_in_binary[:maxbit+1])] ))
        rolling_hash = rolling_hash ^ self.final_poly

        for idx_bit in range(maxbit+1, len(sentence_in_binary)):
            rolling_hash >>= 1
            rolling_hash |= (1 << maxbit) * (int(sentence_in_binary[idx_bit]))
            rolling_hash ^= self.final_poly

        print (bin(rolling_hash)[2:])
def main():
    C = CRC32("Just a random text",32)

main()
