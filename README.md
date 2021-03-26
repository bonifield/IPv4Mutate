# IPv4Mutate
performs various mutations on IPv4 addresses, such as converting to hex, octal, urlencoded, and more

### Usage
```
from ipv4mutate import IPv4Mutate
i = IPv4Mutate("127.0.5.7)
```

### Available Attributes
```
mutate_binary
mutate_hex
mutate_hex_combined
mutate_octal
mutate_octal_padded
mutate_zero_padded
mutate_zero_stripped
mutate_urlencoded
```

### Example Output (via test-ipv4mutate-usage-example.py)
```
IP: 127.0.5.7
        mutate_binary            01111111.00000000.00000101.00000111
        mutate_hex               0x7f.0x0.0x5.0x7
        mutate_hex_combined      0x7f000507
        mutate_octal             0177.00.05.07
        mutate_octal_padded      00000177.00000000000000.005.0007
        mutate_zero_padded       127.000.005.007
        mutate_zero_stripped     127.5.7
        mutate_urlencoded        %31%32%37%2e%30%2e%35%2e%37
```
