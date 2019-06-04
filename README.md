YAAMO: Yet Another Android Malware Obfuscator
========================================

YAAMO is based on [AAMO](https://github.com/necst/aamo) by [NECSTLab](https://github.com/necst), with the improvements given by user [Aleksandr Pilgun](https://github.com/necst). It is based on apktool 2.2.4 and smali/baksmali 2.2.1.

Usage
-----

```
     $ run.main.py [-h] [-a] -i INFILE [-o OUTFILE]
                   [-L [OBFUSCATOR [OBFUSCATOR ...]]]
```

`OBFUSCATOR` is one of the following:

```
    obfuscator_to_apply = [
        'Resigned', 'Alignment',    'Rebuild',   'Fields',
        'Debug',    'Indirections', 'Defunct',   'StringEncrypt',
        'Renaming', 'Reordering',   'Goto',      'ArithmeticBranch',
        'Nop',      'Asset',        'Intercept', 'Raw',
        'Resource', 'Lib',          'Manifest',  'Reflection']
```

Obfuscation Operators
---------------------

[[TODO]]

Bugs
----

* Obfuscating large DEX files may cause the method count to grow over the maximum 65,536.

