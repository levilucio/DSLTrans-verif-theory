#!/bin/python

import os
import subprocess

def convert(fname):
    if not fname.endswith(".png") and not fname.endswith(".svg"):
        return
    
    fname_as_pdf = fname.replace(".svg", ".pdf")
    
    try:
        pdf_mod_time = os.path.getmtime(fname_as_pdf)
    except Exception:
        pdf_mod_time = 0
        
    
    if os.path.getmtime(fname) <= pdf_mod_time:
        return
     
    print("Converting: " + fname)
        
    if fname.endswith(".png"):
        subprocess.call("convert -density 1024x1024 " + fname + " " + fname_as_pdf, shell=True)
    elif fname.endswith(".svg"):
        #subprocess.call("inkscape --verb=FitCanvasToDrawing --verb=FileSave --verb=FileClose " + fname, shell=True)
        subprocess.call("inkscape " + fname + " --export-pdf=" + fname_as_pdf, shell=True)

def convert_dir(d):
    print(d)
    for fname in os.listdir(d):
        path = d + "/" + fname
        print(path)
        if os.path.isdir(fname):
            convert_dir(path)
        else:
            convert(path)

convert_dir(".")
