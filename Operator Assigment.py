#!/usr/bin/env python
# coding: utf-8

# In[1]:


num1 = 10
num2 = 3

jumlah = num1 + num2
kurang = num1 - num2
kali = num1 * num2
bagi = num1 / num2
bagi_bulat = num1 // num2
pangkat = num1 ** num2
modulus = num1 % num2

print(jumlah)
print(kurang)
print(kali)
print(bagi)
print(bagi_bulat)
print(pangkat)
print(modulus)


# In[7]:


x = 5 #assigment operator
x +=10 # x = x + 10 => 15
print(x)
x -=4 # x = x - 4 => 11
print(x)
x *=2 # x = x * 2 => 22
print(x)
x /= 3 # x = x / 3 => 7
print(x)
x //=2 #x = x //2 => 3.0
print(x)
x **=3 #x = x ** 3 => 27
print(x)
x %=2 #x = x % 2 => 1
print(x)


# In[10]:


bil1 = 8
bil2 = 7

is_equal = bil1 == bil2
is_not_equal = bil1 != bil2
is_greater_than = bil1 > bil2
is_less_than = bil1 < bil2
is_greater_equal = bil1 >= bil2
is_less_equal = bil1 <= bil2 

print(is_equal)
print(is_not_equal)
print(is_greater_than)
print(is_less_than)
print(is_greater_equal)
print(is_less_equal)


# In[11]:


var1 = 4
var2 = 10
opr_and = var1 < var2 and var1 <=4 #True
opr_or = var1 >= var2 or var1 % 2==1 #False
opr_not = not opr_or

print(opr_and)
print(opr_or)
print(opr_not)


# operator identitas

# In[13]:


fruits = ["Apple","Mangoes","Watermelon"]
my_favorite_fruits = fruits
your_fruits = ["Apple","Mangoes","Watermelon"]

print(fruits is my_favorite_fruits)
print(fruits is your_fruits)
print(fruits is not my_favorite_fruits)
print(fruits is not your_fruits)

a = 5
b = 5#phyton menggunakan metode hashing dalam memberikan nilai variabel

print(a is b)
print(a is not b)


# In[15]:


student_names = ["Andi","Beni","Chika"]
print("Beni" in student_names)
print("Andi" not in student_names)
print("Defi" in student_names)
print("Defi" not in student_names)


# In[17]:


nilai_and = 255 & 15
nilai_or = 255 | 15
nilai_xor = 255 ^ 15
#11111111
#00001111
#-------- xor
#11110000 => 16 + 32 + 64 + 128
print(nilai_and)
print(nilai_or)
print(nilai_xor)


# In[ ]:




