name = 'MyRusConverter'


class RusConverter:

    ALPHABET = {
        'ф': 500,
        'р': 100,
        'л': 30,
        'и': 8,
        'в': 2,
        'а': 1
    }

    def convert(self):
        ans = ""
        x = self.number
        for digit in self.ALPHABET:

            num = (x//self.ALPHABET[digit])
            if num>19:
                ans+="ффффффффффффффф...ф["+str(num)+" символов]"
            else:
                ans+=digit*(x//self.ALPHABET[digit])
            x=x%self.ALPHABET[digit]
        return ans


    def __init__(self, number):
        self.number = number
        pass


def convert(number):
    c = RusConverter(number)
    return c.convert()
