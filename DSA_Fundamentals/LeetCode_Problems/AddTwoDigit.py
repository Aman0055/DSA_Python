class solution:
    def AddTwoDigit(self, num:int) ->int:

        if num == 0:
            return 0
        else :
            return 1 + (num -1) % 9
obj = solution()
print(obj.AddTwoDigit(-111))


