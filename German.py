import textdistance
import numpy as np
name = 'MyZahlwort'


class ZahlConverter:

    Errors=""

    DIGITS = {
        'ein': 1,
        'eins': 1,
        'eine': 1,
        'er': 1,
        'zwei': 2,
        'drei': 3,
        'drit': 3,
        'vier': 4,
        u'fünf': 5,
        'funf': 5,
        'sechs': 6,
        'sieben': 7,
        'sieb': 7,
        'acht': 8,
        'neun': 9
    }
    TENS = {
        'zehn': 10,
        'zwanzig': 20,
        u'dreißig': 30,
        'dreissig': 30,
        'vierzig': 40,
        u'fünfzig': 50,
        'funfzig': 50,
        'sechzig': 60,
        'siebzig': 70,
        'achtzig': 80,
        'neunzig': 90
    }

    ENDING_TENS = {
        'elf': 11,
        u'zwölf': 12,
        'zwolf': 12,
        'dreizehn': 13,
        'vierzehn': 14,
        'fünfzehn': 15,
        'sechzehn': 16,
        'siebzehn': 17,
        'achtzehn': 18,
        'neunzehn': 19
    }

    SCALES = {
        'dezilliarden': 10 ** 63,
        'dezilliarde': 10 ** 63,
        'dezillionen': 10 ** 60,
        'dezillion': 10 ** 60,
        'nonilliarden': 10 ** 57,
        'nonilliarde': 10 ** 57,
        'nonillionen': 10 ** 54,
        'nonillion': 10 ** 54,
        'oktilliarden': 10 ** 51,
        'oktilliarde': 10 ** 51,
        'oktillionen': 10 ** 48,
        'oktillion': 10 ** 48,
        'septilliarden': 10 ** 45,
        'septilliarde': 10 ** 45,
        'septillionen': 10 ** 42,
        'septillion': 10 ** 42,
        'sextilliarden': 10 ** 39,
        'sextilliarde': 10 ** 39,
        'sextillionen': 10 ** 36,
        'sextillion': 10 ** 36,
        'quintilliarden': 10 ** 33,
        'quintilliarde': 10 ** 33,
        'quintillionen': 10 ** 30,
        'quintillion': 10 ** 30,
        'quadrilliarden': 10 ** 27,
        'quadrilliarde': 10 ** 27,
        'quadrillionen': 10 ** 24,
        'quadrillion': 10 ** 24,
        'trilliarden': 10 ** 21,
        'trilliarde': 10 ** 21,
        'trillionen': 10 ** 18,
        'trillion': 10 ** 18,
        'billiarden': 10 ** 15,
        'billiarde': 10 ** 15,
        'billionen': 10 ** 12,
        'billion': 10 ** 12,
        'milliarden': 1000000000,
        'milliarde': 1000000000,
        'millionen': 1000000,
        'million': 1000000,
        'tausend': 1000,
    }

    def convert(self):
        self.number = self.trimmedText()
        if self.number == "null":
            return 0
        res=0
        for scale in self.SCALES:
            if self.number.count(scale) > 1:
                self.Errors += "[Scale_error]  \n"
                self.Errors += "Слово '"+scale+"' не может встречаться более одного раза  \n"
                self.Errors += "Возможная замена: " + number.split(scale)[0] + scale + number.split(scale)[
                    -1] + "  \n"
                self.number = self.number.split(scale)[-1]
            if self.number.count(scale) == 1:
                triple_str = self.number.split(scale)[0]
                res+=self.SCALES[scale]*self.get_triple(triple_str,scale)
                self.number=self.number.split(scale)[1]

        if self.number !="":
            res += 1 * self.get_triple(self.number, "einen")

        if self.Errors != "":
            raise RuntimeError(self.Errors)

        return res

    def get_triple(self,triple_str,cur_scale):
        number = triple_str
        H, T, D = 0, 0, 0

        if number=="":
            return 1

        if number.count("hundert") > 1:
            self.Errors += "[" + cur_scale + "]  \n"
            self.Errors += "Слово 'hundert' не может встречаться более одного раза внутри весового разряда "+cur_scale+"  \n"
            self.Errors += "Возможная замена: " + number.split("hundert")[0] + "hundert" + number.split("hundert")[-1] + "  \n"
            number = number.split("hundert")[-1]
        if number.count("hundert") == 1:
            before_hundred = number.split("hundert")[0]
            if before_hundred == "":
                H = 1
            else:
                if before_hundred in self.DIGITS:
                    H = self.DIGITS[before_hundred]
                else:
                    k = list(self.DIGITS.keys())
                    dists = [textdistance.levenshtein.distance(before_hundred,k[i]) for i in range(len(k))]
                    suggest = k[np.argmin(dists)]
                    self.Errors += "["+cur_scale+"]  \n"
                    self.Errors += "Слово " + before_hundred + " не может идти перед hundert, возможно имелось ввиду '"+suggest+"',  \n возможные варианты:"
                    for digit in self.DIGITS.keys():
                        self.Errors += "'" + digit + "'; "
                    self.Errors += "  \n"
            number = number.split("hundert")[1]
        if number != "":
            if number.count("und") > 1:
                self.Errors += "[" + cur_scale + "]  \n"
                self.Errors += "Слово 'und' не может встречаться более одного раза внутри весового разряда "+cur_scale+"  \n"
                self.Errors += "Возможная замена: " + number.split("und")[0] + "und" + number.split("und")[-1] + "  \n"
                number = number.split("und")[-1]

            if number.count("und") == 1:
                b_und = number.split("und")[0]
                a_und = number.split("und")[1]
                if b_und in self.DIGITS:
                    D = self.DIGITS[b_und]
                else:
                    k = list(self.DIGITS.keys())
                    dists = [textdistance.levenshtein.distance(b_und, k[i]) for i in range(len(k))]
                    suggest = k[np.argmin(dists)]
                    self.Errors += "[" + cur_scale + "]  \n"
                    self.Errors += "Слово '" + b_und + "' не может идти перед 'und', возможно имелось ввиду '"+suggest+"',  \n возможные варианты:"
                    for digit in self.DIGITS.keys():
                        self.Errors += "'" + digit + "'; "
                    self.Errors += "  \n"

                if a_und in self.TENS:
                    T = self.TENS[a_und]
                else:
                    k = list(self.TENS.keys())
                    dists = [textdistance.levenshtein.distance(a_und, k[i]) for i in range(len(k))]
                    suggest = k[np.argmin(dists)]
                    self.Errors += "[" + cur_scale + "]  \n"
                    self.Errors += "Слово '" + a_und + "' не может идти после 'und', возможно имелось ввиду '"+suggest+"',  \n возможные варианты:"
                    for digit in self.TENS.keys():
                        self.Errors += "'" + digit + "'; "
                    self.Errors += "  \n"
            else:
                if number in self.ENDING_TENS:
                    T = self.ENDING_TENS[number]
                elif number in self.TENS:
                    T = self.TENS[number]
                elif number in self.DIGITS:
                    D = self.DIGITS[number]
                else:
                    k = list(self.TENS.keys())+list(self.ENDING_TENS.keys())+list(self.DIGITS.keys())+['hundert','und']
                    dists = [textdistance.levenshtein.distance(number, k[i]) for i in range(len(k))]
                    suggest = k[np.argmin(dists)]
                    self.Errors += "[" + cur_scale + "]  \n"
                    self.Errors += "Слово '" + number + "' не является числом, возможно имелось ввиду '"+suggest+"',  \n не пропущены ли 'hundert' или 'und' или весовой разряд?  \n"
                    self.Errors += "За дополнительной информацией то обратитесь к данному словарю:  \n"
                    for digit in self.DIGITS.keys():
                        self.Errors += "'" + digit + "' = " + str(self.DIGITS[digit]) + ";  \n"
                    for digit in self.ENDING_TENS.keys():
                        self.Errors += "'" + digit + "' = " + str(self.ENDING_TENS[digit]) + ";  \n"
                    for digit in self.TENS.keys():
                        self.Errors += "'" + digit + "' = " + str(self.TENS[digit]) + ";  \n"
                    for digit in list(self.SCALES.keys().__reversed__())[:9]:
                        self.Errors += "'" + digit + "' = " + str(self.SCALES[digit]) + ";  \n"
                    self.Errors += "...  \n"
                    self.Errors += "'dezilliarden' = 10^63;  \n"



        return H * 100 + T + D

    def trimmedText(self):
        x = self.number.lower().strip().replace(" ", "")
        return x.lower().strip()

    def __init__(self, number):
        self.number = number


def convert(number):
    c = ZahlConverter(number)
    return c.convert()
