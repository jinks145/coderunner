# DG-SANDBOX
- A simple, crude proof of concept for a cpp code runtime api using docker

## Structure
    - Overview
        Simple MVC-based microservice app with server-side computation
    
    - Current Implementation: used the following containers for structure
        1. db: a postgresql container
        2. sandbox: runtime enviornment for code execution
        3. website: main front-end for clients

## Version
- Version 1.0

## Capacity:
    - Currently supports single-file cpp code

## Future Goals:
    - Convert the codebase for the web application into API and restructuring
    - improve file submission logistics
        1. securing file transmission protocol
        2. Direct file-blob to compilation support
    - add unit test functionality using pytest and string comparison
