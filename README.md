# My custom OpenWrt builds

The goal of this repository is containing all the configuration and tools needed to generate *OpenWrt* builds for my home routers.

## Router configurations explained

### Common

* Dropbear removed. Instead, OpenSSH with SFTP support installed
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

## How to generate the builder docker image

```sh
docker build -t openwrt_builder -f docker/openwrt_builder.Dockerfile .
```

## How-to generate builds

First, clone the repository in your computer:

```sh
git clone --recursive git@github.com:AgustinLorenzo/openwrt.git
```

### Manually

First, we deploy a docker container:

```sh
docker run -it --name openwrt openwrt_builder /bin/bash
```

Once inside the container, execute:

```sh
git clone --recursive https://github.com/Hekkfern/my_custom_openwrt.git
cd my_custom_openwrt
```

Then, we start the building process inside the docker container:

* For *Xiaomi AX3000T*:

```sh
cd repos/openwrt_official
./scripts/feeds update -a
./scripts/feeds install -a
cp ../../configs/xiaomi_ax3000t/diffconfig .config
make defconfig
make -j $(($(nproc)+1)) download world
```

* For *Xiaomi AX3600*:

```sh
cd repos/openwrt_nss
./scripts/feeds update -a
./scripts/feeds install -a
cp ../../configs/xiaomi_ax3600/diffconfig .config
make defconfig
make -j $(($(nproc)+1)) download world
```

### Using GitHub Actions

### Using `act` (local "GitHub Actions")

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
