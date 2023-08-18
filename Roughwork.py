models = {('lite', 32, 2), ('pro', 64, 3), ('max', 128, 4),('lite', 128, 4)}
if list(filter(lambda z: z[0] == 'x',models)):
    print("True")

else:
    print("False")