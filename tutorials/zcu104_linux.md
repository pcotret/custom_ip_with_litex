# Running a default Vexriscv with a full Linux system

Working on a ZCU104 board.
All instructions are given here: https://github.com/litex-hub/linux-on-litex-vexriscv/

Basically, do not forget to add a SODIMM memory module (4GB in our case). Otherwise, you may get [stuck at boot](https://github.com/litex-hub/linux-on-litex-vexriscv/issues/417).

```bash
$ sudo ./litex_term --images=/home/cotretpa/Documents/linux-on-litex-vexriscv/images/boot.json /dev/ttyUSB3
00000000000000000000| delays: -
  m1, b02: |00000000000000000000000000000000| delays: -
  m1, b03: |11110000000000000000000000000000| delays: 25+-25
  m1, b04: |00000011111111111111000000000000| delays: 204+-115
  m1, b05: |00000000000000000000000111111111| delays: 437+-73
  m1, b06: |00000000000000000000000000000000| delays: -
  m1, b07: |00000000000000000000000000000000| delays: -
  best: m1, b04 delays: 204+-113
  m2, b00: |00000000000000000000000000000000| delays: -
  m2, b01: |00000000000000000000000000000000| delays: -
  m2, b02: |00000000000000000000000000000000| delays: -
  m2, b03: |10000000000000000000000000000000| delays: 04+-04
  m2, b04: |00011111111111111100000000000000| delays: 158+-112
  m2, b05: |00000000000000000000111111111111| delays: 415+-96
  m2, b06: |00000000000000000000000000000000| delays: -
  m2, b07: |00000000000000000000000000000000| delays: -
  best: m2, b04 delays: 159+-112
  m3, b00: |00000000000000000000000000000000| delays: -
  m3, b01: |00000000000000000000000000000000| delays: -
  m3, b02: |00000000000000000000000000000000| delays: -
  m3, b03: |10000000000000000000000000000000| delays: 04+-04
  m3, b04: |00011111111111111100000000000000| delays: 160+-116
  m3, b05: |00000000000000000000111111111111| delays: 415+-95
  m3, b06: |00000000000000000000000000000000| delays: -
  m3, b07: |00000000000000000000000000000000| delays: -
  best: m3, b04 delays: 160+-115
  m4, b00: |00000000000000000000000000000000| delays: -
  m4, b01: |00000000000000000000000000000000| delays: -
  m4, b02: |00000000000000000000000000000000| delays: -
  m4, b03: |00000000000000000000000000000000| delays: -
  m4, b04: |11111111111111100000000000000000| delays: 111+-111
  m4, b05: |00000000000000000111111111111111| delays: 381+-117
  m4, b06: |00000000000000000000000000000000| delays: -
  m4, b07: |00000000000000000000000000000000| delays: -
  best: m4, b05 delays: 381+-115
  m5, b00: |00000000000000000000000000000000| delays: -
  m5, b01: |00000000000000000000000000000000| delays: -
  m5, b02: |00000000000000000000000000000000| delays: -
  m5, b03: |00000000000000000000000000000000| delays: -
  m5, b04: |11111111111111000000000000000000| delays: 105+-105
  m5, b05: |00000000000000000111111111111110| delays: 371+-112
  m5, b06: |00000000000000000000000000000000| delays: -
  m5, b07: |00000000000000000000000000000000| delays: -
  best: m5, b05 delays: 371+-111
  m6, b00: |00000000000000000000000000000000| delays: -
  m6, b01: |00000000000000000000000000000000| delays: -
  m6, b02: |00000000000000000000000000000000| delays: -
  m6, b03: |00000000000000000000000000000000| delays: -
  m6, b04: |11111111111000000000000000000000| delays: 89+-89
  m6, b05: |00000000000000111111111111110000| delays: 333+-114
  m6, b06: |00000000000000000000000000000001| delays: 502+-09
  m6, b07: |00000000000000000000000000000000| delays: -
  best: m6, b05 delays: 333+-112
  m7, b00: |00000000000000000000000000000000| delays: -
  m7, b01: |00000000000000000000000000000000| delays: -
  m7, b02: |00000000000000000000000000000000| delays: -
  m7, b03: |00000000000000000000000000000000| delays: -
  m7, b04: |11111111110000000000000000000000| delays: 76+-76
  m7, b05: |00000000000001111111111111100000| delays: 309+-111
  m7, b06: |00000000000000000000000000000011| delays: 490+-21
  m7, b07: |00000000000000000000000000000000| delays: -
  best: m7, b05 delays: 310+-112
Switching SDRAM to hardware control.
Memtest at 0x40000000 (2.0MiB)...
  Write: 0x40000000-0x40200000 2.0MiB     
   Read: 0x40000000-0x40200000 2.0MiB     
Memtest OK
Memspeed at 0x40000000 (Sequential, 2.0MiB)...
  Write speed: 199.8MiB/s
   Read speed: 101.2MiB/s

--============== Boot ==================--
Booting from serial...
Press Q or ESC to abort boot completely.
sL5DdSMmkekro
[LITEX-TERM] Received firmware download request from the device.
[LITEX-TERM] Uploading /home/cotretpa/Documents/linux-on-litex-vexriscv/images/Image to 0x40000000 (7531468 bytes)...
[LITEX-TERM] Upload calibration... (inter-frame: 10.00us, length: 64)
[LITEX-TERM] Upload complete (9.9KB/s).
[LITEX-TERM] Uploading /home/cotretpa/Documents/linux-on-litex-vexriscv/images/rv32.dtb to 0x40ef0000 (2383 bytes)...
[LITEX-TERM] Upload calibration... (inter-frame: 10.00us, length: 64)
[LITEX-TERM] Upload complete (9.5KB/s).
[LITEX-TERM] Uploading /home/cotretpa/Documents/linux-on-litex-vexriscv/images/rootfs.cpio to 0x41000000 (3781632 bytes)...
[LITEX-TERM] Upload calibration... (inter-frame: 10.00us, length: 64)
[LITEX-TERM] Upload complete (9.9KB/s).
[LITEX-TERM] Uploading /home/cotretpa/Documents/linux-on-litex-vexriscv/images/opensbi.bin to 0x40f00000 (53640 bytes)...
[LITEX-TERM] Upload calibration... (inter-frame: 10.00us, length: 64)
[LITEX-TERM] Upload complete (9.9KB/s).
[LITEX-TERM] Booting the device.
[LITEX-TERM] Done.
Executing booted program at 0x40f00000

--============= Liftoff! ===============--

OpenSBI v0.8-1-gecf7701
   ____                    _____ ____ _____
  / __ \                  / ____|  _ \_   _|
 | |  | |_ __   ___ _ __ | (___ | |_) || |
 | |  | | '_ \ / _ \ '_ \ \___ \|  _ < | |
 | |__| | |_) |  __/ | | |____) | |_) || |_
  \____/| .__/ \___|_| |_|_____/|____/_____|
        | |
        |_|

Platform Name       : LiteX / VexRiscv-SMP
Platform Features   : timer,mfdeleg
Platform HART Count : 8
Boot HART ID        : 0
Boot HART ISA       : rv32imasu
BOOT HART Features  : pmp,time
BOOT HART PMP Count : 16
Firmware Base       : 0x40f00000
Firmware Size       : 124 KB
Runtime SBI Version : 0.2

MIDELEG : 0x00000222
MEDELEG : 0x0000b109
[    0.000000] Linux version 5.14.0 (florent@panda) (riscv32-buildroot-linux-gnu-gcc.br_real (Buildroot 2021.08-381-g279167ee8d) 10.3.0, GNU ld (GNU Binutils) 2.36.1) #1 SMP Tue Sep 21 12:57:31 CEST 2021
[    0.000000] Machine model: xilinx_zcu104
[    0.000000] earlycon: liteuart0 at I/O port 0x0 (options '')
[    0.000000] Malformed early option 'console'
[    0.000000] earlycon: liteuart0 at MMIO 0xf0001000 (options '')
[    0.000000] printk: bootconsole [liteuart0] enabled
[    0.000000] Zone ranges:
[    0.000000]   Normal   [mem 0x0000000040000000-0x000000007fffffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000040000000-0x000000007fffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000040000000-0x000000007fffffff]
[    0.000000] SBI specification v0.2 detected
[    0.000000] SBI implementation ID=0x1 Version=0x8
[    0.000000] SBI TIME extension detected
[    0.000000] SBI IPI extension detected
[    0.000000] SBI RFENCE extension detected
[    0.000000] SBI v0.2 HSM extension detected
[    0.000000] riscv: ISA extensions aimp
[    0.000000] riscv: ELF capabilities aim
[    0.000000] percpu: Embedded 8 pages/cpu s11340 r0 d21428 u32768
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 260096
[    0.000000] Kernel command line: console=liteuart earlycon=liteuart,0xf0001000 rootwait root=/dev/ram0
[    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
[    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
[    0.000000] Sorting __ex_table...
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] Memory: 1023284K/1048576K available (5685K kernel code, 572K rwdata, 883K rodata, 209K init, 221K bss, 25292K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
[    0.000000] rcu: Hierarchical RCU implementation.
[    0.000000] rcu: 	RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=1.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=1
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] riscv-intc: 32 local interrupts mapped
[    0.000000] plic: interrupt-controller@f0c00000: mapped 32 interrupts with 1 handlers for 2 contexts.
[    0.000000] random: get_random_bytes called from start_kernel+0x4ac/0x63c with crng_init=0
[    0.000000] riscv_timer_init_dt: Registering clocksource cpuid [0] hartid [0]
[    0.000000] clocksource: riscv_clocksource: mask: 0xffffffffffffffff max_cycles: 0x39a85c4118, max_idle_ns: 881590405314 ns
[    0.000014] sched_clock: 64 bits at 125MHz, resolution 8ns, wraps every 4398046511100ns
[    0.008962] Console: colour dummy device 80x25
[    0.012877] Calibrating delay loop (skipped), value calculated using timer frequency.. 250.00 BogoMIPS (lpj=500000)
[    0.023229] pid_max: default: 32768 minimum: 301
[    0.030303] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
[    0.037140] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
[    0.061761] ASID allocator using 9 bits (512 entries)
[    0.067570] rcu: Hierarchical SRCU implementation.
[    0.075777] smp: Bringing up secondary CPUs ...
[    0.079266] smp: Brought up 1 node, 1 CPU
[    0.087964] devtmpfs: initialized
[    0.111737] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.121507] futex hash table entries: 256 (order: 2, 16384 bytes, linear)
[    0.134011] NET: Registered PF_NETLINK/PF_ROUTE protocol family
[    0.267355] pps_core: LinuxPPS API ver. 1 registered
[    0.271482] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.280878] PTP clock support registered
[    0.286994] FPGA manager framework
[    0.300371] clocksource: Switched to clocksource riscv_clocksource
[    0.437842] NET: Registered PF_INET protocol family
[    0.443327] IP idents hash table entries: 16384 (order: 5, 131072 bytes, linear)
[    0.465889] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
[    0.474257] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
[    0.482643] TCP bind hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.490461] TCP: Hash tables configured (established 8192 bind 8192)
[    0.497001] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
[    0.503325] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
[    0.524973] Unpacking initramfs...
[    0.629249] workingset: timestamp_bits=30 max_order=18 bucket_order=0
[    0.817515] io scheduler mq-deadline registered
[    0.821263] io scheduler kyber registered
[    1.053169] LiteX SoC Controller driver initialized
[    1.584875] Initramfs unpacking failed: invalid magic at start of compressed archive
[    1.646885] Freeing initrd memory: 8192K
[    2.203907] f0001000.serial: ttyLXU0 at MMIO 0x0 (irq = 0, base_baud = 0) is a liteuart
[    2.211902] printk: console [liteuart0] enabled
[    2.211902] printk: console [liteuart0] enabled
[    2.220836] printk: bootconsole [liteuart0] disabled
[    2.220836] printk: bootconsole [liteuart0] disabled
[    2.248876] i2c_dev: i2c /dev entries driver
[    2.284414] NET: Registered PF_INET6 protocol family
[    2.299320] Segment Routing with IPv6
[    2.302458] In-situ OAM (IOAM) with IPv6
[    2.306919] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    2.322519] NET: Registered PF_PACKET protocol family
[    2.335202] Freeing unused kernel image (initmem) memory: 204K
[    2.340681] Kernel memory protection not selected by kernel config.
[    2.346738] Run /init as init process
Starting syslogd: OK
Starting klogd: OK
Running sysctl: OK
Saving random seed: [    4.122723] random: dd: uninitialized urandom read (512 bytes read)
OK
Starting network: OK

Welcome to Buildroot
buildroot login: root
                   __   _
                  / /  (_)__  __ ____ __
                 / /__/ / _ \/ // /\ \ /
                /____/_/_//_/\_,_//_\_\
                      / _ \/ _ \
   __   _ __      _  _\___/_//_/         ___  _
  / /  (_) /____ | |/_/__| | / /____ __ / _ \(_)__ _____  __
 / /__/ / __/ -_)>  </___/ |/ / -_) \ // , _/ (_-</ __/ |/ /
/____/_/\__/\__/_/|_|____|___/\__/_\_\/_/|_/_/___/\__/|___/
                  / __/  |/  / _ \
                 _\ \/ /|_/ / ___/
                /___/_/  /_/_/
  32-bit RISC-V Linux running on LiteX / VexRiscv-SMP.

login[69]: root login on 'console'
root@buildroot:~# echo 'Hello LiteX !'
Hello LiteX !
root@buildroot:~# cat /proc/cpuinfo 
processor	: 0
hart		: 0
isa		: rv32i2p0_ma
mmu		: sv32
```