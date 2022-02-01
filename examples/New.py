




    # ------------------- player 1 ---------------------

for hue in range(120):
    if player_one.pos() >= (300,100):
        rgb_fractional = colorsys.hsv_to_rgb(random.randint(hue - 10 , hue + 10) / 360.0 , s ,
                                             v)  # colorsys returns floats between 0 and 1
        r_float = rgb_fractional[0]  # extract said floating point numbers
        g_float = rgb_fractional[1]
        b_float = rgb_fractional[2]

        rgb = (r_float * 255 , g_float * 255 , b_float * 255)  # make new tuple with corrected values
        leds[hue] = rgb
        client.put_pixels(leds)  # send out

        sleep(0.03)  # 20ms

        P()
        L()
        A()
        L()
        E()
        R()
        ONE()
        W()
        I()
        N()
        S()



for hue in range(300 , 360):
    if player_one.pos() >= (300 , 100):
        rgb_fractional = colorsys.hsv_to_rgb(random.randint(hue - 10 , hue + 10) / 360.0 , s ,
                                             v)  # colorsys returns floats between 0 and 1
        r_float = rgb_fractional[0]  # extract said floating point numbers
        g_float = rgb_fractional[1]
        b_float = rgb_fractional[2]

        rgb = (r_float * 255 , g_float * 255 , b_float * 255)  # make new tuple with corrected values
        leds[hue] = rgb
        client.put_pixels(leds)  # send out

        sleep(0.03)  # 20ms

# ------------------- player 2 ---------------------

for hue in range(120):
    
        S()


for hue in range(300 , 360):
    if player_two.pos() >= (300 , -100):
        rgb_fractional = colorsys.hsv_to_rgb(random.randint(hue - 10 , hue + 10) / 360.0 , s ,
                                             v)  # colorsys returns floats between 0 and 1
        r_float = rgb_fractional[0]  # extract said floating point numbers
        g_float = rgb_fractional[1]
        b_float = rgb_fractional[2]

        rgb = (r_float * 255 , g_float * 255 , b_float * 255)  # make new tuple with corrected values
        leds[hue] = rgb
        client.put_pixels(leds)  # send out

        sleep(0.01)  # 20ms
