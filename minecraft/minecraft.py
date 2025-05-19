from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# O'yinchi va osmon
player = FirstPersonController()
Sky()

# Texture nomini alohida saqlaymiz, keyinchalik oson almashtirish uchun
block_texture = 'grass.png'

# Yer tuzish funksiyasi
def create_ground(size=20):
    boxes = []
    for x in range(size):
        for z in range(size):
            box = Button(
                color=color.white,
                model='cube',
                position=(x, 0, z),
                texture=block_texture,
                parent=scene,
                origin_y=0.5
            )
            boxes.append(box)
    return boxes

# Bloklar ro‘yxati
boxes = create_ground()

# Blok qo‘shish va olib tashlash
def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                new_block = Button(
                    color=color.white,
                    model='cube',
                    position=box.position + mouse.normal,
                    texture=block_texture,
                    parent=scene,
                    origin_y=0.5
                )
                boxes.append(new_block)
            elif key == 'right mouse down':
                boxes.remove(box)
                destroy(box)

app.run()