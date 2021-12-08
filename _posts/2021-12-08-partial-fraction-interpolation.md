---
title: 'Partial Fractions and Interpolations'
date: 2021-12-08
permalink: /posts/2021/12/partial-fraction-interpolation/
tags:
  - English
  - Calculus
  - Partial Fractions
  - Lagrange Polynomials
---

## Partial Fraction Decompositions

Evaluating partial fraction decomposition _is_ a tedious job. For instance, making partial fractions of $x/((x+1)(x+2)(x+3))$ first demands to set up

$$\frac{x}{(x+1)(x+2)(x+3)}=\frac{A}{x+1}+\frac{B}{x+2}+\frac{C}{x+3},$$

and make a common denominator and compare the numerators:

\begin{equation}
\label{eqn:PFD-eg}
x = A(x+2)(x+3) + B(x+1)(x+3) + C(x+1)(x+2).
\end{equation}

However, for simple denominators (i.e., denominators without multiple factors), this task can be detoured using [Lagrange Interpolationg Polynomials](https://en.wikipedia.org/wiki/Lagrange_polynomial).

## Lagrange Interpolation Polynoimals

The [Wikipedia link](https://en.wikipedia.org/wiki/Lagrange_polynomial) serves the most general definition of such polynomials, which are not hard to understand through. Thus at this post, we will specifically deal with an example set, $\{x_1=-1,x_2=-2,x_3=-3\}$.

Think of a polynomial $P(x)$ that has degree $\leq 2$. Then this $P(x)$ is found by the following formula:

\begin{equation}
\label{eqn:LIP-elem}
P(x) = P(-1)\frac{(x+2)(x+3)}{(-1+2)(-1+3)}+P(-2)\frac{(x+1)(x+3)}{(-2+1)(-2+3)} + P(-3)\frac{(x+1)(x+2)}{(-3+1)(-3+2)}.
\end{equation}

In particular, say if $P(x)=\ell_{x_1}(x)$ has $\ell_{x_1}(-1)=1$ while $\ell_{x_1}(-2)=\ell_{x_1}(-3)=0$, we have

$$\ell_{x_1}(x)=\frac{(x+2)(x+3)}{(-1+2)(-1+3)},$$

which consists of
 
 * the numerator $(x+2)(x+3)$ multiplying all $(x-x_j)$'s except $(x-x_1)$,
 * the denominator $(-1+2)(-1+3)$ that evaluates the numerator at $x=x_1$.

The other two polynomials $\ell_{x_2}(x)$ and $\ell_{x_3}(x)$ are formed with the similar spirit, each respectively designed to have

 - degree $\leq 2$, and
 - $\ell_{x_i}(x_j)=\delta_{ij}$ (i.e., $=1$ if $i=j$ and $=0$ if $i\neq j$).

By this we have

\begin{equation}
\label{eqn:LIP-abs}
P(x) = P(x_1)\cdot \ell_{x_1}(x) + P(x_2)\cdot \ell_{x_2}(x)+ P(x_3)\cdot \ell_{x_3}(x).
\end{equation}

The polynomials $\ell_{x_1}(x),\ell_{x_2}(x),\ell_{x_3}(x)$ are called _Lagrange Interpolation Polynomials_. It really depends on the _interpolationg points' set_ $\{x_1,x_2,x_3\}$, but we only noted a point for the notational convenience.

### Application to Partial Fractions

Having this idea, we apply \eqref{eqn:LIP-abs} as follows.

$$x = (-1)\cdot \ell_{-1}(x) + (-2)\cdot \ell_{-2}(x) + (-3)\cdot \ell_{-3}(x).$$

That is,

$$x = -\frac{(x+2)(x+3)}{(-1+2)(-1+3)} - 2\frac{(x+1)(x+3)}{(-2+1)(-2+3)} - 3\frac{(x+1)(x+2)}{(-3+1)(-3+2)},$$
$$\therefore x = -\frac12(x+2)(x+3) + 2(x+1)(x+3) -\frac32(x+1)(x+2).$$

Compare this with \eqref{eqn:PDF-eg}:

$$x=A(x+2)(x+3) + B(x+1)(x+3)+C(x+1)(x+2).$$

This thus tells that $A=-\frac12$, $B=2$, and $C=-\frac32$ should be the case. No equation solving, but obtained all with some magic polynomials!

## More Decompositions

The underlying theory is just it. Given a partial fraction decomposition problem, interpret this with Lagrange interpolations, and match the corresponding coefficients.

However this only apparently applies to the denominators of the sort

$$\frac{x^2+2x-1}{x(x-1)(x+1)},$$

i.e., with real and distinct roots, and apparently does not apply for the denominators like

$$\frac{v^2-v}{(1+v)(1+v^2)},\quad \frac{t+1}{t^2(t-1)},$$

i.e., ones with imaginary roots, or ones with repeating roots.

### Imaginary Roots

The Lagrange interpolation polynomials are _not_ limited to reals, and rather it applies for any field (structure with (commutative) addition, multiplication, and division).

Hence for say $\{-1,i,-i\}$, we still have the formula

$$P(x)=P(-1)\cdot \ell_{-1}(x)+P(i)\cdot \ell_i(x)+P(-i)\cdot \ell_{-i}(x),$$

for a polynomial with degree $\leq 2$. It is just the complex number intervening in the computations. Since

$$\ell_{-1}(x)=\frac{(x+i)(x-i)}{(-1+i)(-1-i)}=\frac12(x^2+1),$$
$$\ell_i(x)=\frac{(x+1)(x+i)}{(i+1)(i+i)}=-\frac{1+i}{4}(x+1)(x+i),$$
$$\ell_{-i}(x)=\frac{(x+1)(x-i)}{(-i+1)(-i-i)}=-\frac{1-i}{4}(x+1)(x-i),$$

for say $P(x)=x^2-x$, we have

$$x^2-x=2\cdot\ell_{-1}(x)-(1+i)\cdot\ell_i(x)-(1-i)\ell_{-i}(x),$$

which cleans up to

$$x^2-x=(x^2+1)+\frac{i}{2}(x+1)(x+i)-\frac{i}{2}(x+1)(x-i)$$
$$=(x^2+1)+(x+1)\left[\frac{i}{2}(x+i)-\frac{i}{2}(x-i)\right]$$
$$=(x^2+1)-(x+1),$$

so dividing out $(x+1)(x^2+1)$, we have

$$\frac{x^2-x}{(x+1)(x^2+1)}=\frac{1}{x+1}-\frac{1}{x^2+1}.$$

### Multiple Roots

Algebraically, this one is more tricky. One way is to iterate the partial fraction decompositions:

$$\frac{t+1}{t^2(t-1)}=\frac1t\left[\frac{t+1}{t(t-1)}\right]$$
$$=\frac{1}{t}\left[-\frac{1}{t}+\frac{2}{t-1}\right]$$
$$=-\frac1{t^2}+\frac{2}{t(t-1)}$$
$$=-\frac1{t^2}-\frac{2}{t}+\frac{2}{t-1}.$$

Another is to "split" the roots of the denominator $t^2(t-1)$, to say $\{0,\epsilon,1\}$ (where $\epsilon$ is an infinitesimal). In that case we have the interpolation polynomials

$$\ell_0(t)=\frac{(t-\epsilon)(t-1)}{\epsilon},$$
$$\ell_\epsilon(x)=\frac{t(t-1)}{-\epsilon(1-\epsilon)},$$
$$\ell_1(x)=\frac{t(t-\epsilon)}{1-\epsilon}.$$

Furthermore,

$$t+1=1\cdot\ell_0(t)+(1+\epsilon)\cdot\ell_\epsilon(x)+2\cdot\ell_1(x),$$

and cleaning up the formula we obtain,

$$t+1=\frac{1}{\epsilon}(t-\epsilon)(t-1)-\frac{1+\epsilon}{\epsilon(1-\epsilon)}t(t-1)+\frac{2}{1-\epsilon}t(t-\epsilon).$$

Clearly the first two terms will be problematic if we let $\epsilon\to 0$. How to remedy this? Probably doing more algebra _for the first two terms_ will help to cancel out $\epsilon$ in the denomninator:

$$(t-1)\left[\frac1\epsilon(t-\epsilon) - \frac{1+\epsilon}{\epsilon(1-\epsilon)}t\right]=(t-1)\left[-1+\frac{t}{\epsilon}\left(1-\frac{1+\epsilon}{1-\epsilon}\right)\right]$$
$$=(t-1)\left[-1-\frac{2t}{1-\epsilon}\right].$$

Hence we now have a `safe' version

$$t+1=-(t-1)-\frac{2}{1-\epsilon}t(t-1)+\frac{2}{1-\epsilon}t(t-\epsilon),$$

so sending $\epsilon\to 0$ we have

$$t+1=-(t-1)-2t(t-1)+2t^2,$$

and dividing out $t^2(t-1)$ gives

$$\frac{t+1}{t^2(t-1)}=-\frac1{t^2}-\frac2t+\frac2{t-1},$$

recovering the same partial fraction decomposition as above.

#### Update Log
 * <span style="font-size:12px">211208: Created</span>
