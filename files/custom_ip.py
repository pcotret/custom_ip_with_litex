# Migen/LiteX dependencies
from migen import *
from litex.soc.interconnect.axi import AXILiteInterface

class CustomIP(Module):
    def __init__(self, platform):
        # AXI-Lite interface (32-bit address and data)
        self.bus = axi = AXILiteInterface(address_width=32, data_width=32)

        # 3 internal registers
        self.regs = Array(Signal(32, reset=0) for _ in range(3))

        # AXI-Lite read logic state machine
        read_index = Signal(2)

        fsm = FSM(reset_state="IDLE")
        self.submodules += fsm

        # IDLE state
        fsm.act("IDLE",
            axi.ar.ready.eq(1),
            axi.r.valid.eq(0),
            If(axi.ar.valid,
                NextValue(read_index, axi.ar.addr[2:4]),
                NextState("READ")
            )
        )

        # READ state
        fsm.act("READ",
            axi.ar.ready.eq(0),
            axi.r.valid.eq(1),
            axi.r.resp.eq(0),
            axi.r.data.eq(Mux(read_index == 3, 1, self.regs[read_index])),
            If(axi.r.ready,
                NextState("IDLE")
            )
        )

        # AXI-Lite write logic state machine
        write_index = Signal(2)

        fsm_write = FSM(reset_state="WIDLE")
        self.submodules += fsm_write

        # WIDLE state
        fsm_write.act("WIDLE",
            axi.aw.ready.eq(1),
            axi.w.ready.eq(0),
            axi.b.valid.eq(0),
            If(axi.aw.valid,
                NextValue(write_index, axi.aw.addr[2:4]),
                NextState("WRITE")
            )
        )
        
        # WRITE state
        fsm_write.act("WRITE",
            axi.aw.ready.eq(0),
            axi.w.ready.eq(1),
            axi.b.valid.eq(0),
            If(axi.w.valid,
                If(write_index == 0,
                    NextValue(self.regs[0], axi.w.data)
                ),
                If(write_index == 1,
                    NextValue(self.regs[1], axi.w.data)
                ),
                # No write to the third register as it will contain the result of the custom IP
                NextState("RESP")
            )
        )

        # RESP state
        fsm_write.act("RESP",
            axi.aw.ready.eq(0),
            axi.w.ready.eq(0),
            axi.b.valid.eq(1),
            axi.b.resp.eq(0),
            If(axi.b.ready,
                NextState("WIDLE")
            )
        )

        # Include the Verilog source of the custom IP
        platform.add_source("custom_ip.v")
        
        # Mapping registers to custom IP I/Os
        # i_ and o_ are Migen prefixes needed to identify inputs/outputs
        self.specials += Instance("custom_ip",
            i_a = self.regs[0],
            i_b = self.regs[1],
            o_c = self.regs[2])

