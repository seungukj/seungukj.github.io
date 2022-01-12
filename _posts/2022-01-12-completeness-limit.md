---
title: 'Dedekind Completeness and Limits'
date: 2022-01-12
permalink: /posts/2022/01/order-completeness-and-limit/
tags:
  - English
  - Calculus
  - Analysis
  - Order Completeness
  - Completeness Axiom
---

## Limit of a Sequence

In the usual calculus materials, the limit of a sequence $$\left(a_n\right)\to L$$ is defined by an analogous definition of the usual "$\epsilon$-$\delta$ definition" of the limit:

\begin{equation}
\label{eqn:def-of-limit}\forall\epsilon>0\exists N\in\mathbb{N}\forall n\geq N;\ \vert a_n-L\vert <\epsilon.
\end{equation}

This itself does not sound that odd as long as one is used to the $\epsilon$-$\delta$ definition of the limit. Following this definition, the limit $L=\lim_{n\to\infty}a_n$ is the "filler" of a logical statement \eqref{eqn:def-of-limit}.

On the other hand, the limit may be understood as a _guess_ from the tendency of the sequence. So for instance, it is not hard to guess that

$$0.1, 0.11, 0.111, 0.1111, \cdots\quad\rightarrow\quad 0.111111\ldots=\frac19.$$

I would say that, this example suggests that finding a limit is an activity associated with our sense of quantities. And, if something is clinged with some 'untold dependency to our sense,' usually this boils down to an __axiom__ that we no longer want to justify further.

## Dedekind Completeness

One of the fundamental properties of the real number is so-called the _completeness axiom_:

 > If a nonempty subset $S\subset\mathbb{R}$ is bounded above, then it has the supremum $\sup S$.
 >
 > (Dual Fact) If a nonempty subset $S\subset\mathbb{R}$ is bounded below, then it has the infimum $\inf S$.

If one allows $\sup S=\infty$ for $S$ unbounded above, and $\inf S=-\infty$ for $S$ unbounded below, then we can restate this axiom as

 > Any nonempty subset $S\subset\mathbb{R}$ of reals has the supremum $\sup S$.
 >
 > (Dual Fact) Any nonempty subset $S\subset\mathbb{R}$ of reals has the infimum $\inf S$.

The fact that this completness is given as an __axiom__, pretty much indicates that _there is no systematic way to find the supremum/infimum of a given set_. (Apparently false, if one believes in the "Dedekind cut" construction of the reals. But I am demanding a method independent to the construction details here.)

More aspects of $\sup S$ and $\inf S$:

 - These quantities are easily understood in the "precalculus-level," where one can sketch the set $S$ on the real line, and 'slide' the upper/lower bounds to reach to the supremum/infimum.
 - If $S$ is given by a monotonic sequence, listing the decimal expressions makes the guess for $\sup S$ or $\inf S$ quite well (as long as we list sufficiently many terms).
 - Let $M<\infty$ (rspt. $m>-\infty$). Proving $M=\sup S$ (rspt. $m=\inf S$) is equivalent to, for any $\epsilon>0$ one has $x\in S$ in which $M\geq x>M-\epsilon$ (rspt. $m\leq x<m+\epsilon$). <br>
 Thus suprema/infima _does_ reflect an infinitesimal phenomena.

Collecting these, it seems like the completeness axiom is (1) associated with our visual understanding of the real line, while (2) very tangent to the infinitesimal, or limiting phenomena as well. Brought from the observations, I claim that the concept of the limit is built based on the completeness axiom!

As a support of the claim, let us see some "formula of limits" written in terms of superma and infima. They are particularily intriguing as they (superficially) excludes the $\epsilon$-$\delta$ or $\epsilon$-$N$ definition of limits.

## From Completeness to Sequence Limits

To state how the limit of a sequence is found, the starting point will be the _monotone convergence theorem_, an equivalent formulation of the completeness axiom above.

 > Any increasing sequence $$\left(a_n\right)$$ has the limit $$\sup a_n$$ (possibly $=\infty$).
 >
 > (Dual Fact) Any decreasing sequence $$\left(a_n\right)$$ has the limit $$\inf a_n$$ (possibly $=-\infty$).

Moreover, there is a generic way to generate an increasing or decreasing sequence, from the given sequence $$\left(a_n\right)$$. Namely,

