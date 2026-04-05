class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for word in strs:
            encode += str(len(word)) + "#" + word 
        print(encode)
        return encode

    def decode(self, s: str) -> List[str]:
        decoded, count, size = [], 0, len(s)
        while len(s) > 0:
            if s[count] == "#":
                wordlen = int(s[:count])
                decoded.append(s[count + 1: count + wordlen + 1])
                s = s[count + wordlen + 1:]
                count = 0
                continue
            count += 1
        return decoded



            

