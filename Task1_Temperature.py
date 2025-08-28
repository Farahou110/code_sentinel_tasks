try:
    temperature = float(input(("please enter the temperature ")))

    print("A: Fahrenheit(F)")
    print("B: degrees Celcius(®C)")
    value = input(("select the units of the temperature "))

    if (value == "B"):
     answer=print(f"the temperature is {(temperature*9/5)+32} F")
    elif (value=="A"):
        answer=print(f"the temperature is {temperature}F")
    else:
        answer=print(f"please enter choices from the above ")

except ValueError:print("Input Error!!!!Please enter a numerical value")





