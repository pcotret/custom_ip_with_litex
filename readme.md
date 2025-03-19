# custom_ip_with_litex

> The goal of this repository is to show how to integrate a custom IP written in Verilog in a LiteX-based SoC design

> Many thanks to [Tianxu Li](https://labsticc.fr/en/directory/li-tianxu) for his help with the design of the AXI-lite read/write logic.

## Requirements

- This tutorial has been tested on Nexys4DDR and ZCU104 boards with Vivado 2024.2. It should work with other boards as long as it is supported by LiteX. This tutorial uses the Nexys4DDR default LiteX script: https://github.com/litex-hub/litex-boards/blob/master/litex_boards/targets/digilent_nexys4ddr.py.

- Tested with [LiteX](https://github.com/enjoy-digital/litex). Any recent version should work.

## Goal 

We want to build a very simple SoC with a RISC-V processor and a custom IP on a AXI-lite bus.

<img src="images/soc.drawio.png" alt="soc" width="50%"/>

The custom IP:
- Has three registers `reg_a`, `reg_b` and `reg_c`.
- Has a read/write logic for an AXI-lite bus.
- Computes a function `reg_c=f_n(reg_a,reg_b)`. In this first example, we will use a simple adder (`reg_c=reg_a+reg_b`).

## Description of the AXI-lite read/write logic

**todo. Need some details about how the FSM is built to have a correct read/write logic.**

## Custom IP design

The following two files are located in `<litex_install_directory>/litex/litex/soc/cores`.

### Verilog code 

See [files/custom_ip.v](./files/custom_ip.v)

### Python class for LiteX

See [files/custom_ip.py](./files/custom_ip.py)

## Integration of the custom IP in the main SoC script

The following file is located at `<litex_install_directory>/litex-boards/blob/master/litex_boards/targets/digilent_nexys4ddr.py`:

```diff
@@ -24,6 +24,9 @@ from litedram.phy import s7ddrphy
 
 from liteeth.phy.rmii import LiteEthPHYRMII
 
+from litex.soc.cores.custom_ip import CustomIP
+from litex.soc.integration.soc import SoCRegion
+
 # CRG ----------------------------------------------------------------------------------------------
 
 class _CRG(LiteXModule):
@@ -61,6 +64,7 @@ class BaseSoC(SoCCore):
         with_led_chaser        = True,
         with_video_terminal    = False,
         with_video_framebuffer = False,
+        with_custom_ip         = True,
         **kwargs):
         platform = digilent_nexys4ddr.Platform()
 
@@ -105,6 +109,13 @@ class BaseSoC(SoCCore):
             self.leds = LedChaser(
                 pads         = platform.request_all("user_led"),
                 sys_clk_freq = sys_clk_freq)
+        
+        if with_custom_ip:   
+            self.submodules.custom_ip = CustomIP(platform)
+            # Base address 
+            self.custom_ip_base = 0x30000000
+            # Available address range
+            self.custom_ip_size = 0x1000
+            self.bus.add_slave(name="custom_ip", slave=self.custom_ip.bus, region=SoCRegion(origin=self.custom_ip_base,
+                                                                                            size=self.custom_ip_size))
```

## Running the script

```bash
./digilent_nexys4ddr.py --bus-standard axi-lite --build --load
```

Test in the LiteX prompt:

```
litex> mem_list
Available memory regions:
ROM        0x00000000 0x20000 
SRAM       0x10000000 0x2000 
MAIN_RAM   0x40000000 0x8000000 
CUSTOM_IP  0x30000000 0x1000 
CSR        0xf0000000 0x10000 

litex> mem_read 0x30000000 16 
Memory dump:
0x30000000  00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00  ................

litex> mem_write 0x30000000 0x12345678

litex> mem_read 0x30000000 16         
Memory dump:
0x30000000  78 56 34 12 00 00 00 00 78 56 34 12 01 00 00 00  xV4.....xV4.....

litex> mem_write 0x30000004 0x01020304

litex> mem_read 0x30000000 16         
Memory dump:
0x30000000  78 56 34 12 04 03 02 01 7c 59 36 13 01 00 00 00  xV4.....|Y6.....
``` 

1. We read 16 bytes at the base address: 3 registers are void. However, we have some data at `0x3000000C` (`data=0x00000001`) which is ignored for now as we don't use this address.

2. We write a dummy value for the first register. The result is directly computed.

3. We write a dummy value in the second register. The result is updated as well.