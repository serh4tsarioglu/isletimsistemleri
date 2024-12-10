# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import time
import threading
import multiprocessing
# Çoklu programlama (Threading) fonksiyonu
def coklu_programlama(thread_id):
    print(f"Thread {thread_id} started with Thread ID: {threading.get_ident()}")
    time.sleep(2)  # Simülasyon: işlem süresi
    print(f"Thread {thread_id} finished with Thread ID: {threading.get_ident()}")
# Çoklu işlemci (Multiprocessing) fonksiyonu
def coklu_islemci(process_id):
    print(f"Process {process_id} started with Process ID: {os.getpid()}")
    time.sleep(2)  # Simülasyon: işlem süresi
    print(f"Process {process_id} finished with Process ID: {os.getpid()}")
if __name__ == "__main__":
    print("Çoklu Programlama Başlatılıyor (Threading)...")
    # Çoklu programlama (Threading) ile 4 iş parçacığı başlat
    threads = []
    for i in range(4):
        t = threading.Thread(target=coklu_programlama, args=(i,))
        threads.append(t)
        t.start()
    # İş parçacıklarının bitmesini bekle
    for t in threads:
        t.join()
    print("\nÇoklu İşlemci Başlatılıyor (Multiprocessing)...")
    # Çoklu işlemci (Multiprocessing) ile 4 işlem başlat
    processes = []
    for i in range(4):
        p = multiprocessing.Process(target=coklu_islemci, args=(i,))
        processes.append(p)
        p.start()
    # İşlemlerin bitmesini bekle
    for p in processes:
        p.join()
    print("\nTüm işlemler tamamlandı.")


