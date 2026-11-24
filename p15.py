'''Find LCM and GCM of a number'''

lcm = 0
gcd = 0
cnt = 1
temp = True

n1 = 12
n2 = 18

# GCD
for i in range(1, min(n1, n2) + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i

# LCM
while temp:
    if cnt % n1 == 0 and cnt % n2 == 0:
        lcm = cnt
        temp = False
    cnt += 1

print(f"GCD : {gcd} LCM : {lcm}")