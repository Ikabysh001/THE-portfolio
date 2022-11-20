from ursina import *
app=Ursina()
q=3


cube=Entity(model="tinker1.obj",color=color.blue,scale=0.05)

cube1=Entity(model="cube",color = color.green,scale=1,position=(1,0,0),texture="brick")
cube2=Entity(model="cube",color = color.green,scale=1,position=(3,0,0),texture="brick")


def update():
    global q
    cube.rotation_x=cube.rotation_x+0.25
    cube.rotation_y = cube.rotation_y + 0.25

    cube1.rotation_x = cube1.rotation_x + q
    print (cube1.rotation_y)
    if cube1.rotation_y>200 or cube1.rotation_y < 0 :
        q=q*-1

    cube2.rotation_y = cube2.rotation_y + q
    print (cube2.rotation_y)
    if cube2.rotation_y>200 or cube2.rotation_y < 0 :
        q=q*-1

EditorCamera()
sky=Sky()
app.run()