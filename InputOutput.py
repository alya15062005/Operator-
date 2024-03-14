#!/usr/bin/env python
# coding: utf-8

# Nilai statis dan dinamis 

# In[1]:


bil1 = input('isikan bilangan 1:')
bil2 = input('isikan bilangan 2:')
hasil = int(bil1) + int(bil2)
print("Hasil ", bil1, "+", bil2,"=",hasil)


# buatlah luas dan keliling persegi panjang

# In[2]:


panjang = input ("Masukan nilai panjang :")
lebar = input ("Masukan nilai lebar :")

luas = int(panjang) *int(lebar)
keliling = 2 *(int(panjang)) * int(lebar)

print("luas", luas)
print("keliling", keliling)


# In[3]:


print("A","B","C","D", sep='@_@') #sep=seperator atau pembatas


# In[4]:


print("A","B","C","D", sep='\n', end="^_^") 


# format index

# In[7]:


num_1 = 8
num_2 = 10

# Hasil dari 8 modulus 10 = 8
#str.format()

print('hasil dari {} modulus {} = {}'.format(num_1,num_2,num_1%num_2))


# In[10]:


fname = "Alya"
mname = "Rojwa"
Iname = "Fauziah"

print('Nama anda {0} {1} {2}'.format(fname,mname,Iname))


# In[11]:


print('Nama anda {nama}, nilai anda{nilai}'.format(nama='alya',nilai=85))


# In[13]:


univ = "Universitas Nusa Putra"

print("karakter pertama : ",univ[0])
print("karakter terakhir :",univ[-1])
#Universitas
print(univ[0:11])
print(univ[-5:])
print(univ[17:])
print(univ[::-1])


# f string

# In[15]:


f_name = 'Alya'
l_name = 'Yaya'

print(f'Nama saya {f_name}{l_name}')

first = 100
second = 20

print(f'Hasil penjumlahan {first} + {second} = {first+second}')


# split pada string

# In[20]:


nama = "Bela,Rahma,Rara"
nama2 = "Bela,Rahma,Rara"
#split -> memisahkan string berdasarkan karakter tertentu
print(nama2.split())
print(nama.split(','))

#join ->menggabungkan string kedalam kumpulan karakter
print('@'.join(nama.split(',')))

#input tgl lahir->15/juni/2005
#input nama -> Alya rf
#ouput :
#Tgl : 14, Bulan:Maret, Tahun:2024
#nama inisial : AL

tgl = input ("Masukan tanggal lahir :")
nama = input ("Masukan nama :")
pemisah = tgl.split("/")
print("Output :")
print(f"Tgl : {pemisah[0]}, Bulan :{1}, Tahun :{pemisah[2]}")
pemisah = nama.split()
nama_pertama = pemisah[0]
nama_terakhir = pemisah[1]
print(f"Nama inisial : {nama_pertama[0]+nama_terakhir[0]}")


# In[ ]:




