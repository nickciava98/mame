print("Multidimensional Arrays Management Engine")
print("Copyright \u00a9 2015 Niccolò Ciavarella. All rights reserved.\n")
print("Example: 3 dimensional array 2x2x2\n")

el = [] * 8

for c in range(8):
    el.append(input("Type element " + str(c + 1) + ": "))

a = [
        [
            [el[0], el[1]], [el[2], el[3]]
        ],
        [
            [el[4], el[5]], [el[6], el[7]]
        ]
     ]

print("")
print(a)
