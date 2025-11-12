# File_Transfer  

A simple file-transfer utility written in Python, consisting of a server (`file_server.py`) and a client (`file_client.py`) that allow transferring files over a network between machines.

## Table of Contents  
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Setup & Installation](#setup--installation)  
- [Usage](#usage)  
  - [Running the Server](#running-the-server)  
  - [Running the Client](#running-the-client)  
- [How it Works](#how-it-works)  
- [Contributing](#contributing)  
- [License](#license)  

## Features  
- Server listens on a specified port and accepts incoming file-transfer requests.  
- Client connects to the server and sends a selected file.  
- Simple and minimal dependencies (pure Python).  
- Easy to understand and extend — good for learning network programming basics.  

## Prerequisites  
- Python 3.x installed on both the server and client machines.  
- Network connectivity between the machines.  
- (Optional) Firewall or port forwarding configured if transferring across networks.  

## Setup & Installation  
```bash  
git clone https://github.com/RajnandaniGupta-51/File_Transfer.git  
cd File_Transfer  
