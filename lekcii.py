edno =input()
dve = input()

for i in range(len(edno)):
    if edno[i] != dve[i]:
        for dve_index in range(0,i+1):
            print(dve[dve_index], end="")
        for edno_index in range(i+1, len(edno)):
            print(edno[edno_index], end="")
        print()