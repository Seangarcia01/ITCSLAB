def process_temp(temp):
    print("Temperature readings: (", end="")
    for i, temperature in enumerate(temp):
        if i < len(temp) - 1:
            print(f"{temperature}", end=", ")
        else:
            print(f"{temperature}", end="")
    print(")")

temperatures = (15.2, 16.8, 18.4, 20.1, 21.5, 23.0, 19.8, 17.6)

process_temp(temperatures)
print(f"Maximum Temperature: {max(temperatures)}°C")
print(f"Minimum Temperature: {min(temperatures)}°C")