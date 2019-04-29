<!---
Copyright PavelG
MIT License
--->

# C2C caller form

This is repository of C2C caller via VOIPNOW engine

## Recuirements

    Python3.5

## Pre-start

    vi config/config.ini
    # need set next values with correct and actual extension number, API key and ApiSecret
    
    ExtensionNumber =
    AppKey =
    AppSecret =

## for start application need start command in the root folder of project

    python init.py
    or
    docker build -t ifonprod
    docker run --rm -d -p 80:8081 ifonprod:latest


