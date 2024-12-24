#!/bin/bash

PYTHONPATH=$(pwd) pytest --cov=app --cov-report=term-missing tests "${@}"
