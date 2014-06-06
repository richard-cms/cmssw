#!/bin/sh
for file in Configuration/GenProduction/python/Pyquen_EmEn*170*35*.py
do
    stripped_name=$(echo ${file} | sed 's/python\///' | sed 's/.py//')
    echo files=${stripped_name} output=$(basename ${file/%.py/_2.root})
    cmsRun genPartTest.py files=${stripped_name} output=$(basename ${file/%.py/_2.root})
done
