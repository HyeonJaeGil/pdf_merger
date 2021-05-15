#!/usr/bin/env python3

import argparse
from glob import glob
import os

from PyPDF2 import PdfFileMerger


def MergeFile(keys, directory, sub_dir='merged', bookname='merged'):

    os.chdir(directory)
    if not os.path.isdir(sub_dir):
        os.mkdir(sub_dir)

    targets=[]
    fList=os.listdir('.')
    for f in fList:
        for key in keys:
            if ((key in f) and (f not in targets)): #prevent repetition
                targets.append(f)
    targets.sort()
    print(targets)

    merger=PdfFileMerger()
    for target in targets:
        merger.append(target)
    merger.write(f"{directory}/{sub_dir}/{bookname}.pdf")
    merger.close()

    print("saved {bookname}.pdf in {directory}/{sub_dir}".format(bookname=bookname, directory=directory, sub_dir=sub_dir))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="directory where files to be merged live")
    parser.add_argument('-l','--list',help='list of target files', type=str)
    args = parser.parse_args()
    directory = args.directory
    targets=[items for items in args.list.split(',')]

    MergeFile(targets, directory)

    # usage
    # python3 mergePDF.py -d {YOUR_DIRECTORY} -l {YOUR_KEYS}
    # python3 mergePDF.py -d /home/hj/lectures/convex_optimization -l 02-,03-