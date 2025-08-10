print("method part 3")

print("__rjust__ljust")
#نفس فكرة عمل center  لكن تحدد من اليمين او من اليسار 
a1 = "amar"
print(a1.rjust(8, " "))
print(a1.ljust(8, " "))

print("__index__find__")
a2 = "i love python"
#1_عنطريق كتابة رقم وهو يقلك ما الحرف
print(a2[4])
#2_عنطريق كتابة حرف وهو يقلك الرقم
print(a2.index("p"))
#print(a2.index("p", 0, 3)) error لا يوجد  

#3_find نفس الوظيفة لكن الفرق عند عدم وجد الحرف لا تظهر خطا بلتظهر -1
print(a2.find("p", 0, 3)) 

print("__splitlines__")
a3 = """amar ok
atar no
king yes""" 
#الفرق بينها وبين split انها تقوم بلتقسبم علي حسب السطر وليس  انت من تحدد
print(a3.splitlines())

print("__expandtabs__")
a4 = "amar\tatar\tking\t"
#تتحكم بعدد المساحات

#يمكنك سوال هل النص   بis ثم السوال تفهم بمثال
a6 = " "
print(a6.isspace())
#وهاكذا اي سوا يتعلق بلسترنج وهناك نو اسالة اخر مثل
#isidentifier تسال هل يصلح لاسم للمتغير
a7 = "amat-r"
print(a7.isidentifier())
#isalpha تستخدم لسوال اذا كان النص من احرف فقطa-z
a8 = "amar"
print(a8.isalpha())
#isalnum تستخدم لمعرفة اذا كان النص يحتوي علي a-z 0او-9
a9 = "amar13"
print(a9.isalnum())

print("__replace__")
#تقوم بتبديل الكلمات بكلماة اخرا تفهم بمثال
a10 = "one tow three one one"
print(a10.replace("one", "1"))
print(a10.replace("one", "1", 2))

print("__join__")
#نقوم بتحويل الLIST الي STRING
a11 = ["amar", "atar", "king"]
print(" ".join(a11))
print(type(" ".join(a11)))