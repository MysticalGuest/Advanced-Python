w = ord('a')
print('w', w)
print("bin(w)", bin(w))
bit = w & 0b0000001
print("bit", bin(bit))

w = w >> 1
print('w', w)
bit = w & 0b0000001
print("bit", bin(bit))

w = w >> 1
print('w', w)
bit = w & 0b0000001
print("bit", bin(bit))

w = w >> 1
print('w', w)
bit = w & 0b0000001
print("bit", bin(bit))

w = w >> 1
print('w', w)
bit = w & 0b0000001
print("bit", bin(bit))

w = w >> 1
print('w', w)
bit = w & 0b0000001
print("bit", bin(bit))

w = w >> 1
print('w', w)
bit = w & 0b0000001
print("bit", bin(bit))

pixel = 0b00001011
bit = 0b00000001
pixel = pixel & 0b11111110
print("bin(pixel)", bin(pixel))

a = 0b00111100
b = 0b00111101
print("bin(a or b)", bin(a or b), len(bin(a or b)))
print("bin(a & b)", bin(a & b), len(bin(a & b)))
print("bin(a and b)", bin(a and b), len(bin(a and b)))
print("bin(a | b)", bin(a | b), len(bin(a | b)))
print("bin(a ^ b)", bin(a ^ b), len(bin(a ^ b)))

