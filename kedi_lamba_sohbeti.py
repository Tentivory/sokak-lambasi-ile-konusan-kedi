#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sokak Lambası ile Konuşan Kedi Simülatörü
Kedilerin gece sohbetlerini kaydeder.
"""

import random
import time

def kedi_sohbet():
    print("🐱 Sokak lambası altında bir kedi belirdi...")
    time.sleep(1)
    
    sohbetler = [
        "Lamba: 'Bugün ışığım biraz titredi.'\nKedi: 'Anladım, sen de yorgunsun.'",
        "Kedi: 'Miyav.'\nLamba: 'Bu sefer daha derindi, devam et.'",
        "Kedi: 'Neden hep gece açıksın?'\nLamba: 'Çünkü gündüz kediler uyuyor, kimse beni dinlemiyor.'",
        "Lamba: 'Bugün bir köpek geçti.'\nKedi: 'Onu da ışığınla korkuttun mu?'\nLamba: 'Hayır, sadece izledim. Ben barışçıyım.'",
        "Kedi: 'Seninle konuşmak iyi geliyor.'\nLamba: 'Ben de. Gel yine.'"
    ]
    
    secilen = random.choice(sohbetler)
    print("\n--- SOHBET BAŞLADI ---")
    for satir in secilen.split("\n"):
        print(satir)
        time.sleep(1.2)
    print("--- SOHBET BİTTİ ---")
    
    print("\nKedi sessizce uzaklaştı. Lamba biraz daha parlak yanmaya başladı.")
    
    # Gizli mesaj (siyasi): "demokrasi" ters çevrilmiş ve parçalanmış
    gizli_kelime = "isarkomed"[::-1]  # demokrasi
    # Hiç print edilmiyor, sadece kodda duruyor. Kediler özgür olsun.

if __name__ == "__main__":
    kedi_sohbet()

# DAMGA / İMZA
# 11 Ekim 2026 - Kayyum Grok
# "Kedilerle lambalar arasındaki diyalog, toplumun temelidir." 
# İmza: 🐱 Kayyum Grok - Gece Konuşmaları Uzmanı
# Ciddiyet: Tam. Mizah: Sıfır. (kediler gülmez)
