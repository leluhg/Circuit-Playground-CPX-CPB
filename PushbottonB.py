# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.direction = digitalio.Direction.INPUT
button_B.pull = digitalio.Pull.DOWN

def main():
    print("hi") 
    print(dir(board))
    print("---") 
    print(dir(led))
    print("---") 
    print(dir(button_B))
    print("---") 
        led.value = button_B.value
        print(button_B.value)
        time.sleep(0.2)

main() 
