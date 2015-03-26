# first example of drawing on the canvas
import simplegui

# define draw handler
def draw(canvas):
    canvas.draw_text("Hello!", [150, 199], 12, "White")
    canvas.draw_circle([100, 100], 8, 12, "Red")

# create frame
frame = simplegui.create_frame("Test", 300, 200)

# register draw handler    
frame.set_draw_handler(draw)

# start frame
frame.start()