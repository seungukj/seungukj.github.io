---
title: 'Quantitative Baker Theorem and Rational Approximation of logarithms'
date: 2022-10-29
permalink: /posts/2022/10/rational-approx-of-log/
author_profile: false
tags:
  - English
  - Number theory
  - Transcendental number
  - Diophantine approximation
---

This post posts some rational approximation properties of logarithms $\log_pq$, where $p,q$ are multiplicatively independent natural numbers. This will be discussed as an immediate consequence of [quantitative Baker's theorem](https://en.wikipedia.org/wiki/Baker%27s_theorem#Statement).

# Rational Approximations

Given an irrational number $x\in(0,1)$ (or rational numbers with large heights), the quantity $\vert x-\frac{p}q\vert$ (where $\frac{p}q\in\mathbb{Q}$) gains attention in many ways.

For instance, in numerical algorithms, if we want to estimate $x\in(0,1)$ up to $k$ exact digits, having a definite gap between $x$ and its $k$-digit value $\lfloor 10^kx\rfloor/10^k$ helps us to use an approximate $y\approx x$ of $x$. So for instance, if one can ensure that

$$\left\vert 10^k(x - y)\right\vert \ll \left\vert 10^kx-p\right\vert,$$

for any integer $p$, then this tells $\lfloor 10^kx\rfloor=\lfloor 10^ky\rfloor$.

The main tool to study quantities like $\vert x-\frac{p}q\vert$ or $\vert qx-p\vert$ is *convergents* of the continued fraction of $x$.

## Continued Fractions

See [Einsiedler and Ward, 2011](https://link.springer.com/book/10.1007/978-0-85729-021-2) Chapter 3 for details. I post only a brief sketch of the theory.

We first set some notation for a continued fraction (here, $a_0\in\mathbb{Z}$ and $a_1,a_2,a_3,\ldots\in\mathbb{N}:=\mathbb{Z}_{>0}$):

$$x=a_0+\dfrac1{a_1+\dfrac1{a_2+\dfrac1{a_3+\dfrac1\cdots}}} \\
=[a_0;a_1,a_2,a_3,\ldots]\phantom{xxxx} \\
=a_0+\frac1{a_1+}\frac1{a_2+}\frac1{a_3+}\cdots.$$

The last notation, known as a variant of [Pringsheim's notation](https://en.wikipedia.org/wiki/Continued_fraction#Notations), may be useful in the study of convergents. By a *convergent* of a continued fraction $[a_0;a_1,a_2,\ldots]$ we mean the following rational number (with positive denominator and written in the reduced form):

$$\frac{p_n}{q_n}:=[a_0;a_1,a_2,\ldots,a_n].$$

Another way to determine the numbers $(p_n,q_n)$ is to use the following recurrence relation.

$$\begin{bmatrix} p_{-1} & p_{-2} \\ q_{-1} & q_{-2} \end{bmatrix}=\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}; \\ \begin{bmatrix} p_n & p_{n-1} \\ q_n & q_{n-1} \end{bmatrix}=\begin{bmatrix} p_{n-1} & p_{n-2} \\ q_{n-1} & q_{n-2} \end{bmatrix}\begin{bmatrix} a_n & 1 \\ 1 & 0 \end{bmatrix},$$

for $n\geq 0$. The proof of this fact is based on the induction; if one writes $p'/q'=[a_1;a_2,\ldots a_n]$ then

$$\frac{p_n}{q_n} = a_0+\frac{q'}{p'} = \frac{p'a_0+q'}{p'}$$

gives $p_n=p'a_0+q'$, $q_n=p'$, and the matrix formula.

Furthermore, we have

$$\frac{p_n}{q_n} = a_0 + \sum_{k=0}^{n-1}\frac{(-1)^k}{q_kq_{k+1}},$$

and sending $n\to\infty$ we have

$$x=[a_0;a_1,a_2,\ldots]=a_0+\sum_{k=0}^\infty\frac{(-1)^k}{q_kq_{k+1}}.$$

This gives us the estimate

$$\frac{a_{n+2}}{q_{n+2}}<\vert q_nx-p_n\vert<\frac1{q_{n+1}}.$$

 > **Theorem.** Let $x$ be irrational. The convergents $p_n/q_n$ are the best rational approximation of $x$ up to denominator $q_n$, in the following sense. For any $n>1$, $p\in\mathbb{Z}$, and $0<q\leq q_n$, we have
 >
 > $$\vert qx-p \vert < \vert q_nx-p_n\vert,$$
 >
 > unless $p/q=p_n/q_n$.

One can generalize this and think of the [*semiconvergents*](https://en.wikipedia.org/wiki/Continued_fraction#Semiconvergents),

$$\frac{p_{n-2}+sp_{n-1}}{q_{n-2}+sq_{n-1}}$$

where $s=1,2,\ldots,a_n$, a relaxed version of the convergents $p_n/q_n$. Semiconvergents approximate $x$ well too, and satisfies the following. If $p/q$ is a rational number in which $\vert x-\frac{p}q\vert=\min_{\substack{0<q'\leq q \\ p'\in\mathbb{Z}}}\vert x-\frac{p'}{q'}\vert$, then $p/q$ is a semiconvergent. (The converse is not true.)

## Badly approximated numbers

By the general theory of continued fractions, one has the following estimate for any convergent $p_n/q_n$:

$$\left\vert x-\frac{p_n}{q_n}\right\vert < \frac1{q_n^2}.$$

A *badly approximated number* means that $\vert x-\frac{p_n}{q_n}\vert=\Theta(1/q_n^2)$. More precisely, we describe it as follows.

 > **Definition-Proposition.** Let $x=[a_0;a_1,a_2,\ldots]$ be an irrational number. The followings are equivalent.
 >
 > * There exists $M>0$ in which $a_n\leq M$ for all $n\geq 1$.
 > * There exists $\epsilon>0$ in which $\epsilon/q^2\leq\vert x-\frac{p}q\vert$ holds for any rational number $p/q$.
 >
 > <font style="font-style:normal">In that case, we say $x$ is a *badly approximated number*.</font>

Typical examples of badly approximated numbers are quadratic irrational numbers, i.e., numbers of the form $a+b\sqrt{D}$ where $D>0$ is a square-free integer and $a,b$ are rational numbers, $b$ nonzero.

Badly approximated numbers form a measure zero subset of real numbers. One way to see this is to establish some ergodic theory of continued fractions.

 > **Definition.** <font style="font-style:normal">Define $T\colon(0,1)\setminus\mathbb{Q}\to(0,1)\setminus\mathbb{Q}$, $T(x)=\frac1x-\lfloor\frac1x\rfloor$ (the Gauss map). Define a measure $\mu$ on $[0,1]$ as $\mu(dx)=\frac1{\log 2}\frac1{1+x}\, dx$ (the Gauss–Kuzmin measure).</font>

Let $x$ be an irrational number between 0 and 1. Set $a_n(x):=\lfloor 1/T^{n-1}(x)\rfloor$, for $n\geq 1$. Then we have the continued fraction expansion $x=[0;a_1(x),a_2(x),a_3(x),\ldots]$. In fact, we have $T^n(x)=[0;a_{n+1}(x),a_{n+2}(x),\ldots]$.

The map and measure give an ergodic system:

 > **Theorem.** The Gauss map is ergodic with respect to the Gauss–Kuzmin measure.

 > **Corollary.** Badly approximated numbers form a set of zero $\mu$-measure, thus zero Lebesgue measure too.

(Proof of the **Corollary**) Recall that $x$ is a badly approximated number if and only if the sequence $\left(a_n(x)\right)_{n=1}^\infty$ is bounded. This means we have $M\in\mathbb{N}$ in which $a_n(x)\leq M$ holds for all $n$, i.e.,

$$\sum_{n=0}^\infty\mathbb{1}_{[0,1/M]}(T^n(x))=0.$$

By Birkhoff ergodicity, we have a null set $\mathcal{N}\subset(0,1)$ such that every $x\in(0,1)\setminus\mathcal{N}$ has

$$\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}\mathbb{1}_{[0,1/M]}(T^n(x))=\int_0^{1/M}\frac1{\log 2}\frac{dx}{1+x}\\=\log_2\left(1+\frac1M\right).$$

In particular, the set $$\mathcal{B}_M=\{x\in(0,1)\setminus\mathbb{Q} : (\forall n\in\mathbb{N})(a_n(x)\leq M)\}$$ is disjoint from $(0,1)\setminus\mathcal{N}$, thus $$\mathcal{B}_M\subset\mathcal{N}$$. So each $$\mathcal{B}_M$$ has zero volume. Now the set $$\bigcup_{M\in\mathbb{N}}\mathcal{B}_M$$ of all badly approximated numbers also has zero volume, and the claim follows. $//$

## Amortized growth rate of the 'remainder'

Given an irrational $x=[a_0;a_1,a_2,\ldots]>1$ (so we have $a_0=\lfloor x\rfloor\geq 1$), let $x_i$ be the *$i$-th remainder*

$$x_i := [a_i;a_{i+1},a_{i+2},\ldots].$$

Because $x_i\approx a_i$, by a fact in ergodic theory,

$$\lim_{n\to\infty}(a_1a_2\cdots a_n)^{1/n} = \prod_{a=1}^\infty\left(\frac{(a+1)^2}{a(a+2)}\right)^{\log_2a}\approx 2.685$$

for Lebesgue-a.e. $x$, we see that $(x_1x_2\cdots x_n)^{1/n}$ will have a similar limit for a.e. $x$. But an easy estimate applies for all irrational $x>1$:

 > **Theorem.** Let $x>1$ be an irrational and $x_i$ be the $i$-th remainder as above. Then for any $n\geq 1$,
 >
 > $$\frac1n\sum_{i=1}^n\log x_i>\frac12\log 2. \label{eqn:remainder-asymptotic}$$

(Proof) Fix $n\geq 1$, denote $[n]=\{1,\ldots,n\}$, and let $I_n=\{i\in[n] : a_i\geq 2\}$. Then one has $x_i>a_i\geq 2$ if $i\in I_n$.

For $i\notin I_n$, one estimate

$$x_i > [a_i;a_{i+1},a_{i+2}] = 1 + [0;a_{i+1},a_{i+2}],$$

which results, with the concavity of the logarithm,

$$\log x_i > \log(1+[0;a_{i+1},a_{i+2}])>\frac{\log 2}{[0;a_{i+1},a_{i+2}]}\geq\frac{\log 2}{1+a_{i+1}}.$$

Therefore we estimate

$$\frac1n\sum_{i=1}^n\log x_i > \frac1n\sum_{i\in I_n}\log 2 + \frac1n\sum_{i\notin I_n}\frac{\log 2}{1+a_{i+1}} \\
= \log 2\cdot\frac{\vert I_n\vert}{n} + \frac{\log 2}{n}\sum_{i\notin I_n}\frac1{1+a_{i+1}}.$$

To estimate the latter sum, we observe that the number of $i\notin I_n$ such that $i+1\notin I_n$ is at least $n-2\vert I_n\vert$. Thus at least $n-2\vert I_n\vert$ summands in $\sum_{i\notin I_n}1/(1+a_{i+1})$ are $\geq 1/2$, giving us that

$$\frac1n\sum_{i=1}^n\log x_i > \log 2\cdot\frac{\vert I_n\vert}{n} + \frac{\log 2}{n}\cdot\frac12\cdot(n-2\vert I_n\vert) \\=\frac12\log 2.\quad //$$

I am personally curious about whether the bound $\frac12\log 2$ in \eqref{eqn:remainder-asymptotic} is optimal.

# Quantitative Baker's Theorem

Baker's theorem, in the theory of transcendental numbers, reads as follows (cf. [Murty and Rath, 2014](https://link.springer.com/book/10.1007/978-1-4939-0832-5), Chapter 19).

 > **Theorem** (Baker). Let $$\alpha_1,\ldots,\alpha_n\in\overline{\mathbb{Q}}\setminus\{0\}$$ be nonzero algebraic numbers for which $\log\alpha_1,\ldots,\log\alpha_n$ are $\mathbb{Q}$-linearly independent. Then $1,\log\alpha_1,\ldots,\log\alpha_n$ are $\overline{\mathbb{Q}}$-linearly independent as well.

If one is worried about the branches of logarithms, one may set $$\mathbb{L}=\{z\in\mathbb{C} : e^z\in\overline{\mathbb{Q}}\}$$ (instead of $\log\alpha$ with $\alpha\in\overline{\mathbb{Q}}$) and restate the theorem as this: any $\mathbb{Q}$-linearly independent subset of $\mathbb{L}$ is also $\overline{\mathbb{Q}}$-linearly independent.

In Baker's original work, one has the quantitative version of the theorem.

 > **Theorem** ([Baker](https://doi.org/10.1112/S0025579300003843), quantitative). Let $$\alpha_1,\ldots,\alpha_n\in\overline{\mathbb{Q}}\setminus\{0,1\}$$ be algebraic numbers of degrees $\leq d$ and heights $\leq A$. Suppose we fix a branch of $\log$ so that $\log\alpha_1,\ldots\log\alpha_n$ are $\mathbb{Q}$-linearly independent.
 >
 > Let $\beta_0,\ldots,\beta_n\in\overline{\mathbb{Q}}$, not all zeros, be algebraic numbers with degrees $\leq d$ and heights $\leq B$. Then the number
 >
 > $$\Lambda := \beta_0+\beta_1\log\alpha_1+\cdots+\beta_n\log\alpha_n$$
 >
 > has $\vert\Lambda\vert > B^{-C}$, where $C=C(n,d,A,\log)$ is an effectively computable constant.

One significance of the above theorem is that the 'qualitative' version is a quick corollary of the above estimate (and that is how Baker proved his 'qualitative' theorem). But not only that, things get interesting if one gets interested in estimating quantities like $\log_pq$.

## Logarithm

Suppose $p,q\in\mathbb{N}$ are natural numbers that are multiplicatively independent. This means $p,q\neq 1$ and we cannot have $p^kq^\ell=1$ for some $k,\ell\in\mathbb{Z}$, not both zero.

 > <font style="font-style:normal">So for instance, $p=12=2^2\cdot 3$ and $q=18=2\cdot 3^2$ are multiplicatively *independent*, since $p^kq^\ell=1$ entails $2k+\ell=0$ and $k+2\ell=0$, which gives $k=\ell=0$.)</font>

Thus $\log p$ and $\log q$ are $\mathbb{Q}$-linearly independent. Thus for any algebraic numbers $\beta_0,\beta_1,\beta_2$, with height $\leq B$, we have

$$\left\vert\beta_0+\beta_1\log p+\beta_2\log q\right\vert>B^{-C}.$$

In particular, set $\beta_0=0$ and $\beta_1,\beta_2\in\mathbb{Z}$. Then we have

$$\left\vert\beta_1+\beta_2\frac{\log q}{\log p}\right\vert > \frac1{\log p} \frac1{(\vert\beta_1\vert\vee\vert\beta_2\vert)^{C}}.$$

But furthermore, for this particular setup, we have a further explicit bound.

 > **Theorem** ([Baker-Wüstholz 1993](https://doi.org/10.1515/crll.1993.442.19)) Let $\alpha_1,\ldots,\alpha_n$ be as above, with the degree bound $d$ and the height bound $A$. Let $\beta_1,\ldots,\beta_n\in\mathbb{Z}$ be integers, not all zero, whose absolute values are $\leq B$. Then for
 >
 > $$\Lambda := \beta_1\log\alpha_1+\cdots+\beta_n\log\alpha_n,$$
 >
 > we have $\vert\Lambda\vert>\exp(-(16nd)^{2n+4}(\log A)^n\log B)$.

Suppose $q<p$, so that $0<\log_pq<1$. Then for $\alpha,\beta\in\mathbb{Z}$, $0\leq\alpha\leq\beta\neq 0$, we have an inequality

$$\left\vert\beta\log_pq-\alpha\right\vert > \frac1{\log p}\exp(-32^8\cdot(\log p)^2\cdot\log\beta),\label{eqn:log-diophantine-bound}$$

by plugging in $d=1$, $A=p$, and $B=\beta$.

One application of \eqref{eqn:log-diophantine-bound} is to have some diophantine bounds for $\log_{10}2$. So if we put $p=10$ and $q=2$, we have

$$\left\vert\beta\log_{10}2-\alpha\right\vert > \frac1{\log 10}\exp(-32^8(\log 10)^2\cdot\log\beta)>0.4\cdot\beta^{1-\mathrm{6\times 10^{12}}}.$$

(Here, $6\times 10^{12} - 1>32^8(\log 10)^2=5\;829\;498\;621\;754.60\ldots$ and $0.4<1/\log 10=0.43429\ldots$)

## Inverse of a Lie algebra adjoint

Suppose $P_n^2$ is the vector space of a pair of degree $n$ polynomials in 2 variables (over complex numbers). That is, we have $(x_1^2,x_2^2)\in P^2_2$, $(x_1^2x_2-x_1x_2^2,x_1^3)\in P^2_3$, etc.

For any linear map $L\colon\mathbb{C}^2\to\mathbb{C}^2$, one can define a map

$$ \begin{array}{rl}\mathsf{ad}_L=[L,-] \colon P^2_n &\to P^2_n, \\ p &\mapsto L\circ p - p\circ L. \end{array}$$

We see whether this map is invertible, and find some asymptotic bounds of the inverse in $n$.

For sake of simplicity, suppose $L=\mathrm{diag}(\lambda_1,\lambda_2)$. Then the map $[L,-]$ has eigenvectors $x^\alpha\cdot\vec{e}_i$, so that $[L,x^\alpha\cdot\vec{e}_i]=(\lambda_i-\lambda^\alpha)x^\alpha\cdot\vec{e}_i$.

 > <font style="font-style:normal">For instance, set</font>
 >
 > $$L=\begin{bmatrix} 10 & 0 \\ 0 & \frac12 \end{bmatrix}.$$
 > 
 > <font style="font-style:normal">Then elements like $(x_1^2,0),(0,x_1x_2)\in P^2_2$ are eigenvectors (in $P^2_2$) with eigenvalues $10^2-10, 10\cdot\frac12-\frac12$, respectively.</font>

So to speak of the invertibility of $[L,-]$, one needs to estimate how small $\lambda^\alpha-\lambda_i$'s are. For the example $L=\mathrm{diag}(10,\frac12)$ above, this turns the question to ask whether

$$\vert 10^{\alpha_1-1}2^{-\alpha_2}-1\vert\quad\text{ and }\quad\vert 10^{\alpha_1}2^{1-\alpha_2}-1\vert,$$

are large. The above Baker-Wüstholz estimate then establishes that the estimate is $\gtrsim\alpha_2^{-\mathrm{6e12}}$, giving the estimate of the inverse $[L,-]^{-1}\lesssim n^{\mathrm{6e12}}$.

