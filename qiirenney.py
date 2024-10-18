# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:28:19 2024

@author: Qirana
"""

# Fungsi untuk menentukan apakah tahun kabisat
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Fungsi untuk menentukan jumlah hari dalam suatu bulan
def days_in_month(month, year):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

# Loop utama program
while True:
    # Input bulan
    month = int(input("Enter the month (1-12): "))
    
    if month == -1:
        print("Program stopped.")
        break
    
    # Validasi input bulan
    if month < 1 or month > 12:
        print("Invalid month. Please enter a valid month.")
        continue
    
    # Input tahun
    year = int(input("Please enter the year (e.g., 2023): "))
    
    # Hitung jumlah hari dalam bulan
    days = days_in_month(month, year)
    
    # Tampilkan jumlah hari
    print(f"There are {days} days in the month")