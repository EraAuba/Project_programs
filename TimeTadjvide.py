time_isha_hour = float(input("Time isha in hour: "))
time_isha_minut = float(input("Time isha in minut: "))/60
time_isha = time_isha_hour + time_isha_minut

time_fajr_hour = float(input("Time fajr in hour: "))
time_fajr_minut = float(input("Time fajr in minut: "))/60
time_fajr = time_fajr_hour + time_fajr_minut

def findTimeForSleep(a, b):
    midtime = (a-b)/2
    thirdtime = (a-b)/3

    sleep_till_tahaddjyd = a+midtime
    hour_tahaddjyd = int(sleep_till_tahaddjyd-24)
    minut_tahaddjyd = int(((sleep_till_tahaddjyd-24)-hour_tahaddjyd)*60)
    print("Время для ташаххуда: ", hour_tahaddjyd, " ", minut_tahaddjyd)

    pray_time = sleep_till_tahaddjyd + thirdtime
    hour_pray = int(pray_time-24)
    minut_pray = int(((pray_time-24)-hour_pray)*60)
    print("Время для молитвы до: ", hour_pray, " ", minut_pray)

    hour_b = int(b)
    minut_b = int((b-hour_b)*60)
    print("Просыпаться: ", hour_b, " ", minut_b)

findTimeForSleep(time_isha, time_fajr)