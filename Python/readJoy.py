#https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
import RPi.GPIO as GPIO
# Pins in BCM Mode
chan_dict = {"START":21,"SELECT":4,"TR":23,"TL":18,"UP":5,"DOWN":6,"LEFT":13,"RIGHT":19,"A":26,"B":12,"X":16,"Y":20}
chan_tuple = tuple(chan_dict.values())
try: 
    # Set BCM Mode 
    GPIO.setmode(GPIO.BCM)
    # enable pull up
    GPIO.setup(chan_tuple, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    #print out GPIO`s
    print("Joystick buttons")
    for button in chan_dict:
      print(button,"\t",chan_dict[button])
      
    print("Pressed Buttons")  
    for button in chan_dict:
      print(button,"\t",GPIO.input(int(chan_dict[button])))
  
except KeyboardInterrupt:  
    # exits when you press CTRL+C  
    print("program termination CTRL+C\n"), # print value of counter  
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print("Something Happened")  
  
finally:  
    GPIO.cleanup() # Reset GPIO 
