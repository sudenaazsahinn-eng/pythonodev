import time 
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")
#Önce ağacı çizeceğim
def draw_tree(light):
    print("    ^")    
    print(f"   ^{light}^")
    print(f"  ^{light}^{light}^")
    print(f" ^{light}^{light}^{light}^")
    print("   ||")

#Asallığı kontrol ettireceğim
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False  
    return True
#Fibonacci kontrolünü yapalım
def is_fibonacci(n):
    a , b = 0, 1
    while b < n:
        a, b = b, a+b
    return  b == n or n == 0
#Sparkle desenini ekleyelim
def sparkle_pattern(kelime):
    sesli_harfler = "aeiouAEIOU"
    lights = ["o", "o", "o"]
    index = 0
    for karakter in kelime[:3]:
        clear()
        if karakter in sesli_harfler and index < len(lights):
            lights[index] = "*"
            index += 1
        print("    ^")
        print(f"   ^{lights[0]}^")
        print(f"  ^{lights[1]}^{lights[1]}^")
        print(f" ^{lights[2]}^{lights[2]}^{lights[2]}^")
        print("   ||")

        time.sleep(1.5)
#Pulse desenini ekleyelim
def pulse_pattern():
    for _ in range(2):
        clear()
        draw_tree("*")
        time.sleep(1.5)

        clear()
        draw_tree("o")
        time.sleep(1.5)
#Wawe desenini ekleyelim
def wave_pattern():
    satirlar = [
        "    ^",
        "   ^*^",
        "  ^*^*^",
        " ^*^*^*^",
        "   ||"
    ] 
    for i in range(len(satirlar)):
        clear()
        for j in range(len(satirlar)):
            if j == i:
                print(satirlar[j])
            else:
                print(satirlar[j].replace("*", "o"))
        time.sleep(1)
#Reverse Wave deseni 
def reverse_wave_pattern():
    satirlar = [
        "    ^",
        "   ^*^",
        "  ^*^*^",
        " ^*^*^*^",
        "   ||"
    ] 
    for i in range(len(satirlar)-1, -1, -1):
        clear()
        for j in range(len(satirlar)):
            if j == i:
                print(satirlar[j])
            else:
                print(satirlar[j].replace("*","o"))
        time.sleep(1)

def main():
    clear()
    draw_tree("o")
    time.sleep(0.7)

    magic_word = input("Sihirli kelimeyi giriniz: ")
    number = int(input("Dizi numarasını giriniz:"))

    if len(magic_word) % 2 == 0:  #Kelime uzunluğun çift mi diye bakacak
        if is_prime(number):
            sparkle_pattern(magic_word)
        else:
            pulse_pattern()
    else:
        if is_fibonacci(number):
            wave_pattern()
        else:
            reverse_wave_pattern()

    clear()
    draw_tree("*")
main()            


                