'''ADC动态性能分析函数
用于计算ADC输出数据的有效位、信噪比、信纳比、SFDR、THD等参数，并显示频谱图
输入参数:
    data: 向量，存储ADC的输出数据，数据量应为FFTtime的整数倍
    fs: 系统采样率，单位: Hz
    FFTtime: 信号做谱平均的次数
    bitnum: ADC的位数
    M: 交替采样通道数
    nyquist_band: 信号所处的奈奎斯特区
输出参数:
    fin: 对波形分析得到的输入信号频率，单位: Hz
    dbamplitude: 信号范围与ADC满量程的比值，用对数表示，单位: dBFS
    FAresult: 列向量。频谱分析得到的结果，包含17个值，分别为:
        FAresult[1] = SNR, 单位: dB
        FAresult[2] = SINAD, 单位: dB
        FAresult[3] = THD, 单位: dBc
        FAresult[4] = SFDR, 单位: dBc
        FAresult[5] = ENOB, 单位: Bit
        FAresult[6] = HD[1], 单位: dBc
        FAresult[7] = HD[2], 单位: dBc
        FAresult[8] = HD[3], 单位: dBc
        FAresult[9] = HD[4], 单位: dBc
        FAresult[10] = HD[5], 单位: dBc
        FAresult[11] = HD[6], 单位: dBc
        FAresult[12] = HD[7], 单位: dBc
        FAresult[13] = HD[8], 单位: dBc
        FAresult[14] = HD[9], 单位: dB
        FAresult[15] = HD[10], 单位: dBc
        FAresult[16] = SNRFS, 单位: dBFS
        FAresult[17] = SFDRFS, 单位: dBFS
'''

#导入python自带库
import sys

#导入python第三方库
import numpy as np
import matplotlib.pyplot as plt

#导入用户自定义库


def data_analysis(data = [0], fs = 1, FFTtime  = 1, bitnum = 10, M = 1, nyquist_band = 1):
    