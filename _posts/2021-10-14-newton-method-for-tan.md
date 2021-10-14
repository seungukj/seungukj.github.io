---
title: 'Newton's Method for Tangents'
date: 2021-10-14
permalink: /posts/2021/10/newton-method-for-tan/
tags:
  - Calculus
  - Newton's method
  - English
---

## Evaluating Arctangents

What will be the most effective way to evaluate \\(\arctan(x)\\)? There might be some series method,

\\[ \arctan(x) = x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots,\\]

or apply Simpson's method to estimate the integral \\(\int_0^x\frac{dt}{1+t^2}\\). 
However, both ways have relatively slow decrease of errors (around polynomials of \\(n^{-1}\\)),
implying that we need many trials to reduce so. 

Some numerical examples: to evaluate $\arctan(2)$ in degrees, the standard packages result

 * $\arctan(2) = 63.43494882292201^\circ$,
 * Simpson's method with 100 partitions gives $=63.43494882218863^\circ$, and
 * evaluating series for $\arctan(1/2)$ up to $x^{29}$ term gives $=63.43494882222495^\circ$.

So all the methods are decent, but alas, not as good as the Newton's method:

 * Newton's method to solve $\tan x - 2 = 0$ from $x_0=1.5$, after 10 iterates, gives value as accurate as the "standard package" result.

So it seems like Newton's method are single most effective way to deal with this question, modulo accurate computation of sines and cosines. (The method iterates

\\[x_{n+1} = x_n - \cos(x)\cdot\left(\sin(x) - a\cos(x)\right),\\]

to find $\arctan(a)$, thus the dependence.)
