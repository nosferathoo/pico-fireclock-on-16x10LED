# Example using PIO to drive a set of WS2812 LEDs.
import array, time, math
import bootsel
import os
import random
from font3x10 import *
from NeoPixel import *
from time import gmtime
      
def rgb_to_int(*color):
    return (color[1]<<16) + (color[0]<<8) + color[2]

def rgb_to_int2(color):
    return (color[1]<<16) + (color[0]<<8) + color[2]

def int_to_rgb(c):
    r = int((c >> 8) & 0xFF)
    g = int((c >> 16) & 0xFF)
    b = int(c & 0xFF)
    return (r,g,b)
    
def mul_rgb(mul,rgb):
    (r,g,b)=rgb
    return (int(r*mul),int(g*mul),int(b*mul))

def add_char_to_clockmask(clock_mask,char):
    for i,row in enumerate(font_3x10[char]):
        clock_mask[i] += row

if __name__=='__main__':
    strip = NeoPixel()
    strip.brightness=1
    

    fireTempAr = array.array("I", [0] * (NUM_LEDS+16))
    
    lastLine = fireTempAr[:16]

    fireLookUpPalette = array.array("I", (rgb_to_int(0,i,0) if i<256 else rgb_to_int((i-256),255,0) if i<512 else rgb_to_int(255,255,(i-512)) if i<768 else rgb_to_int(255,255,255) for i in range(1024)))
    fireLookUpPalette2 = array.array("I", (rgb_to_int2(mul_rgb(0.2,int_to_rgb(c))) for c in fireLookUpPalette))
    paletteSize = len(fireLookUpPalette)

    MODE_SET_TIME = 0
    MODE_NORMAL = 4
    mode = MODE_SET_TIME
    
    settime_digit = 0
    settime_time = [0,0,0,0]
    
    digits_mod = [3,10,6,10]
    ignore_first_click = False
    
    offset_time = 0
    while True:
        current_time = time.gmtime(time.time()+offset_time)

        # Extract hours and minutes from the gmtime
        hours = current_time[3]
        minutes = current_time[4]
        seconds = current_time[5]

        formatted_time = ""
        if mode == MODE_SET_TIME:
            
            for i in range(4):
                formatted_time += str(settime_time[i]) if (i!=settime_digit or seconds%2==0) else "_"

            if bootsel.pressed() and not ignore_first_click:
                count = 0
                while bootsel.pressed():
                    time.sleep(0.1)
                    count += 1
                
                    if count > 10:
                        ignore_first_click = True
                        if ((settime_digit==0) and (settime_time[0]==2)):
                            digits_mod[1] = 4
                            
                        settime_digit += 1
                        if settime_digit > 3:
                            hours = settime_time[0]*10+settime_time[1] - hours
                            minutes = settime_time[2]*10+settime_time[3] - minutes
                            offset_time = hours * 3600 + minutes * 60 - seconds
                            mode = MODE_NORMAL
                        break

                if not ignore_first_click:
                    settime_time[settime_digit] = (settime_time[settime_digit] + 1) % digits_mod[settime_digit]
            

        else:
            # Format hours and minutes with leading zeros
            formatted_time = f"{hours:02}{minutes:02}"
            if bootsel.pressed() and not ignore_first_click:
                strip.brightness += 0.1
                if strip.brightness>1.0:
                    strip.brightness=0
                while bootsel.pressed():
                    time.sleep(0.1)
            
        if not bootsel.pressed() and ignore_first_click:
            ignore_first_click = False
        
        clock_mask = [""] * 10
        add_char_to_clockmask(clock_mask,(formatted_time[0]));
        add_char_to_clockmask(clock_mask," ");
        add_char_to_clockmask(clock_mask,(formatted_time[1]));
        
        for _ in range(2):
            add_char_to_clockmask(clock_mask,":" if seconds%2==0 else " ");

        add_char_to_clockmask(clock_mask,(formatted_time[2]));
        add_char_to_clockmask(clock_mask," ");
        add_char_to_clockmask(clock_mask,(formatted_time[3]));            
                
        
        for i in range(16):
            lastLine[i] = random.randrange(0,len(fireLookUpPalette))
        # scroll up add random fire at btooom
        fireTempAr = fireTempAr[16:] + lastLine
        
        fireTempAr2 = fireTempAr
        for i in range(16,NUM_LEDS):
            fireTempAr2[i] = (int)((fireTempAr[i-16] + fireTempAr[i-1] + fireTempAr[i+1] + fireTempAr[i+16] + fireTempAr[i]) / 5.25)
        fireTempAr = fireTempAr2
        
        for i in range(NUM_LEDS):
            mask = clock_mask[i//16][i%16]
            fVal = fireTempAr[i]
            strip.ar[i] = fireLookUpPalette2[fVal] if mask==" " else fireLookUpPalette[fVal]
        
        strip.pixels_show()

               
        time.sleep(0.01) # change this to bigger value to slowdown animation

