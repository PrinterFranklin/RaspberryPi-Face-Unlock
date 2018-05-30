#!/bin/bash
raspistill -o test.jpg -t 2000 
python face_search.py
