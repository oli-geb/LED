# LED blink app

from RPi import GPIO
from math import pi
from time import sleep
from _thread import start_new_thread

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.IN)

def LED_On (pace):
    GPIO.output(8, False)
    sleep(pace)
        
def LED_Off (pace):
    GPIO.output(8, True)
    sleep(pace)

def LED_Blink (pace):
    for i in range (10):
        LED_On(pace)
        LED_Off(pace)
        
def Key_In ():
    print("hello master, what shall I do?")
    i = 0
    pace = 0.5
    LED_Off(pace)
    while True:
        print("Eingabe", i, ":")
        i = i+1
        kommando = input()
        if kommando == 'on':
            LED_On(pace)
        elif kommando == 'off':
            LED_Off(pace)
        elif kommando == 'blink':
            LED_Blink(pace)
        elif kommando == 'fast':
            pace = 0.2
        elif kommando == 'normal':
            pace = 0.5
        elif kommando == 'slow':
            pace = 0.8
        elif kommando == "stop":
            break
        elif kommando == 'help':
            print("on - schaltet Lampe ein")
            print("off - schaltet Lampe aus")
            print("blink - läßt Lampe 10x blinken")
            print("fast - setzt Blink Timer auf 0.2s")
            print("normal - setzt Blink Timer auf 0.5s")
            print("slow - setzt Blink Timer auf 0.8s")
            print("stop - Abbruch und Ausschalten der LED")
            print("help - zeigt diese Hilfe")
        else:
            print ("Kommando nicht bekannt")
    LED_Off(pace)    

def Switch_In ():
    i = 0
    while True:
        if GPIO.input(10):
            LED_On(0.5)
            sleep(0.05)
            i = i+1
            while GPIO.input(10):
                sleep(0.01)
            LED_Off(0.5)
        if i == 5:
            break

start_new_thread(Key_In,())
start_new_thread(Switch_In,())    
