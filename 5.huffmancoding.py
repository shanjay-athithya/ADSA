# Existing code for encoding and building the Huffman tree
string = "ABABCACABAAA"
freq = {}
for i in string:
    freq[i] = string.count(i)

temp = sorted(freq.items(), key=lambda x: x[1])


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)


while len(temp) > 1:
    left, right = temp[0], temp[1]
    n = Node(left[0], right[0])
    temp = temp[2:]
    temp.append((n, left[1] + right[1]))
    temp = sorted(temp, key=lambda x: x[1])


def huffman(node, bindtr=""):
    if isinstance(node, str):
        return {node: bindtr}
    d = {}
    d.update(huffman(node.left, bindtr=bindtr + '0'))
    d.update(huffman(node.right, bindtr=bindtr + '1'))
    return d


huffman_code = huffman(temp[0][0])

# Decoding function
def decode(encoded_string, node):
    decoded_string = ""
    current_node = node
    for bit in encoded_string:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if isinstance(current_node, str):
            decoded_string += current_node
            current_node = node  # Reset to the root
    return decoded_string

# Example usage:
encoded_string = ''.join(huffman_code[char] for char in string)
print("Encoded string:", encoded_string)

decoded_string = decode(encoded_string, temp[0][0])
print("Decoded string:", decoded_string)
