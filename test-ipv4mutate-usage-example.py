#!/usr/bin/python3

from ipv4mutate import IPv4Mutate

print("="*100)

i = IPv4Mutate("127.0.5.7")

print("IP:", str(i))
print("\tmutate_binary\t\t", i.mutate_binary)
print("\tmutate_hex\t\t", i.mutate_hex)
print("\tmutate_hex_combined\t", i.mutate_hex_combined)
print("\tmutate_octal\t\t", i.mutate_octal)
print("\tmutate_octal_padded\t", i.mutate_octal_padded)
print("\tmutate_zero_padded\t", i.mutate_zero_padded)
print("\tmutate_zero_stripped\t", i.mutate_zero_stripped)
print("\tmutate_urlencoded\t", i.mutate_urlencoded)

print("="*100)
