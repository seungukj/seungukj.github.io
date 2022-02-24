---
title: 'Tikz-Test'
date: 2022-02-24
permalink: /posts/2022/02/tikz-test-page/
tags:
  - Test
---

```latex {cmd=true hide=true}
\documentclass{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
\draw[->] (0,0)--(2.5,0) node[right] {$\theta$};
\draw[->] (0,-1.5)--(0,1.5) node[left] {$\cos\theta$};
\draw[blue,thick] (0,1) cos (1,0) sin (2,-1);
\draw[dashed] (2,-1)--(2,0) node[above] {$\pi$};
\node[below right] at (0,0) {0};
\end{tikzpicture}
\end{document}
```

#### Update Log
 * <span style="font-size:12px">220224: Created</span>
