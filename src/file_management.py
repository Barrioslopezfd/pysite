import os
import shutil


def copy_from_to(src, dst):
    rm_or_create(dst)

    src_tree = os.listdir(src)
    if src_tree == []:
        return
    for s in src_tree:
        src_cp = os.path.join(src, s)
        dst_cp = os.path.join(dst, s)
        if os.path.isdir(src_cp):
            os.mkdir(dst_cp)
            copy_from_to(src_cp, dst_cp)
        elif os.path.isfile(src_cp):
            shutil.copy(src_cp, dst_cp)


def rm_or_create(dst):
    if os.path.exists(dst) and os.listdir(dst) is not []:
        rm_files(dst)
        rm_dirs(dst)
    elif not os.path.exists(dst):
        os.mkdir(dst)


def rm_files(dst):
    dst_tree = os.listdir(dst)
    if dst_tree == []:
        return
    for d in dst_tree:
        temp = os.path.join(dst, d)
        if os.path.isfile(temp):
            os.remove(temp)
        else:
            rm_files(temp)


def rm_dirs(dst):
    dst_tree = os.listdir(dst)
    if dst_tree == []:
        return
    for d in dst_tree:
        temp = os.path.join(dst, d)
        rm_dirs(temp)
        os.rmdir(temp)
