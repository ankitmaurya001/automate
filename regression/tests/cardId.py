#!/usr/bin/env python


def silly():
	from ..utils.test import testme
	from ..utils.vxPython import vxConsole
	print testme("sara")
   	t = vxConsole("10.64.106.50",2003)
	return t.cmd("mManufDisplay")
if __name__ == "__main__":
	print silly()