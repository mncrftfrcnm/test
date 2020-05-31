
def move_bat(batMove, batSpeed, rightPressed, leftPressed, c, bat, canvasWidth):
    batMove = batSpeed*rightPressed - batSpeed*leftPressed
    (batLeft,batTop,batRight,batBottom) = c.coords(bat)
    if (batLeft > 0 or batMove > 0) and (batRight < canvasWidth or batMove < 0):
        c.move(bat,batMove,0)