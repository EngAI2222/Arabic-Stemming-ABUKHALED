from .normalization import Normalizer

class KhojaStemmerABUKHALED:
    def __init__(self):
        self.normalizer = Normalizer()
        self.prefixes = ["وال", "بال", "فال", "ال", "لل", "و", "ب", "ف"]
        self.suffixes = ["ون", "ات", "ين", "كما", "هم", "هن", "نا", "ت", "ه", "ها"]

    def stem(self, word):
        word = self.normalizer.normalize(word)
        if len(word) <= 3: return word # الكلمات الثلاثية لا تُجذر
        
        res = word
        # إزالة السوابق (تحسين: ترتيب الأطول أولاً)
        for p in sorted(self.prefixes, key=len, reverse=True):
            if res.startswith(p) and len(res) - len(p) >= 3:
                res = res[len(p):]
                break

        # إزالة اللواحق
        for s in sorted(self.suffixes, key=len, reverse=True):
            if res.endswith(s) and len(res) - len(s) >= 3:
                res = res[:-len(s)]
                break
                
        return res