import German as w2n
import AncientRus as AR
from unittest import TestCase


class TestConverter(TestCase):
    def test_hardcoded_values_upto_100(self):
        self.assertTrue(w2n.convert('eins') == 1)
        self.assertTrue(w2n.convert('zwei') == 2)
        self.assertTrue(w2n.convert('drei') == 3)
        self.assertTrue(w2n.convert('vier') == 4)
        self.assertTrue(w2n.convert('fünf') == 5)
        self.assertTrue(w2n.convert('sechs') == 6)
        self.assertTrue(w2n.convert('sieben') == 7)
        self.assertTrue(w2n.convert('acht') == 8)
        self.assertTrue(w2n.convert('neun') == 9)
        self.assertTrue(w2n.convert('zehn') == 10)
        self.assertTrue(w2n.convert('elf') == 11)
        self.assertTrue(w2n.convert('zwölf') == 12)
        self.assertTrue(w2n.convert('dreizehn') == 13)
        self.assertTrue(w2n.convert('vierzehn') == 14)
        self.assertTrue(w2n.convert('fünfzehn') == 15)
        self.assertTrue(w2n.convert('sechzehn') == 16)
        self.assertTrue(w2n.convert('siebzehn') == 17)
        self.assertTrue(w2n.convert('achtzehn') == 18)
        self.assertTrue(w2n.convert('neunzehn') == 19)
        self.assertTrue(w2n.convert('zwanzig') == 20)
        self.assertTrue(w2n.convert('einundzwanzig') == 21)
        self.assertTrue(w2n.convert('zweiundzwanzig') == 22)
        self.assertTrue(w2n.convert('dreiundzwanzig') == 23)
        self.assertTrue(w2n.convert('vierundzwanzig') == 24)
        self.assertTrue(w2n.convert('fünfundzwanzig') == 25)
        self.assertTrue(w2n.convert('sechsundzwanzig') == 26)
        self.assertTrue(w2n.convert('siebenundzwanzig') == 27)
        self.assertTrue(w2n.convert('achtundzwanzig') == 28)
        self.assertTrue(w2n.convert('neunundzwanzig') == 29)
        self.assertTrue(w2n.convert('dreißig') == 30)
        self.assertTrue(w2n.convert('einunddreißig') == 31)
        self.assertTrue(w2n.convert('zweiunddreißig') == 32)
        self.assertTrue(w2n.convert('dreiunddreißig') == 33)
        self.assertTrue(w2n.convert('vierunddreißig') == 34)
        self.assertTrue(w2n.convert('fünfunddreißig') == 35)
        self.assertTrue(w2n.convert('sechsunddreißig') == 36)
        self.assertTrue(w2n.convert('siebenunddreißig') == 37)
        self.assertTrue(w2n.convert('achtunddreißig') == 38)
        self.assertTrue(w2n.convert('neununddreißig') == 39)
        self.assertTrue(w2n.convert('vierzig') == 40)
        self.assertTrue(w2n.convert('einundvierzig') == 41)
        self.assertTrue(w2n.convert('zweiundvierzig') == 42)
        self.assertTrue(w2n.convert('dreiundvierzig') == 43)
        self.assertTrue(w2n.convert('vierundvierzig') == 44)
        self.assertTrue(w2n.convert('fünfundvierzig') == 45)
        self.assertTrue(w2n.convert('sechsundvierzig') == 46)
        self.assertTrue(w2n.convert('siebenundvierzig') == 47)
        self.assertTrue(w2n.convert('achtundvierzig') == 48)
        self.assertTrue(w2n.convert('neunundvierzig') == 49)
        self.assertTrue(w2n.convert('fünfzig') == 50)
        self.assertTrue(w2n.convert('einundfünfzig') == 51)
        self.assertTrue(w2n.convert('zweiundfünfzig') == 52)
        self.assertTrue(w2n.convert('dreiundfünfzig') == 53)
        self.assertTrue(w2n.convert('vierundfünfzig') == 54)
        self.assertTrue(w2n.convert('fünfundfünfzig') == 55)
        self.assertTrue(w2n.convert('sechsundfünfzig') == 56)
        self.assertTrue(w2n.convert('siebenundfünfzig') == 57)
        self.assertTrue(w2n.convert('achtundfünfzig') == 58)
        self.assertTrue(w2n.convert('neunundfünfzig') == 59)
        self.assertTrue(w2n.convert('sechzig') == 60)
        self.assertTrue(w2n.convert('einundsechzig') == 61)
        self.assertTrue(w2n.convert('zweiundsechzig') == 62)
        self.assertTrue(w2n.convert('dreiundsechzig') == 63)
        self.assertTrue(w2n.convert('vierundsechzig') == 64)
        self.assertTrue(w2n.convert('fünfundsechzig') == 65)
        self.assertTrue(w2n.convert('sechsundsechzig') == 66)
        self.assertTrue(w2n.convert('siebenundsechzig') == 67)
        self.assertTrue(w2n.convert('achtundsechzig') == 68)
        self.assertTrue(w2n.convert('neunundsechzig') == 69)
        self.assertTrue(w2n.convert('siebzig') == 70)
        self.assertTrue(w2n.convert('einundsiebzig') == 71)
        self.assertTrue(w2n.convert('zweiundsiebzig') == 72)
        self.assertTrue(w2n.convert('dreiundsiebzig') == 73)
        self.assertTrue(w2n.convert('vierundsiebzig') == 74)
        self.assertTrue(w2n.convert('fünfundsiebzig') == 75)
        self.assertTrue(w2n.convert('sechsundsiebzig') == 76)
        self.assertTrue(w2n.convert('siebenundsiebzig') == 77)
        self.assertTrue(w2n.convert('achtundsiebzig') == 78)
        self.assertTrue(w2n.convert('neunundsiebzig') == 79)
        self.assertTrue(w2n.convert('achtzig') == 80)
        self.assertTrue(w2n.convert('einundachtzig') == 81)
        self.assertTrue(w2n.convert('zweiundachtzig') == 82)
        self.assertTrue(w2n.convert('dreiundachtzig') == 83)
        self.assertTrue(w2n.convert('vierundachtzig') == 84)
        self.assertTrue(w2n.convert('fünfundachtzig') == 85)
        self.assertTrue(w2n.convert('sechsundachtzig') == 86)
        self.assertTrue(w2n.convert('siebenundachtzig') == 87)
        self.assertTrue(w2n.convert('achtundachtzig') == 88)
        self.assertTrue(w2n.convert('neunundachtzig') == 89)
        self.assertTrue(w2n.convert('neunzig') == 90)
        self.assertTrue(w2n.convert('einundneunzig') == 91)
        self.assertTrue(w2n.convert('zweiundneunzig') == 92)
        self.assertTrue(w2n.convert('dreiundneunzig') == 93)
        self.assertTrue(w2n.convert('vierundneunzig') == 94)
        self.assertTrue(w2n.convert('fünfundneunzig') == 95)
        self.assertTrue(w2n.convert('sechsundneunzig') == 96)
        self.assertTrue(w2n.convert('siebenundneunzig') == 97)
        self.assertTrue(w2n.convert('achtundneunzig') == 98)
print(AR.convert(999))
print(w2n.convert('zweihundertachtundfünfzig'))
T = TestConverter()
#T.test_hardcoded_values_upto_100()