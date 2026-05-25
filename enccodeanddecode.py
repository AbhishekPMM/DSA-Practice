class Codec:

    def encode(self, strs):

        encoded = ""

        for s in strs:

            encoded += str(len(s)) + "#" + s

        return encoded


    def decode(self, s):
        decoded = []
        i = 0
        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decoded.append(word)
            i = j + 1 + length
        return decoded

obj = Codec()
arr = input("Enter strings separated by comma: ").split(",")
encoded = obj.encode(arr)
print("Encoded:", encoded)
decoded = obj.decode(encoded)
print("Decoded:", decoded)