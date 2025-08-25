#3. Convert distant given in feet and inches into meter and centimeter.


ft = int(input("Enter feet: "))
inch = float(input("Enter inches: "))

ft = (inch // 12)
inch = inch % 12

total_inches = ft * 12 + inch
cm = total_inches * 2.54
m = cm / 100

print(f"meters{m}")
print(f'centimeters',cm)