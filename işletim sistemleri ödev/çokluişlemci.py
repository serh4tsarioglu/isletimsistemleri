# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import time
import multiprocessing

# Her işlemde çalışacak fonksiyon
def process_task(process_id):
    print(f"Process {process_id} started with PID: {os.getpid()}")
    time.sleep(2)  # İşlem süresi (simülasyon)
    print(f"Process {process_id} finished with PID: {os.getpid()}")

if __name__ == "__main__":
    # 4 adet işlem başlatacağız
    processes = []

    # İşlemleri oluşturma ve başlatma
    for i in range(4):
        p = multiprocessing.Process(target=process_task, args=(i,))
        processes.append(p)
        p.start()

    # Tüm işlemlerin tamamlanmasını bekleme
    for p in processes:
        p.join()

    print("Tüm işlemler tamamlandı.")

