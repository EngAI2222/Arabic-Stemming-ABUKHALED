import re

class Normalizer:
    def __init__(self):
        self.arabic_diacritics = re.compile(r'[\u064B-\u0652]')
        
    def normalize(self, text):
        # إزالة التشكيل
        text = re.sub(self.arabic_diacritics, '', text)
        # توحيد الهمزات
        text = re.sub("[إأآ]", "ا", text)
        # توحيد الياء والتاء المربوطة
        text = re.sub("ى", "ي", text)
        text = re.sub("ة", "ه", text)
        # إزالة أي رموز غير عربية
        text = re.sub(r'[^\u0621-\u064A\s]', '', text)
        return text.strip()