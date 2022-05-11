import os
import ipywidgets as widgets
from IPython.display import IFrame

out0 = widgets.Output()
out1 = widgets.Output()
out2 = widgets.Output()
out3 = widgets.Output()
out4 = widgets.Output()


tab = widgets.Tab(children = [out0, out1, out2, out3, out4])
tab.set_title(0, 'CPU')
tab.set_title(1, 'GPU USM')
tab.set_title(2, 'GPU USM hotspots')
tab.set_title(3, 'GPU Repeat')
tab.set_title(4, 'GPU hotspots Repeat')

display(tab)

with out0:
    display(IFrame(src='reports/bl_cpu.html', width=1024, height=768))
with out1:
    display(IFrame(src='reports/bl_usm_output.html', width=1024, height=768))
with out2:
    display(IFrame(src='reports/bl_usm_hotspots_output.html', width=1024, height=768))
with out3:
    display(IFrame(src='reports/output_repeat5.html', width=1024, height=768))
with out4:
    display(IFrame(src='reports/output_hotspots_repeat5.html', width=1024, height=768))
    
    