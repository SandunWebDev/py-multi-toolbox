#!/bin/bash

# NOTE : Notice shebangs used in these scripts are "bash" not "sh".

# When this file is mentioned as "ENTRYPOINT" in "Dockerfile", Every time container is started, this will run first. (Even before "CMD" command.)
# Currently we are using this to make sure Poetry's Python Virtual Envroment is activated.

set -e

# Sourcing ".bashrc" file so $PATH is updated and stuff. (Ex. asdf Loaded)
source ~/.bashrc

# Activating our virtual environment.
. .venv/bin/activate

# You can put other setup logic here. (If applicable)
echo "-------------------------------------------------------------------------------------------------------------"
echo "# Starting Container"
echo "  Executing $0 $@"
echo "-------------------------------------------------------------------------------------------------------------"
echo ""

# Evaluating passed command.
exec "$@"
