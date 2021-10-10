name = 'Interlacer'


class Interlacer:

    def reverse_interlace(self):
        ans=""
        m1 = self.str1.split(" ")
        m2 = self.str2.split(" ")
        i = 0
        for i in range(min(len(m1),len(m2))):
            ans += m1[-(i + 1)] + " "
            ans += m2[-(i + 1)] + " "
        ans+= " ".join(m1[-i-2:-len(m1)-1:-1])
        ans+= " ".join(m2[-i-2:-len(m2)-1:-1])

        return ans


    def __init__(self, str1,str2):
        self.str1 = str1.strip()
        self.str2 = str2.strip()
        pass


def reverse_interlace(str1,str2):
    c = Interlacer(str1,str2)
    return c.reverse_interlace()