$$ b_k = \sup_{n\colon n\geq k}a_n, \\ c_k = \inf_{n\colon n\geq k} a_n. $$

(If $$\left(a_n\right)$$ is not bounded, then these sequences may take the values $\pm\infty$. We intentionally allow this.) There, $\left(b_k\right)$ gives a _decreasing_ sequence while $\left(c_k\right)$ gives an _increasing_ sequence, thus should have their respective limits $\inf b_k$ and $\sup c_k$.

These sequences are the ingredients of so-called the _limit supremum_ (limsup) or _limit infimum_ (liminf) of the sequence:

$$\limsup_{n\to\infty}a_n = \inf_{k\geq 1}b_k = \inf_{k\geq 1}\sup_{n\geq k}a_n, \\ \liminf_{n\to\infty}a_n = \sup_{k\geq 1}c_k = \sup_{k\geq 1}\inf_{n\geq k}a_n.$$

These quantities are relevant to the limit, as they are independent with any adjustment of $\left(a_n\right)$ for the first few terms. That is, $\limsup a_n$ and $\liminf a_n$ are "tail" quantities: they are independent to changing a finite number of terms in $a_n$.

If these limsup and liminf coincide, then one can say that the limit $$\lim_{n\to\infty}a_n$$ exists and equals to that coinciding value. The converse is also the case.

 > (Proof) Suppose $$\limsup a_n=\liminf a_n=L$$. If $L=\infty$, then for each $M>0$ we have $$c_N$$ in which $$M<c_N$$. If $n\geq N$ then $$c_N\leq a_n$$ holds, thus $$M<a_n$$ follows. This proves $\lim a_n=\infty$. 
 > 
 > Likewise for $L=-\infty$, but focused on $$\left(b_k\right)$$.
 > 
 > If $L$ is finite, then for any $\epsilon>0$ we have $K,M\in\mathbb{N}$ in which $L-\epsilon<c_M$ and $b_K<L+\epsilon$ holds. Let $N=\max(K,M)$. Then for any $n\geq N$, we have
 >
 > $$L-\epsilon<c_M\leq c_N\leq a_n\leq b_N\leq b_K<L+\epsilon.$$
 > 
 > This verifies that $\vert a_n-L\vert <\epsilon$.
 >
 > Conversely, if $\lim a_n=L$ (with $L$ finite), then for any $\epsilon>0$, one can choose $N\in\mathbb{N}$ in which all $n\geq N$ satisfies $L-\epsilon<a_n<L+\epsilon$. Because of that, we have $L-\epsilon\leq \inf_{n\geq N}a_n=c_N$ and $L+\epsilon\geq\sup_{n\geq N}a_n=b_N$. This entails,
 >
 > $$L-\epsilon\leq c_N\leq\sup c_k=\liminf_{n\to\infty}a_n, \\ L+\epsilon\geq b_N\geq\inf b_k=\limsup_{n\to\infty}a_n.$$
 >
 > That is, $L-\epsilon\leq\liminf a_n\leq\limsup a_n\leq L+\epsilon$ holds for all $\epsilon>0$. The only possible state for this to hold is $\liminf a_n=\limsup a_n=L$.

(Notice that we have used the 'archimedean property,' that the only number $x$ in which $\vert x\vert <\epsilon$ for all $\epsilon>0$ is $x=0$, crucially in the converse. The fact that $\liminf a_n\leq\limsup a_n$ is not heavily hard as long as one gets $c_\ell\leq b_k$ for all $k,\ell\geq 1$.)

Some example demos:

 - If $a_n=(-1)^n/n$, then $b_k=\sup_{n\geq k}a_n=\begin{cases} \frac{1}{k+1} & \text{ if }k\text{ is odd} \\ \frac{1}{k} & \text{ if }k\text{ is even}\end{cases}$, while $c_k=\inf_{n\geq k}a_n=\begin{cases} -\frac{1}{k} & \text{ if }k\text{ is odd} \\ -\frac{1}{k+1} & \text{ if }k\text{ is even}\end{cases}$. <br>
 There one sees that $b_k\colon\frac12,\frac12,\frac14,\frac14,\frac16,\frac16,\cdots$ has infimum 0, while $c_k\colon-1,-\frac13,-\frac13,-\frac15,-\frac15,\cdots$ has supremum 0. This tells $\limsup a_n=\liminf a_n=0$, thus the limit.
 - If $a_n=\frac12(1+(-1)^n)\colon 0,1,0,1,0,1,\cdots$, then $b_k=\sup_{n\geq k}a_n=1$ while $c_k=\inf_{n\geq k}a_n=0$. This evidently tells $\limsup a_n=1\neq 0=\liminf a_n$, thus the limit fails to exist.

