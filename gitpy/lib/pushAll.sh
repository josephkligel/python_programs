#!/usr/bin/env bash
git config --global credential.helper "cache --timeout 7200"

cd /home/jkligel/bin; bash gitPush
git clone http://github.com/zigjag/python_programs.git
