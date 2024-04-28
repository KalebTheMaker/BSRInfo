# BSRInfo

## Pi Config
### Install Raspberry Pi OS lite
Currently using bookworm lite no desktop. Follow normal install procedure
### Configure Display
Follow instructions here: [Waveshare Install Instructions](https://www.waveshare.com/wiki/3.5inch_DPI_LCD "Waveshare Install Instructions")
### Install Samba
`sudo apt install samba samba-common-bin`
`sudo mkdir /opt/BSRInfo`
`sudo chown <user>.<user> /opt/BSRInfo`
`sudo vi /etc/samba/smb.conf`
Put the following block at the end of the file
```
    [BSRInfoDev]
    path = /opt/BSRInfo
    writable=yes
    create mask=0777
    directory mask=0777
    public=no
```
Create password:
` sudo smbpasswd -a <user>`
Restart Samba
`sudo systemctl restart smbd`
