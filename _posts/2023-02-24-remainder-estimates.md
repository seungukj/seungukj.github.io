---
title: 'Amortized Multiplicative Estimates of Remainders of Continued Fractions'
date: 2023-02-24
permalink: /posts/2023/02/remainder-estimates/
author_profile: false
tags:
  - English
  - Continued Fractions
  - Analysis
---

<b id="thm:main">Theorem.</b> For any irrational $\alpha>1$ whose continued fraction is $\alpha=[a_0;a_1,a_2,\ldots]$, the *remainders* $\alpha_i=[a_i;a_{i+1},a_{i+2},\ldots]$ have an amortized estimate

$$(\alpha_1\cdots\alpha_n)^{1/n} > \sqrt{2}.$$

# Continued Fractions

Recall that a *continued fraction* is an infinite fractional expression

$$x=a_0+\dfrac1{a_1+\dfrac1{a_2+\dfrac1{\ddots+\dfrac1{a_n+\cdots}}}},$$

where typically one sets $a_0,a_1,a_2,\cdots$ to be integers, especially that $a_i>0$ for $i>0$. Some notations like

$$x=a_0+\frac1{a_1+}\frac1{a_2+}\cdots\frac1{a_n+}\cdots \\
=[a_0;a_1,a_2,\cdots,a_n,\cdots]$$

are used to write the fraction in a more compact form.

## Convergents

Continued fractions, if it terminates in finitely many steps, represent rational numbers, or if it does not terminate, represent irrational numbers. For the latter, if one truncates the fraction with finitely many steps, one obtains the *convergent* of the continued fraction.

A formula to find the convergent is as follows. Define the matrix

$$\begin{bmatrix} p_{-1} & q_{-1} \\ p_{-2} & q_{-2} \end{bmatrix}=\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}.$$

For general matrices $\begin{bmatrix} p_n & q_n \\ p_{n-1} & q_{n-1} \end{bmatrix}$, we update this matrix according to the recurrence

$$\begin{bmatrix} p_n & q_n \\ p_{n-1} & q_{n-1} \end{bmatrix} = \begin{bmatrix} a_n & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} p_{n-1} & q_{n-1} \\ p_{n-2} & q_{n-2} \end{bmatrix}, \label{eqn:recurrence}$$

for $n\geq 0$. For the sequence of matrix determined this way, the fraction $p_n/q_n$ is called the *$n$-th convergent* of the continued fraction $[a_0;a_1,a_2,a_3,\ldots]$. That is,

$$\frac{p_n}{q_n} = a_0 + \frac1{a_1+}\frac1{a_2+}\cdots\frac1{a_{n-1}+}\frac1{a_n}.$$

## Derivation of \eqref{eqn:recurrence}

One way to derive the recurrence \eqref{eqn:recurrence} is to consider the Möbius transforms

$$T_n\colon z\mapsto a_n+\frac1z,$$

and think that the n-th convergent is same as $T_0T_1\cdots T_n(\infty)$. So letting $p_n/q_n=[a_0;a_1,a_2,\ldots,a_n]$, we have

$$\begin{bmatrix} p_n \\ q_n \end{bmatrix} = c_n\cdot\begin{bmatrix} a_0 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} a_1 & 1 \\ 1 & 0 \end{bmatrix}\cdots\begin{bmatrix} a_n & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix},$$

for some number $c_n\neq 0$. We may set this $c_n=1$, if we allow $p_n,q_n$ to be rational numbers. (They will be shown to be integers later.) A similar construction $T_0T_1\cdots T_{n-1}T_n(0)$ gives the $(n-1)$-th convergent, because $T_n(0)=\infty$. Hence

$$\begin{bmatrix} p_{n-1} \\ q_{n-1} \end{bmatrix} = \begin{bmatrix} a_0 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} a_1 & 1 \\ 1 & 0 \end{bmatrix}\cdots\begin{bmatrix} a_n & 1 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix}.$$

In particular, one has

$$\begin{bmatrix} p_n & p_{n-1} \\ q_n & q_{n-1} \end{bmatrix}=\begin{bmatrix} a_0 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} a_1 & 1 \\ 1 & 0 \end{bmatrix}\cdots\begin{bmatrix} a_n & 1 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \label{eqn:recurrence-1}$$

