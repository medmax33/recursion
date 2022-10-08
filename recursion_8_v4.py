import os


def recursion_find_all_files(path: str) -> list:
    # local file list
    file_list: list = []

    # scan path, define pathname and filename
    with os.scandir(path) as cycle:
        for item in cycle:
            if item.is_dir():
                # dive in subfolder
                file_list.extend(recursion_find_all_files(path + '/' + item.name))
            elif item.is_file():
                # append filename to filelist
                file_list.append(item.name)

    # return result filelist
    return file_list
