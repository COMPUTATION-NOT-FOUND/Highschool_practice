
x=[[0 for i in range (2)]for j in range (100)]
y=[[0,0]]*100
z=[[0,0] for k in range(100)]
w=[[0]*2]*100

print(x)
print(w)
print(y)
print(z)


#So, if you want to initialize a 2D list with 100 rows and 2 columns
#and you don't need to change the value of any element later on, you can use any of the above methods.
#But if you want to modify the value of any element later on,
#you should use x or z.
