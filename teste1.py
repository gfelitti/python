import simpleguitk as simplegui
def tick():
    print "tick!"

# Register handler
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()
