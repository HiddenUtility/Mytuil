#!/usr/bin/python
# -*- coding: utf-8 -*-
"""__init__.py
Explain : プロット系ひな形サンプル
          
Create  : 2024-06-20(木): H.U
          
Todo    : 
          
"""
#// matplotutil
from plotutil.matplot.single_axis_mat_plot_maker import SingleAxisMatPlotMaker
#// plotry 
from plotutil.plotly.single_axis_plotly_plot_maker import SingleAxisPlotlyPlotMaker

__copyright__    = 'Copyright(C) 2024 Hiroki Uchimura'
__version__      = '1000'
__license__      = 'BSD-3-Clause'
__author__       = 'HiddenUtility'
__author_email__ = 'i.will.be.able.to.see.you@gmail.com'
__url__          = 'https://github.com/HiddenUtility/pyutil'
__all__ = [
    'SingleAxisMatPlotMaker',
    'SingleAxisPlotlyPlotMaker',
]