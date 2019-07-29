# How to use

1. Turn off the VPN
1. Shutdown the virtualbox (if you have)
1. ./env\_setup.sh
1. Done!

# Possible problems
## 1. creating host: Error executing step: Creating VM （Mac）
```
Starting local Kubernetes v1.10.0 cluster...
Starting VM...
E0911 13:34:45.394430   41676 start.go:174] Error starting host: Error 
creating host: Error executing step: Creating VM.
: Error setting up host only network on machine start: The host-only 
adapter we just created is not visible. This is a well known 
VirtualBox bug. You might want to uninstall it and reinstall at least 
version 5.0.12 that is is supposed to fix this issue.
```
## Solution
* Restarting won't work if VirtualBox isn't installed correctly.
* System Preferences -> Security & Privacy -> Allow -> Then allow the software corporation (in this case Oracle)
* Restart