and because the matrix on the right is an integer matrix, we see that $p_n,q_n$ are integers also. Transposing \eqref{eqn:recurrence-1} gives the recurrence \eqref{eqn:recurrence}.

This idea of using Möbius transforms can be applied to find convergents of more general fractions

$$x=a_0+\dfrac{b_1}{a_1+\dfrac{b_2}{a_2+\dfrac{b_3}{a_3+\cdots}}}.$$

This time, one uses the transforms

$$S_n(z)=\frac{b_n}{a_n+z},$$

and consider $a_0+S_1S_2\cdots S_n(0)$ for the n-th convergent $r_n/s_n$. For a moment set $a_0=0$. Then we have

$$\begin{bmatrix} r_n & r_{n-1} \\ s_n & s_{n-1} \end{bmatrix}=\begin{bmatrix} 0 & b_1 \\ 1 & a_1 \end{bmatrix}\cdots\begin{bmatrix} 0 & b_n \\ 1 & a_n \end{bmatrix}\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix},$$

which, by transposing, gives

$$\begin{bmatrix} r_n & s_n \\ r_{n-1} & s_{n-1} \end{bmatrix}=\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} 0 & 1 \\ b_n & a_n \end{bmatrix}\cdots\begin{bmatrix} 0 & 1 \\ b_1 & a_1 \end{bmatrix} \\
= \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} 0 & 1 \\ b_n & a_n \end{bmatrix}\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} r_{n-1} & s_{n-1} \\ r_{n-2} & s_{n-2} \end{bmatrix} \\
= \begin{bmatrix} a_n & b_n \\ 1 & 0 \end{bmatrix}\begin{bmatrix} r_{n-1} & s_{n-1} \\ r_{n-2} & s_{n-2} \end{bmatrix},$$

generalizing \eqref{eqn:recurrence}.

# Euclidean Algorithm

Consider the following dynamics on the 1st quadrant of the plane. Given $(x,y)\in\mathbb{R}^2$, $x,y\geq 0$, define

$$f(x,y) = \begin{cases} (x-y,y) & (\text{if }\ y<x), \\ (x,-x+y) & (\text{if }\ y\geq x). \end{cases}$$

If $x,y$ are $\mathbb{Q}$-linearly dependent, i.e., either $x=0$ or $y/x\in\mathbb{Q}$, then "iterate $f$" is a way to describe the [Euclidean gcd algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm). Hence for such initial points, by a finitely many iterates of $f$ one reaches to a point on the x-axis or the y-axis. Because $f(0,y)=(0,y)$ and $f(x,0)=(x,0)$, the behavior of further iterates is clear.

If $x,y$ are $\mathbb{Q}$-linearly independent, we claim the following.

 > <b id="thm:superficial">Theorem.</b> If $x,y>0$ have $y/x\notin\mathbb{Q}$, then $f^k(x,y)\to(0,0)$ as $k\to\infty$.

## Strategy for convergence

