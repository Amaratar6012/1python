print ("___list___")
list1 = ["ONE", "tow", "77", 8, 100.8, "amar"]
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[5])
print("________________")
print(list1[-1])
print(list1[-2])
print(list1[-3])
print(list1[-4])
print(list1[-5])
print("________________")
print(list1[1:3])
print(list1[:3])
print(list1[1:])
print(list1[1::2])
print("________________")
print(list1)
list1[3] = 7
list1[4] = False
list1[0:2] = ["a", "b"]
print(list1)

print("___METHODS___")
#append يضيف عنصر جديد
a1 = ["amar", "atar"]
a2 = ["atar", "king"]
a1.append("obada")
print(a1)
a1.append(a2)
print(a1)
print(a1[3])
print(a1[3][1])
#extendتضيف عناصر listوليس الست كعنصر
a = [1, 2, 3, 4]
print(a)
b = ["A", "B", "C"]
c = ["one", "tow"]
a.extend(b)
a.extend(c)
a.extend("ama") # كل حرف عنصر ههههه
print(a)
#remove حذف عنصر من list
a.remove("one")
print(a)
#sort ترتيب لارقام ولاحرف لكن ليس مع بعض
y = [23, 435, 4, 54, 6457, 746, -349]
y.sort()
print(y)
y.sort(reverse=False)#بتقله لا تعكسهم
print(y)
y.sort(reverse=True)#بتقله اعكسهم
print(y)
#reverse يعكس list فقط
z = ["afgdsa", 284, "FJWEF", True]
z.reverse()
print(z)