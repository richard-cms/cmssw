#!/bin/sh
for file in Configuration/GenProduction/python/Pyquen_Un*.py
do
    stripped_name=$(echo ${file} | sed 's/python\///' | sed 's/.py//')
    echo files=${stripped_name} output=$(basename ${file/%.py/_v2.root})
    cmsRun genPartTest.py files=${stripped_name} output=$(basename ${file/%.py/_v2.root})
done
