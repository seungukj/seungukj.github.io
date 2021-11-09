---
title: 'Some Code Fragments'
date: 2021-11-09
permalink: /posts/2021/11/tikz-code-frag/
tags:
  - English
  - Python
  - Graphics
---

This is to record some Python macro that I have used to draw some TikZ figures:

>     import numpy as np
>     
>     e = lambda x: np.exp(x * (0+1j) * np.pi/180)
>     f = lambda n: "({a:.4f},{b:.4f})".format(a=n.real,b=n.imag)
>     
>     # e.g.: f(e(60)+e(150)) = "(-0.3660,1.3660)"

#### Update Log
 * <span style="font-size:12px">211109: Created</span>
