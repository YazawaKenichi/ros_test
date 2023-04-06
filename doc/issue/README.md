# UI 表示がされなくなってしまった！

IP : 192.168.0.79

history.log は `xavier@192.168.0.79:/var/log/apt/history.log` のもの

# 参考になりそうなサイト
- [apt update は絶対に禁止](http://keibasys.seesaa.net/article/481862393.html)
- [

# 以下実行したコマンドと、何を返したか
状況、画面が真っ青になってから（再起動した後）SSH でつないだ
``` cmd
xavier@ubuntu:~$ sudo apt install --reinstall xorg
[sudo] password for xavier: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 cuda-libraries-dev-11-4 : Depends: cuda-profiler-api-11-4 (>= 11.4.239) but it is not going to be installed
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).
xavier@ubuntu:~$ sudo apt --fix-broken install
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Correcting dependencies... Done
The following packages were automatically installed and are no longer required:
  apt-clone archdetect-deb bogl-bterm busybox-static cryptsetup-bin cuda-nvprof-11-4 dctrl-tools dpkg-repack gir1.2-goa-1.0
  gir1.2-timezonemap-1.0 gir1.2-xkl-1.0 grub-common libavresample-dev libavresample4 libdc1394-22-dev libdebian-installer4 libexif-dev
  libfwupdplugin1 libgdcm-dev libgphoto2-dev libilmbase-dev libopencv4.2-java libopencv4.2-jni libopenexr-dev libraw1394-dev
  libtimezonemap-data libtimezonemap1 libxmlb1 os-prober python3-icu python3-pam rdate tasksel tasksel-data
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  cuda-profiler-api-11-4
The following NEW packages will be installed:
  cuda-profiler-api-11-4
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
786 not fully installed or removed.
Need to get 0 B/18.6 kB of archives.
After this operation, 90.1 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
debconf: delaying package configuration, since apt-utils is not installed
(Reading database ... 240492 files and directories currently installed.)
Preparing to unpack .../cuda-profiler-api-11-4_11.4.239-1_arm64.deb ...
Unpacking cuda-profiler-api-11-4 (11.4.239-1) ...
dpkg: error processing archive /var/cache/apt/archives/cuda-profiler-api-11-4_11.4.239-1_arm64.deb (--unpack):
 trying to overwrite '/usr/local/cuda-11.4/targets/aarch64-linux/include/cudaProfiler.h', which is also in package cuda-nvprof-11-4 11.4.166-1
Errors were encountered while processing:
 /var/cache/apt/archives/cuda-profiler-api-11-4_11.4.239-1_arm64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)

```

