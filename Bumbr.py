class Bumbr:
    def __init__(self):
        self.number = list([
            [0, '']                     , # 0
            [0, 'thousand']             , # 1
            [0, 'million']              , # 2
            [0, 'billion']              , # 3
            [0, 'trillion']             , # 4
            [0, 'quadrillion']          , # 5 
            [0, 'quintillion']          , # 6  # 2^64
            [0, 'sextillion']           , # 7 
            [0, 'septillion']           , # 8
            [0, 'octillion']            , # 9
            [0, 'nonillion']            , # 10
            [0, 'decillion']            , # 11 # 2^128
            [0, 'undecillon']           , # 12
            [0, 'duodecillion']         , # 13
            [0, 'tredecillion']         , # 14
            [0, 'quattuordecillion']    , # 15
            [0, 'quinquadecillion']     , # 16
            [0, 'sedecillion']          , # 17
            [0, 'septendecillion']      , # 18
            [0, 'octodecillion']        , # 19
            [0, 'novendecillion']       , # 20
            [0, 'vigintillion']         , # 21
            [0, 'uvigintillion']        , # 22
            [0, 'duovigintillion']      , # 23
            [0, 'tresvigintillion']     , # 24
            [0, 'quattuorvigintillion'] , # 25 # 2^256 
            [0, 'zillion']              , # 26 # tm starts here
        ])
        self.high_index = 0

    def __repr__(self):
        stringe = ''
        new_num = ''
        self.high_index = self.check_highest(self.number)
        for x in range(0, self.high_index+1):
            if x != self.high_index:
                new_num = str(self.number[x][0]).rjust(3, '0')
            else:
                new_num = str(self.number[x][0])
            stringe = '{nn},{s}'.format(nn=new_num, s=stringe)
        return stringe[:-1]

    def q_rep(self):
        if self.high_index == 0:
            return '{}'.format(self.number[0][0])
        return '{h}.{l} {n}'.format(h=self.number[self.high_index][0], l=str(self.number[self.high_index-1][0]), n=self.number[self.high_index][1])

    def add(self, val):
        parsed_vals = val.split(',')
        if len(parsed_vals) > len(self.number):
            for x in range(0, len(self.number)):
                self.number[x][0] = 999
            print('your bumbr is maxed, chief')
            self.high_index = len(self.number) - 1
            return 0 
        for x in range(0, len(parsed_vals)):
            self.add_part(x, int(parsed_vals[len(parsed_vals) - (x+1)])) 
        self.high_index = self.check_highest(self.number)

    def sub(self, val):
        parsed_vals = val.split(',')
        if len(parsed_vals) > len(self.number) or self.check_highest(parsed_vals) > self.check_highest(self.number):
            for x in range(0, len(self.number)):
                self.number[x][0] = 0
            print('your bumbr just got slammed, killer. welcome back to 0')
            self.high_index = 0
            return 0
        for x in range(0, len(parsed_vals)):
            self.sub_part(x, int(parsed_vals[len(parsed_vals) - (x+1)]))


    def add_part(self, index, val):
        new_val = val + self.number[index][0]
        if new_val < 1000:
            self.number[index][0] = new_val
            return 0 
        self.add_part(index+1, 1)
        self.number[index][0] = new_val - 1000
        return 0

    def sub_part(self, index, val):
        if val > self.number[index][0]:
            self.sub_part(index+1, 1)
            self.number[index][0] = 1000 + self.number[index][0] - val
            return 0
        self.number[index][0] = self.number[index][0] - val
        return 0

    def check_highest(self, bumbr):
        index = 0
        for x in range(1, len(bumbr) + 1):
            if int(bumbr[len(bumbr) - x][0]) > 0:
                index = len(bumbr) - x
                return index
        return index

if __name__ == '__main__':
    b = Bumbr()
    b.add('349,623')
    print(b)
    b.sub('39,823')
    print(b)
    b.sub('150,212')
    print(b)

