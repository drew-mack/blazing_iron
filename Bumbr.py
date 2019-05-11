class Bumbr:
    def __init__(self):
        self.number = list([
            [0, ''],
            [0, 'thousand'],
            [0, 'million'],
            [0, 'billion'],
            [0, 'trillion'],
            [0, 'quadrillion'],
            [0, 'quintillion'],
            [0, 'sextillion'],
            [0, 'septillion'],
            [0, 'octillion'],
            [0, 'nonillion'],
            [0, 'decillion'],
            [0, 'undecillon'],
            [0, 'duodecillion'],
            [0, 'tredecillion'] # we bigger than 64 bits now
        ])
        self.high_index = 0

    def __repr__(self):
        if self.high_index == 0:
            return '{}'.format(self.number[0][0])
        elif self.high_index == 1:
            return '{h}.{l}k'.format(h=self.number[self.high_index][0], l=str(self.number[self.high_index-1][0])[:-1])
        return '{h}.{l} {n}'.format(h=self.number[self.high_index][0], l=str(self.number[self.high_index-1][0]), n=self.number[self.high_index][1])

    def add(self, val):
        parsed_vals = val.split(',')
        for x in xrange(0, len(parsed_vals)):
            self.add_part(x, int(parsed_vals[len(parsed_vals) - (x+1)])) 
        self.check_highest()

    def add_part(self, index, val):
        new_val = val + self.number[index][0]
        if new_val < 1000:
            self.number[index][0] = new_val
            return 0 
        if index >= 14:
            for x in xrange(0, len(self.number)):
                self.number[x][0] = 999
            print 'your bumber is maxed, chief'
            return 0 
        self.number[index+1][0] += 1
        self.number[index][0] = new_val - 1000
        return 0

    def check_highest(self):
        self.high_index = 0
        for x in xrange(0, len(self.number)):
            if self.number[len(self.number) - x][0] > 0:
                self.high_index = len(self.number) - x
                return
        return

if __name__ == '__main__':
