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
>     # 3d projections
>     ## parameters
>     a = .8
>     th = 40 # check: https://www.desmos.com/calculator/4awmzytpad
>     ## projection function
>     proj_3d = lambda x,y,z: -x*a*e(th) + y + (0+1j)*z
>     
>     # e.g.: f(e(60)+e(150)) = "(-0.3660,1.3660)"
>     # e.g.: f(proj_3d(1,2,-3)) = "(1.3872,-3.5142)"

#### Update Log
 * <span style="font-size:12px">211109: Created</span>
 * <span style="font-size:12px">220210: added 3D projection module</span>
