---
title: 'A Formula of Hyperbolic Distance'
date: 2022-06-21
permalink: /posts/2022/06/hyperbolic-distance
tags:
  - English
  - Hyperbolic geometry
  - Complex Analysis
  - Upper half plane
---

The idea of this post is to (1) introduce a formula to measure a distance on the upper half plane with the 'standard' hyperbolic metric, and (2) record some ideas of deriving this.

## Preliminaries

I list some basic facts about the [upper half plane](https://en.wikipedia.org/wiki/Poincar%C3%A9_half-plane_model) $$\mathbb{H}=\{z\in\mathbb{C} : \Im z>0\}$$ model of the hyperbolic 2-plane.

 * To have the curvature $-1$, the standard choice of metric is

$$ ds^2 = \frac{dx^2+dy^2}{y^2}.$$

 * Geodesics in $\mathbb{H}$ are, as figures in $\mathbb{C}$, either upper half circles centered at a real number, or vertical lines (i.e., lines parallel to the imaginary axis).
 * Isometries of $\mathbb{H}$ are given as Mobius transforms by real matrices. That is, for each isometry $f\colon\mathbb{H}\to\mathbb{H}$, we have $a,b,c,d\in\mathbb{R}$, $ad\neq bc$, such that

 $$f(z)=\frac{az+b}{cz+d}.$$

 * Fix $z_2\in\mathbb{H}$. The map $z\mapsto(z-z_2)/(z-\overline{z}_2)$ is an isometric map $\mathbb{H}\to\mathbb{D}$ to the [Poincare disk model](https://en.wikipedia.org/wiki/Poincar%C3%A9_disk_model). The map sends $z_2\in\mathbb{H}$ to $0\in\mathbb{D}$.
 * The hyperbolic circles in $\mathbb{D}$, centerd at $0\in\mathbb{D}$, are same as Euclidean circles with the same center. (For other centers, the descriptions get more complicated.)

## Distance Formula

Morally, one can find the hyperbolic distance between $z_1,z_2\in\mathbb{H}$ by sketching the hyperbolic geodesic between them, and use the formula

$$\mathsf{len}(\gamma)=\int_\gamma\frac{\sqrt{dx^2+dy^2}}{y}$$

to evaluate the distance. This is nice, except that it requires an unfeasible amount of computations.

So we introduce a 'formula-wise' way to find the distance, which reads as follows.

\begin{equation}
\label{eqn:hyperbolic-distance}
\mathsf{dist}_{\mathbb{H}}(z_1,z_2)=\log\left(\frac{|z_1-\overline{z}_2|+|z_1-z_2|}{|z_1-\overline{z}_2|-|z_1-z_2|}\right).
\end{equation}

Here is a geometric interpretation of the formula.

![geometric-interpretation](/images/220621-fig1.png)

Although the distance formula does not look symmetric in $z_1$ and $z_2$, the symmetry evidently follows from the geometric interpretation. (An algebraic verification is not too hard, though.)

We aim to prove \eqref{eqn:hyperbolic-distance} in this post.

## Idea

Fix $z_2\in\mathbb{H}$. The idea of the proof is to think of the locus of points $z_1\in\mathbb{H}$ that are claimed to be 'equidistanced' from $z_2$. If such loci are hyperbolic circles, then we can claim the relation with the actual hyperbolic distances.

To elaborate, define the quantity

\begin{equation}
\label{eqn:exp-hyperbolic-distance}
D(z_1,z_2) = \frac{|z_1-\overline{z}_2|+|z_1-z_2|}{|z_1-\overline{z}_2|-|z_1-z_2|}.
\end{equation}

It is not hard to show that the quantity $D(z_1,z_2)$ always stays in $[1,\infty)$, with $D(z_1,z_2)=1$ iff $\vert z_1-z_2\vert =0$ iff $z_1=z_2$.

Fix $D_0>0$. If the set of points $z\in\mathbb{H}$ with $D(z,z_2)=D_0$ forms a hyperbolic circle, then we infer that its (hyperbolic) radius $\rho=\mathsf{dist}_\mathbb{H}(z,z_2)$ should be determined by $D_0$. Then we study the relation $\rho=\rho(D_0)$ by, say, plugging in special points like $z=z_0+it$ ($t$ a real number, $t\in(0,\infty)$).

### Hyperbolic circles

Declare the map $\phi\colon\mathbb{H}\to\mathbb{D}$ by

$$\phi(z)=\frac{z-z_2}{z-\overline{z}_2}.$$

Then this $\phi$ is an isometry that sends $z_2\mapsto 0$. Furthermore, the quantity \eqref{eqn:exp-hyperbolic-distance} may be written as

$$D(z,z_2)=\frac{1+|\phi(z)|}{1-|\phi(z)|}.$$

Thus the set of points $z\in\mathbb{H}$ with $D(z,z_2)=D_0$ is thus sent to, via $\phi$, the set of points $w\in\mathbb{D}$ with $\vert w\vert=\frac{D_0-1}{D_0+1}$. That is, the locus is mapped to a circle (Euclidean and hyperbolic) in $\mathbb{D}$, centered at $0$. As $\phi$ is an isometry, this implies that the points $z\in\mathbb{H}$ with $D(z,z_2)=D_0$ form a hyperbolic circle (in $\mathbb{H}$).

This means that the quantity $$\mathsf{dist}_\mathbb{H}(z,z_2)$$ is constant if $D(z,z_2)$ is constant, i.e., $\mathsf{dist}_\mathbb{H}(z,z_2)$ is a function of $D(z,z_2)$. We declare a function $\rho\colon[1,\infty)\to[0,\infty)$ and write $$\rho(D(z,z_2))=\mathsf{dist}_\mathbb{H}(z,z_2)$$ for that status.

### Relation

Now we plug in $z=z_2+it$, where $t>0$. Then the hyperbolic geodesic connecting $z_2$ to $z$ is given as a curve $\gamma(s)=z_2+is$, $0\leq s\leq t$. There, we compare

$$D(z,z_2)=\frac{|z-\overline{z}_2|+|z-z_2|}{|z-\overline{z}_2|-|z-z_2|} \\ =\frac{|z_2-\overline{z}_2+it|+|it|}{|z_2-\overline{z}_2+it|-|it|} \\ = \frac{(2\Im z_2 + t) + t}{(2\Im z_2+t)-t} \\ = 1+\frac{t}{\Im z_2},$$

and

$$\mathsf{dist}_\mathbb{H}(z,z_2)=\int_0^t\frac{|\gamma'(s)|\, ds}{\Im\gamma(s)} = \int_0^t\frac{ds}{\Im z_2 + s} \\ = \log\left(\frac{\Im z_2 + t}{\Im z_2}\right) = \log\left(1+\frac{t}{\Im z_2}\right).$$

So given any input $D_0\in[1,\infty)$, we can write this as $D_0=1+t/\Im z_2$, and we have

$$\rho(D_0)=\rho(D(z,z_2))=\mathsf{dist}_\mathbb{H}(z,z_2) \\ =\log(1+t/\Im z_2)=\log D_0.$$

We thus conclude that,

$$\mathsf{dist}_\mathbb{H}(z_1,z_2) = \log D(z_1,z_2),$$

which is essentially \eqref{eqn:hyperbolic-distance}, as required.

#### Update Log
 * <span style="font-size:12px">220621: Created</span>
