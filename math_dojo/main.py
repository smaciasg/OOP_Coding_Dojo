from prueba import MatematicasDojo

matem = MatematicasDojo()
x = matem.add(2).add(2,5,3).sustrac(2).sustrac(2,5,3).resultado
y = matem.add(2,1,1,8).sustrac(10,59,87,8).add(89,45,789).resultado
z= matem.add(x,y,y).sustrac(x,x,x).resultado
print(x)
print(y)
print(z)