# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import threading
import time

# Program 1
def program1():
    for i in range(5):
        print("Program 1: Çıktı", i+1)
        time.sleep(0.5)  # Programın çalışmasını durdur, diğer programa geçiş yapabilmesi için

# Program 2
def program2():
    for i in range(5):
        print("Program 2: Çıktı", i+1)
        time.sleep(0.5)  # Programın çalışmasını durdur, diğer programa geçiş yapabilmesi için

# Thread'ler oluşturuluyor
thread1 = threading.Thread(target=program1)
thread2 = threading.Thread(target=program2)

# Thread'ler başlatılıyor
thread1.start()
thread2.start()

# Her iki thread'in tamamlanmasını bekliyoruz
thread1.join()
thread2.join()

print("Programlar tamamlandı.")
