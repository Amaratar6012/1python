print("methods part tow")

print("__split__")
#__split__ تقوم بتقسيم النص الي list
a1 = "i love python and my brother"
print(a1.split())
a1 = "i-love-python-and-my-brother"
print(a1.split("-"))#انت تقوم بتحديد الرمز الذي يفصل الكلمات 
a1 = "i love python and my brother"
print(a1.split(" ", 2))#maxsplit وهي التي تحدد عدد الكلمات التي تريد فرزها والباقي والباقي لا
#rsplit نقس العمل لكن تبدا من لاخر
print(a1.rsplit(" ", 2))

print("__center__")
#center  تقوم بتحديد عدد لاحرف في النص لاتفهم الي بمثال
#مع تحديد عدد لاحرف
a2 = "amar"
print(a2.center(8, "#"))

print("__count__")
#count تقوم بعد الكلمات
a3 = "i love python and php and php"
print(a3.count("php", 0, 35))

print("__swapcase__")
#__swapcase__ تقوم بتكبير الحروف الصغيرة والعكس
a4 = "AmAR aTaR"
print(a4.swapcase())

print("__startswith___endswith__")
#__startwith___endwith__ يعملون علي مبدا الbooleanيعطونك قيمة ب true false
#هل تبدا او تنتهي ب ()والناتج يكون  true false
a5 = "hi my frinde"
print(a5.startswith("h"))
print(a5.endswith("t"))