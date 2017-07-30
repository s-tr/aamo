from obfuscators import obfuscators

#Scripts applies obfuscation methods one by one.

obfuscator_to_apply = ['Resigned',
                       'Alignment',
                       'Rebuild',
                       'Fields',
                       'Debug',
                       'Indirections',
                       'Defunct',
                       'StringEncrypt',
                       'Renaming',
                       'Reordering',
                       'Goto',
                       'ArithmeticBranch',
                       'Nop',
                       'Asset',
                       'Intercept',
                       'Raw',
                       'Resource',
                       'Lib',
                       'Restring',
                       'Manifest',
                       'Reflection'
                       ]

apk_paths = "c:\\projects\\aamo\\input\\0016A78BF0281D008A8280130137BB56FC9FEC998E861A6A3C6A0409202BBE52-{0}.apk"
names = [(apk_paths.format(obf_proc), obf_proc) for obf_proc in obfuscator_to_apply]

def main():
    for n in names:
        print(n)
        obfuscators.apply_dir(n[0], [n[1]])

if __name__ == '__main__':
    main()