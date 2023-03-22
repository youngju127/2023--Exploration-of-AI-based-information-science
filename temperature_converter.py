while true:
    menu = int(input("1) fahrenheit to celcius  2) celcius to fahrenheit  3) exit"))

    if menu == 1:
        fahrenheit = float(input('enter temperture in fehrenheit :'))
        # (0°C × 9/5) + 32 = 32°F
        celsius = (fahrenheit - 32.0) * ((5.0 / 9.0))
        # print(f"화씨 {fahrenheit:.2f}도는 섭씨 {celsius:.2f}도 입니다")
        print(f"{fehrenheit:.2f} degrees fahrenheit is {celcius:.2f} degrees celcius.")
    elif menu == 2:
        fahrenheit = float(input('enter temperture in celcius :'))
        fahrenheit = (celsius * (9.0 / 5.0)) + 32.0
        print(f"{celsius:.2f} degrees celcius is {fahrenheit:.2f} degrees fahrenheit.")
    elif menu == 3:
        break
    else:
        print("Please choose from the given menu.")

fahrenheit = float(input('화씨 입력 :'))
#(0°C × 9/5) + 32 = 32°F
celsius = (fahrenheit - 32.0) * ((5.0/9.0))
#print(f"화씨 {fahrenheit:.2f}도는 섭씨 {celsius:.2f}도 입니다")
print("화씨 {0:.2f}도는 섭씨 {1:.2f}도 입니다".format(fahrenheit, celsius))
