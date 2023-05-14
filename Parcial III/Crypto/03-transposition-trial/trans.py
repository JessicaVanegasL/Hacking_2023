MESSAGE="heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4"

FLAG=""
for i in range(0,len(MESSAGE),3):

	FLAG +=MESSAGE[i+2] + MESSAGE[i:i+2]

print(FLAG)
