#!/bin/sh
for file in Pyquen_EmEn*80*35*.py
do
    echo files=${file/%.py/} output=$(basename ${file/%.py/.root})
    cmsRun genPartTest.py files=${file/%.py/} output=$(basename ${file/%.py/.root})
done
