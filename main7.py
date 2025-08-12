print("__string formatting__")#طريقة قدبمة

#لايمكن شرحها الي بمثال لكن باختصار تقوم بتعليم مكان فاضي في السترنغ وتضع مكانه متغير او اي شي + انت تحدد نوع البيانات
#ياخذ بلترتيب و لا يكرر اخذ نفس الشي مرتين
#1_%s => string
print("___%s___")
a1 = 'amar'
print("my name is : %s" % a1) 
#تحديد عدد الحروف المراد طباعتاها
print("my name is : %.2s" % a1) 

#2_%d => number
print("___%d___")
a2 = 17
print("my age is : %d" % a2)
 
#3_%f => float
a3 = 10
print("i have A : %f" % a3) 
#تحديد عدد الحروف المراد طباعتاها
print("i have A : %.3f" % a3) 






print("__string formatting__")#طريقة جديدة
#1_{:s} => string
#نفس الفكرة مع تغيرات بسيطة واشياء جديدة 
#هذه لست مطر لتحديد نوع البيانات هو ياخذ بترتيب
print("___{:S}___")
a1 = 'amar'
print("my name is : {:s}".format(a1)) 
#تحديد عدد الحروف المراد طباعتاها
print("my name is : {:.2s}".format(a1)) 

#2_{d} => number
print("___{:d}___")
a2 = 17
print("my age is : {:d}".format(a2))
 
#3_{:f} => float
print("___{:f}___")
a3 = 10
print("i have A : {:f}".format (a3)) 
#تحديد عدد الحروف المراد طباعتاها
print("i have A : {:.3f}".format(a3)) 


print("__new__")
#1وضع علامة معينة كل 3 ارقام
money = 1000000000
print("my money is : {:,d}".format(money))
print("my money is : {:d}".format(money))
print("my money is : {:_d}".format(money))

#2تحدد ترتيب الطباعة
a, b, c = ("one", "two", "three")
print("hello {0} {1} {2}".format(a, b, c))
print("hello {2} {0} {1}".format(a, b, c))
print("hello {2} {1} {0}".format(a, b, c))
#a=0 b=1 c=2

#طريقة ال 3  السهلة
myname = "amar"
age = 77
print(f"amar is {myname} age is {age}")
#f" {} {} ""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
name1 = "amar"
shift = 6

    