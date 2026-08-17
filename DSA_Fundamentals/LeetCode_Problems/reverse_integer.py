# Reverse integer problem from LeetCode of 32 - bit 

class solution:

    def reverse_integer(self, x : int) -> int:

        INT_MIN , INT_MAX = -2**31 , 2 **31 -1
        sign = -1 if x < 0 else 1
        x = abs(x)
        reverse_num = 0
        while x != 0:
            digit = x % 10
            x //= 10
            reverse_num = reverse_num * 10 + digit
            if reverse_num > INT_MAX:
                return 0
        return sign * reverse_num

sol = solution()
for x in [123, -123, 10, 0, 123344456677776]:
    print(f"Reverse of {x} is : {sol.reverse_integer(x)}")

    