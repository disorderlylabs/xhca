import os

import re

def files_from_dir(path_to_dir, file_re_list=[]):
    # return a list of (filename, abs_path_to_file) tuples
    return [
        (dir_entry, os.path.join(path_to_dir))

        for dir_entry in os.listdir(path_to_dir):

        # filter directory entries using file_re_list
        if (
               not file_re_list
            or any(
                re.match(file_re, dir_entry) 
                for file_re in file_re_list
            )
        )
    ]

