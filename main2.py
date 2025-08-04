help("keywords")
# الكلمات التي تم حجزها في الغة
y =10
x= "amar"
#يمكنك كتابة المتغير ثم = وهو يعرف نوع المتغير
#يمكنك كتابة اي اسم للمتغير عد1.رقم في بداية
#2.@ - في كل لاسم لايمكنك كتابتهم
#المتغير يشير الي المكان الموجود فيه البيانات لا يخزنها
a, b, c = 1, 2, "amar"
# كنك كتابة اكثر من متغيمته في نفس السطر وتعريفه
print(y)
print(x)
print(a)
print(b)
print(c)
# Escape Sequences Characters (\) تكتب كلها في علامات تنصيص
print("hello\bworld") #يحذف حرف خلفه
print("I \
LOVE") # \ لوحدها تنتقل لسطر اخر الموجود
print("AMAR\'AMAR\'") # \ تلغي تاثير  #"", '', \
print('AMAR\"AMAR\"')
print("AMAR\\")
print("amar\natar") #تنزل سطر
print("amar\tatar") #تعمل مسافة ال tab
print("111117\ramar") #تعيد الكلمة التي بعدها الي بداية السطر وتحذف نفس عدد لاحرف
print("\x61") #تستخمدم لطباعة الحروف ولارقام والعلامات برموز معينة hex value
# Concatenation (+) دمج نصان
print("amar" + "atar")
print("amar" + "\n" + "atar")
print("amar" + " " + "atar")
print("amar " + " atar")
#print("hello + 1") error لايمكن جمع نص مع رقم
n = "amar"
m = "atar"
j = n+m
print(j)
print('amar"amar"amar')#تلغي علامة التنصيص عكسها ولا لاتلغي نفسها
print("atar'atar'atar")
tt ="""1 
2"test" 'test' 
3""" # الترابيل تحدد كل مابنها وتلغي تاثير اي علامة ماعدا \ازا وضعت اخر السطر وبعد شي مباشر
print(tt)