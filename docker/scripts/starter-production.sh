#!/bin/bash

# This file define what should be executed when docker "production" container is started by default.

# Running multiple commands parallelly.
poetry run task docs-serve &
poetry run start
wait
