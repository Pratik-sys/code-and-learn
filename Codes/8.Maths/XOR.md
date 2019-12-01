# Subtraction of the two integrs without using arithmetic operators

- Sum of two bits can be obtianed by XOR(^) of two bits and carry can be obtianed by AND(&) and borow by same AND(&) and NOT(~)

- Basically we are using the half subtractor logic here to get the difference.

## Truth table of half subtractor:

| X | Y|  Diff |Borrow|
|---|---|------|------| 
| 0 | 0 |   0  |   0  |
| 0 | 1 |   1  |   1  |
| 1 | 0 |   1  |   0  |
| 1 | 1 |   0  |   0  |

