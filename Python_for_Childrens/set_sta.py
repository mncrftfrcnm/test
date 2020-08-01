def set_state(objecte,mouse_x,mouse_y):
    while True:
        if mouse_x < objecte.rect.x:
            objecte.x -= 1
            objecte.rect.x = objecte.x
        if mouse_x > objecte.rect.x:
            objecte.x += 1
            objecte.rect.x = objecte.x
        if mouse_y < objecte.rect.y:
            objecte.y -= 1
            objecte.rect.y = objecte.y
        if mouse_y < objecte.rect.y:
            objecte.y -= 1
            objecte.rect.y = objecte.y
        if mouse_x == objecte.rect.x and mouse_y ==  objecte.rect.x:
            break
        