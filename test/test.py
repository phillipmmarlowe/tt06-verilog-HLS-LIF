import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles



@cocotb.test()
async def test_lfi(dut):
    CURRENT = 200

    dut._log.info("starting simulation")
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    # reset
    dut._log.info("reset")
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1
    # shouldn't be needed
    #dut.ena.value = 1
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 10)
    dut.ui_in.value = CURRENT
    for i in range(100):
        if (i%2 == 0):
            dut.ui_in.value = 125
        else:
            dut.ui_in.value = CURRENT
        await ClockCycles(dut.clk, 10)
    dut._log.info("test done")



'''
    # the compare value is shifted 10 bits inside the design to allow slower counting
    max_count = dut.ui_in.value << 10
    dut._log.info(f"check all segments with MAX_COUNT set to {max_count}")
    # check all segments and roll over
    for i in range(15):
        dut._log.info("check segment {}".format(i))
        await ClockCycles(dut.clk, max_count)
        assert int(dut.segments.value) == segments[i % 10]

        # all bidirectionals are set to output
        assert dut.uio_oe == 0xFF

    # reset
    dut.rst_n.value = 0
    # set a different compare value
    dut.ui_in.value = 3
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    max_count = dut.ui_in.value << 10
    dut._log.info(f"check all segments with MAX_COUNT set to {max_count}")
    # check all segments and roll over
    for i in range(15):
        dut._log.info("check segment {}".format(i))
        await ClockCycles(dut.clk, max_count)
        assert int(dut.segments.value) == segments[i % 10]
'''
