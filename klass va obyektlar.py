# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:43:51 2024

@author: Valijon
"""

class Kompyuter:
    def __init__(self, model, ram, hdd, gpu, cpu):
        self.model = model
        self.ram = ram
        self.hdd = hdd
        self.gpu = gpu
        self.cpu = cpu
        
    def info(self):
        inf = f"{self.model}, RAM:{self.ram}, SSD:{self.hdd}, CPU:{self.cpu}"
        return inf
        
macbook = Kompyuter("Apple Macbook", "8GB", "256MB", "NVIDIA", "Core i7")