To show [this](#thm:superficial), we consider an alternative coordinates of the 1st quadrant, which is essentially the polar coordinates. But instead of the Euclidean norm and the angle, we consider the [taxicab norm](https://en.wikipedia.org/wiki/Taxicab_geometry) (i.e., $\ell^1$-norm) and the slope for respective alternatives.

For a point $(x,y)\in\mathbb{R}^2$ in the 1st quadrant, define the variables $\gamma=x+y$ and $m=y/x$ [if $x=0$, set $m=\infty$]. The coordinate $[m,\gamma]$ then recovers the original point by $(x,y)=(\frac1{1+m}\gamma,\frac{m}{1+m}\gamma)$. Furthermore, the map $f$ acts on the coordinates in the following way.

$$f[m,\gamma]=\begin{cases} \left[\dfrac{m}{1-m},\dfrac1{1+m}\gamma\right] & (\text{if }\ m<1), \\ \left[m-1,\dfrac{m}{1+m}\gamma\right] & (\text{if }\ m\geq 1). \end{cases}$$

Define the functions

$$\phi(m)=\begin{cases} m/(1-m) & (\text{if }\ m<1), \\ m-1 & (\text{if }\ m\geq 1), \end{cases} \\
\rho(m)=\begin{cases} 1/(1+m) & (\text{if }\ m<1), \\ m/(1+m) & (\text{if }\ m\geq 1). \end{cases}$$

Then it follows that $f[m,\gamma]=[\phi(m),\rho(m)\gamma]$. Since $\rho(m)\leq 1$ unless $m=0,\infty$, iterating $f$ makes $\gamma$ to decrease. Thus the theorem $f^k(x,y)\to(0,0)$ reduces to this. If $m$ is irrational then

$$\prod_{j=0}^{k-1}\rho(\phi^j(m))\to 0.$$

To show this, notice that one has $\rho(m)\leq 1$ whenever $m\in[0,\infty]$, but also $\rho(m)\leq\frac23$ if $m\in[\frac12,2]$. If one tracks the $\phi$-orbit of $m=[a_0;a_1,a_2,\ldots]$, one sees that numbers of the form $[1;a_i,a_{i+1},\ldots]$ or $[0;1,a_j,a_{j+1},\ldots]$ occur infinitely often; one can even show that

$$\phi^{a_0+a_1+\cdots+a_i-1}(m)=\begin{cases} [1;a_{i+1},a_{i+2},\ldots] & (\text{if $i$ is even}), \\ [0;1,a_{i+1},a_{i+2},\ldots] & (\text{if $i$ is odd}). \end{cases}\label{eqn:sweet-orbit}$$

Infinite continued fractions of the form $[1;a_j,a_{j+1},\ldots]$ are precisely the irrational numbers in the interval $[1,2]$, and infinite continued fractions of the form $[0;1,a_i,a_{i+1},\ldots]$ are precisely the irrational numbers in the interval $[\frac12,1]$. Hence we have the estimate

$$\prod_{j=0}^{a_0+\cdots+a_n}\rho(\phi^j(m))\leq\left(\frac23\right)^n,$$

and thus the convergence.

## An old attempt

When I happened to front the map $f$ first time, for some reason I happened to consider $c=\min(x,y)$ in place of $\gamma$, which required some extra work to show the convergence to the origin. [One can show that $c\to 0$ through the iterates, but the locus $c=0$ is the union of $x$ and $y$-axes.]

Nonetheless, the update pattern of $c$ under $f$ is quite interesting. For $(x',y')=f(x,y)$, $c=\min(x,y)$, and $c'=\min(x',y')$, one can show that

$$c'=\begin{cases} \min(m^{-1}-1,1)\cdot c & (\text{if }\ m<1), \\ \min(m-1,1)\cdot c & (\text{if }\ m\geq 1). \end{cases}$$

Defining

$$\mu(m)=\begin{cases} \min(m^{-1}-1,1) & (\text{if }\ m<1), \\ \min(m-1,1) & (\text{if }\ m\geq 1), \end{cases}$$

we have $\mu(m)=1$ if $m\notin(\frac12,2)$, $\mu(m)=m^{-1}-1$ if $m\in[\frac12,1]$, and $\mu(m)=m-1$ if $m\in[1,2]$. Notice that $\mu(1)=0$ and $\mu$ is continuous; so on the `sweet interval' $[\frac12,1]$, the multiplier gets quite small.

Regarding \eqref{eqn:sweet-orbit}, we see that for $m=[a_0;a_1,a_2,\ldots]$,

$$\mu(\phi^{a_0+a_1+\cdots+a_i-1}(m))=[0;a_{i+1},a_{i+2},\ldots],$$

so to study the asymptotics of the Birkhoff product $\prod_{j=0}^{k-1}\mu(\phi^j(m))$, some knowledge on products of the "remainder" fractions

$$m_i=[0;a_{i+1},a_{i+2},\ldots]$$

will be useful; even, the Birkhoff product will be bounded above by (in fact, equals to) $m_1\cdots m_j$ if $k\geq\sum_{i=0}^ja_i$. By the [theorem](#thm:main) at the top, we have $m_1\cdots m_j\leq 2^{-j/2}$ and hence we have $\min(x_k,y_k)\to 0$, for $(x_k,y_k)=f^k(x,y)$.

# Proof of the [Theorem](#thm:main)

Recall the irrational number $\alpha=[a_0;a_1,a_2,\ldots]>1$ and the remainder fractions $\alpha_i=[a_i;a_{i+1},a_{i+2},\ldots]$.

Fix $n\geq 1$, and let $$I_n = \{i\in\{1,\ldots,n\} : a_i\geq 2\}$$. Then we have $\alpha_i>a_i\geq 2$ if $i\in I_n$. 

For $i\notin I_n$, we estimate

$$\alpha_i > a_i + \frac1{a_{i+1}+\dfrac{1}{a_{i+2}}} = 1 + \frac{1}{a_{i+1}+\dfrac{1}{a_{i+2}}},$$

which results

$$\log\alpha_i > \log\left(1 + \frac{1}{a_{i+1}+\dfrac{1}{a_{i+2}}}\right)>\frac{\log 2}{a_{i+1}+\dfrac{1}{a_{i+2}}}\geq\frac{\log 2}{1+a_{i+1}},$$

where the second inequality follows from the concavity of the $\log$ on $[1,2]$. Summing up these contributions, we conclude

$$
    \frac1n\sum_{i=1}^n\log\alpha_i > \frac1n\sum_{i\in I_n}\log 2 + \frac1n\sum_{i\notin I_n}\frac{\log 2}{1+a_{i+1}} \\
    = \log 2\cdot\frac{|I_n|}{n} + \frac{\log 2}{n}\sum_{i\notin I_n}\frac{1}{1+a_{i+1}}.
$$

Now the number of $i\notin I_n$'s that has $i+1\notin I_n$ is at least $n-2\vert I_n\vert$; if we think the complement of such $i$'s in $$[n]=\{1,\ldots,n\}$$, it is $I_n\cup(I_n-1)$ which has at most $2\vert I_n\vert$ elements. Thus at least $n-2\vert I_n\vert$ summands in $\sum_{i\notin I_n}1/(1+a_{i+1})$ are $1/2$, which gives us the estimate

$$\frac1n\sum_{i=1}^n\log\alpha_i > \log 2\cdot\frac{|I_n|}{n} + \frac{\log 2}{n}\cdot\frac12\cdot(n-2|I_n|) = \frac{\log 2}{2}.\quad\square$$

## Notes

Initially, I thought that the geometric average $(\alpha_1\cdots\alpha_n)^{1/n}$ may stay close to 1, so I tried to collect reasons that will avoid the product to be close to 1.

The cheapest cause came from $\alpha_i>a_i$. So if $a_i\geq 2$ for sufficiently many $i$'s, then this would avoid the product to be close to 1. But then the worst opposite to it, the golden ratio $[1;1,1,1,\ldots]=(1+\sqrt{5})/2$, should give us the worst possible behavior for $(\alpha_1\cdots\alpha_n)^{1/n}$. Still, we are away from 1 in this 'proposed worst case.'

Rather, golden ratio is another good example, because $\alpha_i$'s are not that close to 1. Thus the 'true' worst case should appear with a remainder $\alpha_i=[1;M,\ast,\ast,\ldots]$, where $M$ is a big number to keep $\alpha_i\approx 1$; but then $\alpha_{i+1}\geq M$ gives us a big product at the next step. As all potential worst cases were contributing to keep the average $(\alpha_1\cdots\alpha_n)^{1/n}$ away from 1, we guess that the product really stays away from 1.

Surprisingly, the gap from 1 was found to be $\sqrt{2}$, independent with $\alpha$. Furthermore, we might have some room to have a number better than $\sqrt{2}$. So we ask:

 > **Question.** What is the infimum of the following limit infima
 >
 > $$\liminf_{n\to\infty}(\alpha_1\cdots\alpha_n)^{1/n},$$
 >
 > among all irrational numbers greater than 1?

(Obviously, the infimum in question should be lower than the golden ratio. So somewhere in $[\sqrt{2},(1+\sqrt{5})/2]$ we should have the answer.)

Note that the bound $\sqrt{2}$ is quite smaller than the 'typical asymptotics.' For (Lebesgue-)almost every $\alpha$, we have

$$\lim_{n\to\infty}(a_1\cdots a_n)^{1/n} = K_0,$$

where $K_0\approx 2.685$ is the [Khinchin's constant](https://en.wikipedia.org/wiki/Khinchin%27s_constant). Hence one has $\liminf (\alpha_1\cdots\alpha_n)^{1/n}\geq K_0$, for almost every $\alpha$.

#### Update Log
 * <span style="font-size:12px">230224: Created</span>
