#!/bin/bash

# This script is used to install other language realated scripts folder's dependencies. (Ex. nodejsRunner)

# Sourcing "bashrc" to update things. (Ex. asdf)
source ~/.bashrc

cd ./scripts/nodejsRunner
npm install
