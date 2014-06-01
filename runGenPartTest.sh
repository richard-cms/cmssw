#!/bin/sh
for file in Pyquen_EmEn*.py
do
    echo cmsRun genPartTest.py files=${file/%.py/} output=$(basename ${file/%.py/.root})
done
