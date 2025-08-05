#index يمكنك تحديد حرف معين من  string list tuple اي نص
#slicingيمكن تحديد  قطعة كاماة من النص
#يبدا العد من 0 مع عد المساحات الفارغة ويبدا العد من   العكس ب-1 []

print("____index____")
num = "I  love python"
print(num[3]) # l
print(num[-3]) # h

print("\n____slicing____")
print(num[3:7]) #[بداية:نهاية]لايتم تحديد الرقم لاخير بل الذي قبله
print(num[:7])#يطبع من بداية حتا نهاية موضوعة
print(num[3:])#من بداية موضوعة حتا نهاية سطر
print(num[:])#كل شيء
#هناك شيء يسما staps خطوات مثل
#num[0:13:1]1يقوم بطباعة واحد واحد
#num[0:13:3]يقوم بطباعة كل ثلاث حروف متتالية
print(num[0:13:1])
print(num[0:13:3]) 
#امر len يعد عدد لاحرف والمساحات
an = "amara atar king"
print(len(an))
#mathods اوامر تضاف مع string تقوم ببعض الوظاىف
print("__strip__") #تقوم بحذاف اشياء معينة من النص ان لم تحددها تقوم بازالة المساحات
a1 = "   I Love my brother   "
print(a1.strip()) #كل السطر
print(a1.rstrip())#r اليمين تحدد له الجهة
print(a1.lstrip())#l اليسار تحدد له الجهة
a1 = "##I Love my brother##"
print(a1.strip("#"))

print("__title__") ; print("capitalize")
a2 = "amar 16a obada 13a"
print(a2.title())#تقوم بتكبير اول حرف في الكلمة والحرف بعد الرقم\
print(a2.capitalize())#تقوم  بتكبير اول حرف

print("__zfill__")
ap, ap2, ap3="1", "11", "111"
print(ap.zfill(3))
print(ap2.zfill(3))
print(ap3.zfill(3))
#تقوم باضافة اصفار حتى يصبح لارقام متساوين وانت تكتب عدد لارقام حسب اكبر رقم كتبته
#1, 11, 111, --> 001 011 111

print("__upper___lower__")
nn = "aMar"
print(nn.upper())#تكبير كل الحروف
print(nn.lower())#تصغير كل الحروف