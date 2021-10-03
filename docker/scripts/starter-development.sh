#!/bin/bash

# This file define what should be executed when docker "development" container is started by deafult.

# Running multiple commands parallelly.
poetry run task docs-serve &
poetry run task dev
wait
