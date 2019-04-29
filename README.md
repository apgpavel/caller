<!---
Copyright PavelG
MIT License
--->

# C2C forma dialer / C2C caller form

This is repository of C2C caller via VOIPNOW engine

## Wymagania / Recuirements

    Python version 3.5 or 3.6 

## Pre-start

# Edit config file
    vi config/config.ini
    
# należy ustawić kolejne konfiguracje z poprawnym numerem rozszerzenia, kluczem API i ApiSecret
# need set next values with correct and actual extension number, API key and ApiSecret
    
    ExtensionNumber =
    AppKey =
    AppSecret =

## dla uruchomienia aplikacji wymaga polecenia w głównym folderze projektu
## for start application need start commands in the root folder of project

    python init.py
    
or

    docker build -t ifonprod
    docker run --rm -d -p 80:8081 ifonprod:latest .


