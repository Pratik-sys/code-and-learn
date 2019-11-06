# Built-in Dictionary Methods

- The following is an overview of methods that can be applied to the dictioonary:

## d.clear
 > Clears all the Dictionary

 ```bash
 >>> d = {'alex':23,'martin':21,'andrew':22,'keanu':25}
 >>> d.clear 
 >>> print(d)
{}
 ```

 ## d.get()
 > Returns the value for a key if exists in Dictionary

 ```bash
 >>> d = {'alex':23,'martin':21,'andrew':22,'keanu':25}
 >>> print(d.get('martin'))
21
```

## d.items()
> Returns the list of key value pairs from the Dictionary

```bash
>>> d = {'alex':23,'martin':21,'andrew':22,'keanu':25}
>>> list(d.items())
[('alex', 23), ('martin', 21), ('andrew', 22), ('keanu', 25)]
```

## d.keys()
> Returns the list of jey from the Dictionary 

```bash 
>>> d = {'alex':23,'martin':21,'andrew':22,'keanu':25}
>>> list(d.keys())
['alex','martin','andrew','keanu']
```

## d.values()
> Returns the values in the dicitonary

```bash 
>>> d = {'alex':23,'martin':21,'andrew':22,'keanu':25}
>>> list(d.values())
[23,21,22,25]
```

## d.pop()
> Removes the key from the Dictionary

```bash
>>> d = {'alex':23,'martin':21,'andrew':22,'keanu':25}
>>> d.pop('alex')
>>>print(d)
d = {'martin':21,'andrew':22,'keanu':25}
```

## d.popitem()
> Removes a random key-value pair and return it as tuple

```bash
>>> d = {'alex':23,'martin':21,'andrew':22,'keanu':25}
>>> d.popitem()
('keanu', 25)
>>> print(d)
{'alex': 23, 'martin': 21, 'andrew': 22}
```

## d.update()
> Merges a Dictionary with another Dictionary

```bash
>>> d1 = {'alex':23,'martin':21,'andrew':22,'keanu':25}
>>> d2 = {'stephen':31, 'paulo':37, 'Robin':25, 'Richard':34}
>>> d1.update(d2)
>>>print(d1)
{'alex': 23, 'martin': 21, 'andrew': 22, 'keanu': 25, 'stephen': 31, 'paulo': 37, 'Robin': 25, 'Richard': 34}
```