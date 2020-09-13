class Solution:
    def isAlienSorted(self, words: list, order: str):
        order_index = {}
        for i,o in enumerate(order,1):
            order_index[o]=i
        #print(order_index)
        words_index = []
        for word in words:
            word_index = []
            for l in word:
                word_index.append(order_index[l])
            words_index.append(word_index)
        #print(words_index)
        if words_index == sorted(words_index):
            return True
        else:
            return False

if __name__ == "__main__":
    a = Solution()
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(a.isAlienSorted(words,order))
    words = ["word","world","row"]; order = "worldabcefghijkmnpqstuvxyz"
    print(a.isAlienSorted(words,order))