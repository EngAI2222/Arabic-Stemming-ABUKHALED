import os
from stemmers.khoja_stemmer import KhojaStemmerABUKHALED

def run_project():
    stemmer = KhojaStemmerABUKHALED()
    
    # التأكد من وجود المجلدات
    if not os.path.exists('outputs'): os.makedirs('outputs')
    if not os.path.exists('data'): os.makedirs('data')

    # عينة بيانات كبيرة (إذا لم يوجد ملف سيقوم بإنشائه)
    input_file = 'data/words.txt'
    if not os.path.exists(input_file):
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write("والعاملون\nبالمعلمات\nالجامعات\nيستخرجونها\nالمدرسة\nالانتصارات\nمكتبتنا")

    # معالجة الكلمات
    results = []
    with open(input_file, 'r', encoding='utf-8') as f:
        words = f.readlines()
        
    for word in words:
        word = word.strip()
        if word:
            root = stemmer.stem(word)
            results.append(f"Word: {word} -> Root: {root}")

    # حفظ النتائج في مجلد outputs
    output_path = 'outputs/results.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(results))

    print(f"✅ تم الانتهاء! تم حفظ {len(results)} نتيجة في {output_path}")

if __name__ == "__main__":
    run_project()