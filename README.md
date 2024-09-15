# My custom OpenWrt builds

The goal of this repository is containing all the configuration and tools needed to generate *OpenWrt* builds for my home routers.

## Router configurations explained

### Common

* Dropbear removed. Instead, OpenSSH with SFTP support is installed
* LUCI with nginx (and SSL support) installed
* LUCI ttyd installed
* LUCI WiFi-Schedule installed
* wpad with OpenSSL installed

### Xiaomi AX3600

* ZeroTier installed
* Unbound installed
* Adblock-fast installed

### Xiaomi AX3000T

*



## How-to

First, clone the repository in your computer:

```sh
git clone --recursive git@github.com:AgustinLorenzo/openwrt.git
```

## Generate builds manually

[!IMPORTANT]
Due to *OpenWrt* requirements, the following instructions are recommended to be done in a Linux machine.




## Generate builds using GitHub Actions

#### With `act`

[!IMPORTANT]
Due to *OpenWrt* requirements, the following instructions are recommended to be done in a Linux machine.

Follow the [`act` installation instructions](https://nektosact.com/installation/index.html).

Execute:

* For *Xiaomi AX3000T*:

```sh
act -W '.github/workflows/xiaomi_ax3000t.yaml' -j 'build'
```

* For *Xiaomi AX3600*:

```sh
act -W '.github/workflows/xiaomi_ax3600.yaml' -j 'build'
```

#### With the GitHub nodes
