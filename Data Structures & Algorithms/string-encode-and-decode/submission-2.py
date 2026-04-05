class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        delimiter = "UTF*!)@()*$*&#(*FOKDHFS&#(*WUF))"
        for word in strs:
            encoded += delimiter
            encoded += word
        return encoded


    def decode(self, s: str) -> List[str]:
        delimiter = "UTF*!)@()*$*&#(*FOKDHFS&#(*WUF))"
        parts = s.split(delimiter)
        return parts[1:]
