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
        WORDS = self.number.split()

        lexems = ["START_0"]
        for word in WORDS:
            if word in self.ENDING_TENS: lexems.append("ETEN"+"_"+str(self.ENDING_TENS[word]))
            elif word in self.TENS: lexems.append("TEN"+"_"+str(self.TENS[word]))
            elif word in self.DIGITS: lexems.append("DIGIT"+"_"+str(self.DIGITS[word]))
            elif word == "hundert": lexems.append("HUNDERT_0")
            elif word == "und": lexems.append("UND_0")
            else: raise RuntimeError("встретилось неизвестное слово '"+word+"'")
        lexems.append("END_0")

        hundr = 0
        for i in range(len(lexems)-1):
            if lexems[i].split("_")[0]=="START":
                if lexems[i+1].split("_")[0] == "ETEN":pass
                elif lexems[i+1].split("_")[0] == "TEN":pass
                elif lexems[i+1].split("_")[0] == "DIGIT":pass
                elif lexems[i+1].split("_")[0] == "HUNDERT":hundr = 1
                elif lexems[i+1].split("_")[0] == "UND":raise RuntimeError("число не может начинаться словом und")
                elif lexems[i+1].split("_")[0] == "END":raise RuntimeError("Задано пустое число")
            if lexems[i].split("_")[0]=="ETEN":
                if lexems[i+1].split("_")[0] == "ETEN":raise RuntimeError("два числа 11-19 не могут идти подряд")
                elif lexems[i+1].split("_")[0] == "TEN":raise RuntimeError("разряд десяток не может идти после числа 11-19")
                elif lexems[i+1].split("_")[0] == "DIGIT":raise RuntimeError("разряд единиц не может идти после числа 11-19")
                elif lexems[i+1].split("_")[0] == "HUNDERT":raise RuntimeError("разряд сотен не может идти после числа 11-19")
                elif lexems[i+1].split("_")[0] == "UND":raise RuntimeError("слово 'und' не может идти после числа 11-19")
                elif lexems[i+1].split("_")[0] == "END":pass
            if lexems[i].split("_")[0]=="TEN":
                if lexems[i+1].split("_")[0] == "ETEN":raise RuntimeError("число 11-19 не может идти после разряда десятков")
                elif lexems[i+1].split("_")[0] == "TEN":raise RuntimeError("два разряда десятков не могут идти подряд")
                elif lexems[i+1].split("_")[0] == "DIGIT":raise RuntimeError("разряд единиц не может идти после разряда десятков")
                elif lexems[i+1].split("_")[0] == "HUNDERT":raise RuntimeError("разряд сотен не может идти после разряда десятков")
                elif lexems[i+1].split("_")[0] == "UND":raise RuntimeError("слово 'und' не может идти после разряда десятков")
                elif lexems[i+1].split("_")[0] == "END":pass
            if lexems[i].split("_")[0]=="DIGIT":
                if lexems[i+1].split("_")[0] == "ETEN":raise RuntimeError("число 11-19 не может идти после разряда единиц")
                elif lexems[i+1].split("_")[0] == "TEN":raise RuntimeError("разряд десятков не может сразу идти после разряда единиц")
                elif lexems[i+1].split("_")[0] == "DIGIT":raise RuntimeError("два разряда единиц не могут идти подряд")
                elif lexems[i+1].split("_")[0] == "HUNDERT" and hundr == 0:hundr = 1
                elif lexems[i+1].split("_")[0] == "HUNDERT" and hundr == 1:RuntimeError("разряд сотен не может идти после разряда единиц")
                elif lexems[i+1].split("_")[0] == "UND":pass
                elif lexems[i+1].split("_")[0] == "END":pass
            if lexems[i].split("_")[0]=="HUNDERT":
                if lexems[i+1].split("_")[0] == "ETEN":pass
                elif lexems[i+1].split("_")[0] == "TEN":pass
                elif lexems[i+1].split("_")[0] == "DIGIT":pass
                elif lexems[i+1].split("_")[0] == "HUNDERT":raise RuntimeError("два разряд сотен не могут идти подряд")
                elif lexems[i+1].split("_")[0] == "UND":raise RuntimeError("слово 'und' не может идти после разряда сотен")
                elif lexems[i+1].split("_")[0] == "END":pass
            if lexems[i].split("_")[0]=="UND":
                if lexems[i+1].split("_")[0] == "ETEN":raise RuntimeError("число 11-19 не может идти после слова 'und'")
                elif lexems[i+1].split("_")[0] == "TEN":pass
                elif lexems[i+1].split("_")[0] == "DIGIT":raise RuntimeError("разряд единиц не может идти после слова 'und'")
                elif lexems[i+1].split("_")[0] == "HUNDERT":raise RuntimeError("разряд сотен не может идти после слова 'und'")
                elif lexems[i+1].split("_")[0] == "UND":raise RuntimeError("два слова 'und' не могут идти подряд")
                elif lexems[i+1].split("_")[0] == "END":raise RuntimeError("число не может заканчиваться словом 'und'")

        res=0
        for i in range(1,len(lexems)-1):
            if lexems[i].split("_")[0] == "HUNDERT":
                res=100
                if lexems[i-1].split("_")[0] == "DIGIT":
                    res*=int(lexems[i-1].split("_")[1])
            if lexems[i].split("_")[0] in ["ETEN", "TEN", "DIGIT"]:
                res +=int(lexems[i].split("_")[1])
        return res

    def trimmedText(self):
        x = self.number.lower().strip().replace(" ", "")
        return x.lower().strip()

    def __init__(self, number):
        self.number = number


def convert(number):
    c = ZahlConverter(number)
    return c.convert()