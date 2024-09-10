# My custom OpenWrt builds

The goal of this repository is containing all the configuration and tools needed to generate *OpenWrt* builds for my home routers.

## Getting started

First, clone the repository in your computer:

```sh
git clone --recursive git@github.com:AgustinLorenzo/openwrt.git
```

## How to generate the builds

### Manually

[!IMPORTANT]
Due to *OpenWrt* requirements, the following instructions are recommended to be done in a Linux machine.




### Using GitHub Actions

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
