from PIL import Image, ImageDraw
import random
import math

#background and canvas setup
image_size_px = 1080
image_bg_color = (255, 255, 255)
image = Image.new("RGB", (image_size_px, image_size_px), (image_bg_color))

#input for amount of images
amount = int(input("How Many Images: "))

draw = ImageDraw.Draw(image)

#center point
x = int(540)
y = int(540)

#loop for every image
for i in range(amount):

    #size range settings
    radius = (random.randint(40, 100))
    width_range = (random.randint(10,25))
    length_range = (random.randint(200,600))

    #color range settings
    r = random.randint(0, 205)
    g = random.randint(0, 205)
    b = random.randint(0, 205)


    #loop for every line
    for _ in range(random.randint(100, 200)):
        #picks a colour in the range
        red = (random.randint(int(r), int(r) + 50))
        green = (random.randint(int(g), int(g) + 50))     
        blue = (random.randint(int(b), int(b) + 50))        
        color = (red, green, blue)
        #determines angle of line
        angle = math.degrees(random.randint(0, 360))
        #detemines size in range
        length = (random.randint(int(length_range), int(length_range) + 50))
        width = (random.randint(int(width_range), int(width_range) + 5))
        #math for drawing the line
        x2 = int(radius * (math.cos(angle)))
        y2 = int(radius * (math.sin(angle)))
        x3 = int(x + x2)
        y3 = int(y + y2)
        x4 = int(length * (math.cos(angle)))
        y4 = int(length * (math.sin(angle)))
        x5 = int(x + x4)
        y5 = int(y + y4)
        line = ((x3, y3), (x5, y5))
        #draws the line
        draw.line(line, color, width)
        

    #saves the image to computer
    image.save(f'#{i+1}.png', 'PNG')
    #clears the canvas
    draw.rectangle([0, 0, 1080, 1080], image_bg_color)
