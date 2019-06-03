import util as u
import re
import os


def append_defunct_method(defunct_str, smali_file_list):
    """Append to each smali class file the defunct method"""
    for smali_file in smali_file_list:  # For each file
        for smali_line in u.open_file_input(smali_file):  # For each line
            print smali_line,
            if re.search(r'^([ ]*?)# direct methods', smali_line) is not None:  # At the top of the direct methods section
                print defunct_str  # Append the defunct method


def append_defunct_class_now(base_dir, curr_dir, incremental):
    """Append a random generated class file to the class tree"""

    if base_dir == curr_dir:
        class_path = ''
    else:
        class_path = curr_dir.replace(base_dir, '')  # Remove the root reference
        class_path = os.path.relpath(curr_dir, base_dir)
    
    defunct_class = u.get_defunct_class()
    random_class_name = u.get_random(True, 16) + str(incremental)
    
    defunct_class = defunct_class.replace('*ClassName*', os.path.join(class_path, random_class_name))  # Random class name
    defunct_class = defunct_class.replace('*String1*', u.get_random(True, 16))  # Random string
    defunct_class = defunct_class.replace('*String2*', u.get_random(True, 16))  # Random string
    defunct_class = defunct_class.replace('*MethodName*', u.get_random(True, 16))  # Random method
    defunct_class = defunct_class.replace('*SourceName*', u.get_random(True, 16))  # Random source
    u.write_text_file(os.path.join(curr_dir, random_class_name + '.smali'), defunct_class)  # Write the class file


def append_defunct_class(smali_dir_list):
    """Append some classes files to the class tree"""
    base_path = smali_dir_list[-1]  # The root of the class tree
    for smali_dir in smali_dir_list:  # For each dir
        for count_class in range(u.random_nop_interval()):
            append_defunct_class_now(base_path, smali_dir, count_class)


def obfuscate():
    """ The main obfuscator function """
    append_defunct_method(u.get_defunct_method(), u.load_smali_file())
    append_defunct_class(u.load_all_smali_dirs())
