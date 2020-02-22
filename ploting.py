import matplotlib.pyplot as plt
import numpy as np
import struct

file1 = open('c:\\temp\\outfd_f0_imag.floats', 'rb')
file2 = open('c:\\temp\\outfd_f0_imag_gpu.floats', 'rb')
# file1 = open('c:\\temp\\results_0_0_3.floats', 'rb')
# file2 = open('c:\\recordings\\xcorrGetSummary_1_2_3_summary.floats', 'rb')
buffer = file1.read()
buffer2 = file2.read()

print(len(buffer2))

fa = struct.unpack('{:.0f}f'.format(len(buffer)/4), buffer)
fa2 = struct.unpack('{:.0f}f'.format(len(buffer2)/4), buffer2)

# print(fa)
# print(fa2)

plt.figure(1)
plt.plot(range(len(fa[5:])), fa[5:], '+')
plt.plot(range(len(fa2[5:])), fa2[5:], '-')
plt.show()

file1.close()
file2.close()