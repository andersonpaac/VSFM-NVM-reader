__author__ = 'andersonpaac'
import argparse

def args():
    parser=argparse.ArgumentParser(description="TRIX")
    parser.add_argument("-f","--filename",default="")
    parser.add_argument("-o","--out",default="")
    parser.add_argument("-t","--thresh",default="")
    return parser
