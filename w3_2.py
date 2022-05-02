
def computepay(hour,pay):
    if hour>40:
        return float((pay * 40)+((hour-40)*pay*1.5))

    elif hour<=40:
        return float(pay * hour)
h=float(input("Working Hour:"))
p=float(input("Hourly Wage:"))
print(computepay(h,p))


