@echo off
coverage erase
coverage run -m pytest
coverage report -m