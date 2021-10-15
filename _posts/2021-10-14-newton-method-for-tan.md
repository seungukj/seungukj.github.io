---
title: 'Newton Method for Tangents'
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

 * $\arctan(2) = 63.434948822\underline{92201}^\circ$,
 * Simpson's method with 100 partitions gives $=63.434948822\underline{18863}^\circ$, and
 * evaluating series for $\arctan(1/2)$ up to $x^{29}$ term gives $=63.434948822\underline{22495}^\circ$.

So all the methods are decent, but alas, not as good as the Newton's method:

 * Newton's method to solve $\tan x - 2 = 0$ from $x_0=1.5$, after 10 iterates, gives value as accurate as the "standard package" result.

So it seems like Newton's method are single most effective way to deal with this question, modulo accurate computation of sines and cosines. (The method iterates

\begin{equation}
\label{eqn:iteration-formula}
x_{n+1} = x_n - \cos(x_n)\cdot\left(\sin(x_n) - a\cos(x_n)\right),
\end{equation}

to find $\arctan(a)$, thus the dependence.)

 - By the way, I assume $a>0$ throughout.

## How Tangent behaves, with the Newton's Method

If one looks at the graph of the tangent function, [desmos demo](https://www.desmos.com/calculator/grtzepj49c) 
this graph goes steep as $x$ approaches to $\frac{\pi}2$.

On the other hand, if one starts with $x_0=0$, then one is thrown to $x_1=a$ for the next step; 
it may be away from the ${[}0,\frac{\pi}2)$ window when $a$ is big, thus a `random start' at $[0,\frac{\pi}2)$ does not seem to be an option.

Collecting these observation, we would better start at $x=(\pi/2)-\epsilon$. Is it, really?

## Focus on the Iterates

There is an elementary criterion for convergence of Newton's Method:

\begin{equation}
\left|\frac{f(x)f^{\prime\prime}(x)}{(f'(x))^2}\right|<1,
\end{equation}

on an interval $I$ that contains `the' zero. If we apply $f(x)=\tan x - a$, simplifying, we have

\begin{equation}
\left|2\sin x(\sin x - a\cos x)\right|<1,
\end{equation}

and with some little further manipulation with trigonometric identities, this is equivalent to

\begin{equation}
\label{eqn:elem-newton-bound}
0 < \cos\left(2x-\arctan(a)\right) < \frac{2}{\sqrt{1+a^2}}.
\end{equation}

So as far as $x\approx\arctan(a)$ and \eqref{eqn:elem-newton-bound} is still the case, we have the convergence. 
Nonetheless, \eqref{eqn:elem-newton-bound} fails as $x\to(\frac{\pi}2)-$. What was up there?

## Extra Fixed Point?

Of course \eqref{eqn:iteration-formula} is fixed if $x=\arctan(a)$. However, as observed [in this demo](https://www.desmos.com/calculator/3giqmuazik), the iteration \eqref{eqn:iteration-formula} has two fixed points, $x=\arctan(a)$ and $x=\frac{\pi}{2}$. Thus tentatively, if one starts from $x_0=\pi/2$, they is stuck.

However, it is well-known (see, e.g. [Brin & Stuck](https://doi.org/10.1017/CBO9780511755316), Exercise **1.5.4**) that the iteration

\\[ x_{n+1}=F(x_n) \\]

and a fixed point $p$ on it is **repelling** (i.e., nearby points gets away from $p$) if \\({\mid F'(p)\mid}>1\\), and **attracting** (i.e., nearby points converges to $p$) if \\({\mid F'(p)\mid}<1\\). 

Ah-ha, time to think of the nature of fixed points, then. Following \eqref{eqn:iteration-formula}, put
\begin{equation}
  \label{eqn:iteration-function}
  F(x) := x - \cos x(\sin x - a\cos x).
\end{equation}
Then
\\[ F'(x) = 2\sin x(\sin x - a\cos x),\\]
giving $F'(\arctan(a)) = 0$ and $F'(\frac{\pi}2)=2$. Thus by the forementioned fact, $\arctan(a)$ is attracting (very strongly!), while $\frac{\pi}2$ is repelling.

To see the attracting behavior better, we further compute
\\[ F''(x) = 2(\sin(2x) - a\cos(2x)), \\]
and $F''(\arctan(a)) = 2a$ follows, i.e., $F(x)\approx \arctan(a) + a(x-\arctan(a))^2$ near $x\approx\arctan(a)$. Not only that,
\begin{equation}
\label{eqn:polynomial-estimate-1}
F(x) > \arctan(a) + a(x-\arctan(a))^2 
\end{equation}
may be proven for $\arctan(a)<x<\frac{\pi}2$.

## Failure 1

A corollary to \eqref{eqn:polynomial-estimate-1} is that, once we start $x_0\in(\arctan(a),\frac{\pi}2)$, we always stay in $(\arctan(a),\frac{\pi}2)$. (Thus this interval $I$ is "invariant" in the sense that $F(I)\subset I$, but we hope this to collapse to $\arctan(a)$ as we iterate.)

\eqref{eqn:polynomial-estimate-1} with $x=x_n$ plugged in, gives an interesting fact about the error term $\epsilon_n:=|x_n-\arctan(a)|$:
\\[\epsilon_{n+1}>a\epsilon_n^2.\\]
Some standard techniques regarding recurrence thus applies. For instance, we take $\log$ on each side
\\[\log\epsilon_{n+1} > \log a + 2\log\epsilon_n,\\]
and solve the "recurrence inequality" (or use Gr\"onwall-type inequalities) to find
\begin{equation}
\label{eqn:error-estimate-1}
\epsilon_n > (a\epsilon_0)^{2^n}/a,
\end{equation}
a fact that I did **not** desire of.

### Remnant of the Fire

\erqef{eqn:error-estimate-1} suggests an interesting point, however.

Assume that $\epsilon_n\to 0$ when we start from $x_0\in(\arctan(a),\frac{\pi}2)$. Then by \eqref{eqn:error-estimate-1}, we **cannot** have $a\epsilon_0>1$, so it follows that $x_0-\arctan(a) < 1/a$, whenever $x_0\in(\arctan(a),\frac{\pi}2)$. Sending $x_0\to(\frac{\pi}2)-$,
\begin{equation}
\label{eqn:taylor-arctan-infinity-ineq}
  \frac{\pi}2-\arctan(a) < \frac1a.
\end{equation}

\eqref{eqn:taylor-arctan-infinity-ineq} does match with the Taylor expansion of $\arctan x$ near infinity: [source](https://mathhelpforum.com/threads/taylor-expansion-of-arctan-x-at-infinity.168163/)
\begin{equation}
\label{eqn:taylor-arctan-infinity}
\arctan x = \frac{\pi}2-\frac1x+\frac1{3x^3}-\frac1{5x^5}+\cdots,
\end{equation}
if $x\geq 1$.

## Attempt 2

Prime reason why \eqref{eqn:polynomial-estimate-1} gives a result \eqref{eqn:error-estimate-1} not implying the convergence to nil, is because the inequality is directed to a wrong direction. Thus making some further expansion of $F$ might be the next hope:
\\[ F(\arctan(a) + \epsilon) = \arctan(a) + a\epsilon^2 + \frac1{2!}\epsilon^3 - \frac{a}{3!}\epsilon^4 - \frac1{4!}\epsilon^5 + \frac{a}{5!}\epsilon^6 + \cdots\\]
and we do get
\begin{equation}
\label{eqn:polynomial-estimate-2}
F(\arctan(a)+\epsilon) < \arctan(a) + a\epsilon^2 + \frac12\epsilon^3,
\end{equation}
an inequality that can be proven to be the case for $\arctan(a)+\epsilon\in(\arctan(a),\frac{\pi}2)$.

Setting $x_0\in(\arctan(a),\frac{\pi}2)$, $x_{n+1}=F(x_n)$, and $\epsilon_n = |x_n-\arctan(a)|$, we have
\begin{equation}
\label{eqn:base-error-inequality}
a\epsilon_n^2 < \epsilon_{n+1} < a\epsilon_n^2 + \frac12\epsilon_n^3.
\end{equation}

Some elementary methods tells that \eqref{eqn:taylor-arctan-infinity-ineq} holds for **any** $a>0$. 
Thus $x_n\in(\arctan(a),\frac{\pi}2)$, or equivalently $x_n-\arctan(a)\in(0,\frac{\pi}2-\arctan(a))$, implies $x_n-\arctan(a)\in(0,1/a)$; 
thus $a\epsilon_n=a(x_n-\arctan(a))<1$, for any $n=0,1,2,\ldots$.

Set $\delta_n := a\epsilon_n$, a sequence in $(0,1)$. Then \eqref{eqn:base-error-inequality} turns into,
\begin{equation}
\label{eqn:base-error-inequality-2}
\delta_n^2 < \delta_{n+1} < \delta_n^2 + \frac{1}{2a^2}\delta_n^3.
\end{equation}
As $\delta_n<1$ for all $n\geq 0$, we conclude,
\\[\delta_{n+1} < \left(1+\frac{1}{2a^2}\right)\delta_n^2.\\]
"Solving" this inequality then gives
\\[\delta_n < \left[\left(1+\frac{1}{2a^2}\right)\delta_0\right]^{2^n}\cdot\left(1+\frac{1}{2a^2}\right)^{-1},\\]
a guarantee of $\delta_n\to 0$ if
\begin{equation}
\label{eqn:o(1)-criterion-1}
\delta_0 = a\cdot (x_0 - \arctan(a)) < \left(1+\frac{1}{2a^2}\right)^{-1}.
\end{equation}

Of course the estimate $\delta_n<1$ is rough and we can tighten this bound further, but interpreting \eqref{eqn:o(1)-criterion-1} is still worthwhile to do so.

## A Safe Initial

Suppose $a\geq 1$, and put $x_0 = \frac{\pi}2 - \frac1{2a}$. Then for checking \eqref{eqn:o(1)-criterion-1},
\\[ \left(1+\frac{1}{2a^2}\right)\delta_0 = \left(1 + \frac{1}{2a^2}\right)\cdot a \cdot\left(-\frac{1}{2a}+\frac{\pi}{2}-\arctan(a)\right) \\]
\\[ = \left(1+\frac{1}{2a^2}\right)\cdot a\cdot\left(-\frac{1}{2a}+\frac{1}{a}-\sum_{k\geq 2}\frac{(-1)^k}{2k-1}\frac{1}{a^{2k-1}}\right) \\]
\\[ = \frac12 - \sum_{\substack{\mu=k-1 \\\ k\geq 2}}\frac{(-1)^{\mu+1}}{2\mu+1}\frac{1}{a^{2\mu}} + \frac{1}{4a^2} - \sum_{k\geq 2}\frac{(-1)^k}{2k-1}\frac{1}{2a^{2k}} \\]
\\[ = \frac12 - \frac{1}{12a^2} + \sum_{k\geq 2}(-1)^k\frac{2k-3}{2(2k+1)(2k-1)}\frac{1}{a^{2k}}. \\]
Thus the criterion holds if $\displaystyle\frac12 - \frac{1}{12a^2} + \frac{1}{15a^4}<1$, an inequality that holds whenever $a\geq 1$.

Some extra refined estimate might be in need to guarantee that a $x_0$ closer to $\frac{\pi}2$ should work, but anyways it is good to have
\\[x_0 = \frac{\pi}2 - \frac{1}{2a}\\]
as an explicit, working start to apply the Newton's method \eqref{eqn:iteration-formula} for solving $\tan x = a$.

## In case of a<1

If $a<1$, the matter is much easier; simply put $x_0=0$ and run the algorithm. The first step will result $x_1=a(>\arctan(a))$, and the test \eqref{eqn:o(1)-criterion-1} applies:
\\[ \left(1+\frac{1}{2a^2}\right)\delta_1 = \left(1+\frac{1}{2a^2}\right)\cdot a\cdot (a - \arctan(a)) \\]
\\[ = \left(1 + \frac{1}{2a^2}\right) \cdot a \cdot \left(\frac{a^3}{3} - \frac{a^5}{5} + \cdots \right) \\]
\\[ < \left(1 + \frac{1}{2a^2}\right) \frac{a^4}{3} = \frac{a^4}{3} + \frac{a^2}{6} < \frac13 + \frac16 = \frac12. \\]
So we know even better: $\delta_n=O(2^{-2^n})$.


#### Update Log
 * <span style="font-size:12px">211014: Created</span>
 * <span style="font-size:12px">211014: Wrestling with `align` that ignores newlines. Any resolutions?</span>
