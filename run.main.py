from obfuscators import obfuscators, util
import argparse as A
import sys

#Scripts applies obfuscation methods one by one.

def main():
    parser = A.ArgumentParser(description="Program for obfuscating APK files")
    parser.add_argument('-i', '--infile', required=True, help="Input file name")
    parser.add_argument('-o', '--outfile', required=False, help="Output file name. Defaults to input file name (i.e. in place obfuscate)")
    parser.add_argument('obf_list', nargs='+', choices = obfuscators.all_obfuscators, metavar = 'OBFUSCATOR', help="List of obfuscators to apply.")
    args = parser.parse_args()

    infile = args.infile
    outfile = args.outfile or args.infile
    obf_list = args.obf_list
    if(len(obf_list) != 0):
        if(outfile != infile):
            try:
                util.copy_file(infile, outfile)
            except Exception as e:
                sys.stderr.write("Unable to perform copy from {0} to {1}", infile, outfile)
                sys.exit(1)
        obfuscators.apply_dir(outfile, obf_list)


if __name__ == '__main__':
    main()