## From Completeness to Function Limits

The above limsup and liminf for sequences are somewhat classical topics in analysis. But in fact, one can tweak the definitions and define the following limsup and liminf of functions:

$$\limsup_{x\to a}f(x)=\inf_{\delta>0}\sup\{f(x)\mid 0<\vert x-a\vert <\delta\}, \\
\liminf_{x\to a}f(x)=\sup_{\delta>0}\inf\{f(x)\mid 0<\vert x-a\vert <\delta\}.$$

Again, by the completeness axiom (if we admit $\pm\infty$) the quantities always exist. Note also that these quantities are independent to any tweak of values off from $a$. That is, even if I change values of $f(x)$ on $$\{x\mid\vert x-a\vert >\delta'\}$$, I still have the same $\limsup_{x\to a}f(x)$, etc.

Furthermore, they coincide with the value $L$ iff $\lim_{x\to a}f(x)=L$.

 > (Proof) Suppose $\limsup_{x\to a}f(x)=\liminf_{x\to a}f(x)=L$. If $L$ is finite, then for each $\epsilon>0$ one has $\delta_1,\delta_2>0$ in which,
 >
 > $$ L-\epsilon<\inf\{f(x)\mid 0<\vert x-a\vert <\delta_2\}, \\ \sup\{f(x)\mid 0<\vert x-a\vert <\delta_1\} < L+\epsilon.$$
 > 
 > Set $\delta=\min(\delta_1,\delta_2)$, and let $x$ be any number such that $0<\vert x-a\vert <\delta$. Then we have
 >
 > $$ L-\epsilon < \inf_{0<\vert x-a\vert<\delta_1}f(x) \leq f(x) \leq \sup_{0<\vert x-a\vert<\delta_2} f(x)<L+\epsilon. $$
 >
 > There $\vert f(x)-L\vert <\epsilon$  follows, and by this we check the usual `$\epsilon$-$\delta$ definition.'
 >
 > The cases if $L=\pm\infty$ and the converse will be skipped. (Essentially same as the sequence cases.)

So for $f(x)=\sin(1/x)$ with $x\to 0$, we have, for any $\delta>0$,

$$\sup\{ f(x) \mid 0<\vert x\vert <\delta\}=1, \\ \inf\{f(x)\mid 0<\vert x\vert <\delta\}=-1,$$

thus the $\limsup_{x\to 0}f(x)=1$ and $\liminf_{x\to 0}f(x)=-1$ follows. Other than playing with the negation of $\epsilon$-$\delta$ definition, this check is much more straightforward to deal with!

Another example is $f(x)=x$ with $x\to a$. For any $\delta>0$, we have

$$\sup\{ x \mid 0<\vert x-a\vert<\delta\}=a+\delta, \\ \inf\{x\mid 0<\vert x-a\vert<\delta\}=a-\delta.$$

Hence $\limsup_{x\to a}x=\inf_{\delta>0}(a+\delta)=a$, and likewise $\liminf_{x\to a}x=a$. _Without any fancy $\epsilon$-$\delta$ type arguments_, we thus have proven that $\lim_{x\to a}x=a$ !

## Disclaimer

This is in no sense meant to suggest a replacement definition for the limits. Although the notion of suprema and infima are quite natural in terms of the visual sketches, the "limsup-liminf definition" of limit,

 > We say $\lim_{x\to a}f(x)=L$ if $\limsup_{x\to a}f(x)=\liminf_{x\to a}f(x)=L$.

is (simply) losing too many things:

 - exercising local estimates of the error $\vert f(x)-L\vert$
 - gadgets to prove limit theorems (E.g.: proving $\lim(f(x)\cdot g(x))=\lim f(x)\cdot\lim g(x)$ with the "limsup-liminf definition" is a mess.)
 - generalizations of the concept towards metric or topological spaces (probably the most critical pitfall!)

and many more. This note is more intended to think of, whether formalizing the limit definitions in accordance to the completeness axiom, is giving an easier access to the concept of limits.

#### Update Log
 * <span style="font-size:12px">220112: Created</span>
