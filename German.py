import textdistance
import numpy as np
name = 'MyZahlwort'


class ZahlConverter:
    DIGITS = {
        'null': 0,
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

    def convert(self):
        number = self.trimmedText()
        Errors = ""
        H, T, D = 0, 0, 0

        if number.count("hundert") > 1:
            Errors += "Слово 'hundert' не может встречаться более одного раза  \n"
            Errors += "Возможная замена: " + number.split("hundert")[0] + "hundert" + number.split("hundert")[-1] + "  \n"
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
                    Errors += "Слово " + before_hundred + " не может идти перед hundert, возможно имелось ввиду '"+suggest+"',  \n возможные варианты:"
                    for digit in self.DIGITS.keys():
                        Errors += "'" + digit + "'; "
                    Errors += "  \n"
            number = number.split("hundert")[1]
        if number != "":
            if number.count("und") > 1:
                Errors += "Слово 'und' не может встречаться более одного раза  \n"
                Errors += "Возможная замена: " + number.split("und")[0] + "und" + number.split("und")[-1] + "  \n"
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
                    Errors += "Слово '" + b_und + "' не может идти перед 'und', возможно имелось ввиду '"+suggest+"',  \n возможные варианты:"
                    for digit in self.DIGITS.keys():
                        Errors += "'" + digit + "'; "
                    Errors += "  \n"

                if a_und in self.TENS:
                    T = self.TENS[a_und]
                else:
                    k = list(self.TENS.keys())
                    dists = [textdistance.levenshtein.distance(a_und, k[i]) for i in range(len(k))]
                    suggest = k[np.argmin(dists)]
                    Errors += "Слово '" + a_und + "' не может идти после 'und', возможно имелось ввиду '"+suggest+"',  \n возможные варианты:"
                    for digit in self.TENS.keys():
                        Errors += "'" + digit + "'; "
                    Errors += "  \n"
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
                    Errors += "Слово '" + number + "' не является числом, возможно имелось ввиду '"+suggest+"',  \n не пропущены ли 'hundert' или 'und'?  \n"
                    Errors += "Если они не нужны в числе, то обратитесь к данному словарю:  \n"
                    for digit in self.DIGITS.keys():
                        Errors += "'" + digit + "' = " + str(self.DIGITS[digit]) + ";  \n"
                    for digit in self.ENDING_TENS.keys():
                        Errors += "'" + digit + "' = " + str(self.ENDING_TENS[digit]) + ";  \n"
                    for digit in self.TENS.keys():
                        Errors += "'" + digit + "' = " + str(self.TENS[digit]) + ";  \n"

        if Errors != "":
            raise RuntimeError(Errors)

        return H * 100 + T + D

    def trimmedText(self):
        x = self.number.lower().strip().replace(" ", "")
        return x.lower().strip()

    def __init__(self, number):
        self.number = number


def convert(number):
    c = ZahlConverter(number)
    return c.convert()
