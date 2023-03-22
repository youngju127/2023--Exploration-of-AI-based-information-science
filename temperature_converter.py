fahrenheit = float(input('화씨 입력 :'))
#(0°C × 9/5) + 32 = 32°F
celsius = (fahrenheit - 32.0) * ((5.0/9.0))
#print(f"화씨 {fahrenheit:.2f}도는 섭씨 {celsius:.2f}도 입니다")
print("화씨 {0:.2f}도는 섭씨 {1:.2f}도 입니다".format(fahrenheit, celsius))

