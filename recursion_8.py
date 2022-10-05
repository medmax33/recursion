import os


def recursion_find_all_files(path: str, file_list: list = None) -> list:
    # define result filelist
    if file_list is None:
        file_list = []

    # scan path, define pathname and filename
    with os.scandir(path) as cycle:
        for item in cycle:
            if item.is_dir():
                # dive in subfolder
                recursion_find_all_files(path + '/' + item.name, file_list)
            elif item.is_file():
                # append filename to filelist
                file_list.append(item.name)

    # return result filelist
    return file_list
