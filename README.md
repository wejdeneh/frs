# SPIFFS Forensics

This repo is for Forensics SPRING 2025 project entitled : File systems for embedded devices

## About this project

This project focuses on SPIFFS. 
The main goals are : 
- to conduct a small research on its uses and characteristics
- to write a forensic tool that can list the files and directories, print its core data-structure information, and (if possible) recover deleted files.

## What is SPIFFS? 

SPIFFS (SPI Flash File System ) is a lightweight, log-structured filesystem designed for embedded devices that support SPI protocol.
It is notably used on ESP32 systems (although many newer designs mostly use LittleFS) to store user files like web assets, configuration data, sensor logs, etc.
It is also particularly useful for resource constrained (RAM) applications that use many small files, but also in applications where we require frequent R/W operations.
And because it has minimal per-file overhead, developers use SPIFFS to store HTML/CSS files for on-board web servers with no need for external storage. 

In embedded systems, SPIFFS is very useful because you need to store data logs, configuration settings and updates, also needing to remember user-entered settings or preferences. 
In this case, SPIFFS acts practically as a memory management and ensures that all data is maintained after the embedded device is powered off, and ideally, recovered. 

# Built with :

## Usage of the tool


## Authors

- [ ] Kawtar EL MAMOUN
- [ ] Wejden HAJ MEFTEH

## Project Status

