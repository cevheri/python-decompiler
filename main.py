import os
import uncompyle6


def decompile(your_directory):
    """
    Compiles decompiled Python files and extracts them to the same folder
    :param your_directory: decompiled files
    :return: void
    """
    for dirpath, b, filenames in os.walk(your_directory):

        # files to be bypassed, not scanned
        if 'venv' in dirpath or 'env' in dirpath or '.git' in dirpath:
            continue

        for filename in filenames:
            if not filename.endswith('.pyc'):
                continue

            filepath = dirpath + '/' + filename
            original_filename = filename.split('.')[0]
            original_filepath = dirpath + '/' + original_filename + '.py'
            with open(original_filepath, 'w') as f:
                try:
                    uncompyle6.decompile_file(filepath, f)
                    print("decompiled file: " + filepath)
                except Exception as ex:
                    print("Decompiled Error filename -> " + filepath + ". " + ex)


if __name__ == '__main__':
    decompile("/home/cevher/decompiled_project")
