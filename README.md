# IPv4Mutate
performs various mutations on IPv4 addresses, such as converting to binary, hex, octal, urlencoded, and more

### Installation
```
pip install ipv4mutate
```

### Usage
```
from ipv4mutate import IPv4Mutate
i = IPv4Mutate("127.0.5.7")
print(i.mutate_hex)
```

### Available Attributes
```
mutate_binary
mutate_dotted_hex
mutate_hex
mutate_octal
mutate_octal_padded
mutate_zero_padded
mutate_zero_stripped
mutate_urlencoded
mutate_decimal
```

### Example Output (via `test-ipv4mutate-usage-example.py`)
```
IP: 127.0.5.7
        mutate_binary            01111111.00000000.00000101.00000111
        mutate_dotted_hex        0x7f.0x0.0x5.0x7
        mutate_hex               0x7f000507
        mutate_octal             0177.00.05.07
        mutate_octal_padded      0000000000000000000177.000000000000000000000.00000005.00000000007
        mutate_zero_padded       127.000.005.007
        mutate_zero_stripped     127.5.7
        mutate_urlencoded        %31%32%37%2e%30%2e%35%2e%37
        mutate_decimal           2130707719
```

### Integration with IPv4Helper [GitHub](https://github.com/bonifield/IPv4Helper) [PyPi](https://pypi.org/project/ipv4helper/)
```
from ipv4helper import IPv4Helper
from ipv4mutate import IPv4Mutate
i = IPv4Helper("127.144.4.9/28")
for x in i.ip_range_generator():
	z = IPv4Mutate(x)
	print(z.mutate_hex)

# snipped output
# ...
# 0x7f.0x90.0x4.0x0
# 0x7f.0x90.0x4.0x1
# 0x7f.0x90.0x4.0x2
# 0x7f.0x90.0x4.0x3
# ...
```
