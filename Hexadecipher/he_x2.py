# *Alli*

name =["ali","ayaz","ahmed"] # لدينا مصفوفة مخزن فيه الاسماء 
def string(x): # دالة من اجل تشفير الاسماء 
    result = [] # انشاء مصفوفة من اجل حفظ التغيرات فيها 
    for i in x: #  من اجل تجزئة الاسماء لتحويلها الا نظام الست عشر for حلقات 
        b = [ord(j) for j in i] #   ord متغير من اجل تجزئة الاسماء وتحويلها الى
        z = [hex(c) for c in b] #   وا يحولها الى النظام الست عشر  b متغير ياخذ قيمته من المتغير 
        result.append(z) # ادراج المحتويات الى المصفوفة 
    return result # ارجاع قيمة المصفوفة 

def chrekter(y): # دالة من اجل فك تشفير الاسماء 
    result1 = []  # نفس ترتيب الدالة الاولى 
    for i in string(y): 
        b = [''.join(chr(int(strin,16)) for strin in i)]
        result1.append(b)
    return result1

print(string(name)) # استدعاء الدالات مع ادخال المصفوفة 
print(chrekter(name))
