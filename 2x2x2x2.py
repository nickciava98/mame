print("Multidimensional Arrays Management Engine")
print("Copyright \u00a9 2015 Niccolò Ciavarella\n")
print("Example: 4 dimensional array\n")

el = [] * 16

for c in range(16):
    el.append(input("Type element " + str(c + 1) + ": "))
    
a = [
        [
            [
                [el[0], el[1]], [el[2], el[3]]
            ],
            [
                [el[4], el[5]], [el[6], el[7]]
            ]
        ],
        [
            [
                [el[8], el[9]], [el[10], el[11]]
            ],
            [
                [el[12], el[13]], [el[14], el[15]]
            ]
        ]
    ]

print("")
print(a)
