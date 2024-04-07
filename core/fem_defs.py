#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# 			            Базовые константы
###################################################################

# Точность вычислений
eps = 1.0E-10

# Коды направлений вдоль осей координат
DIR_X = 1      # 0000000000000001
DIR_Y = 2      # 0000000000000010
DIR_Z = 4      # 0000000000000100

# Коды начальных условий
INIT_U = 1     # 0000000000000001
INIT_V = 2     # 0000000000000010
INIT_W = 4     # 0000000000000100
INIT_UT = 8    # 0000000000001000
INIT_VT = 16   # 0000000000010000
INIT_WT = 32   # 0000000000100000
INIT_UTT = 64  # 0000000001000000
INIT_VTT = 128 # 0000000010000000
INIT_WTT = 256 # 0000000100000000
