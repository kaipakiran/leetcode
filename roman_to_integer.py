class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {}
        roman['I'] = 1
        roman['V'] = 5
        roman['X'] = 10
        roman['L'] = 50
        roman['C'] = 100
        roman['D'] = 500
        roman['M'] = 1000
        number_list= []
        prev_char = ''
        for char in s:
            concat = prev_char+char
            if concat  in ['IV','IX','XL','XC','CD','CM']:
                sub = number_list[-1]
                number_list.pop()
                number_list.append(roman[char] - sub)
            else:
                number_list.append(roman[char])
            prev_char=char
        return sum(number_list)
                