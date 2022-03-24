---
title: 'Discovering a nontriviality of the ε-δ definition, in a math way'
date: 2022-03-24
permalink: /posts/2022/03/epsilon-delta-limit/
tags:
  - English
  - Calculus
  - Pedagogy of Limits
  - Ultraproducts
  - Analysis
---

This is a record of a talk that I made in the UChicago Math dept. Pedagogy seminar, in 2022-02-23.

## Hurdles to understand the Standard Definition

A student of calculus who first get introduced the precise definition of the limit $\lim_{x\to c}f(x)=L$, should overcome some mental challenge to understand the following definition.

 > ($\epsilon$-$\delta$) For all $\epsilon>0$, there exists $\delta>0$ in which, $0<\vert x-c\vert<\delta$ implies $\vert f(x)-L\vert<\epsilon$.

There are several layers of hurdles to understand this:

 1. To understand why we use a lot of absolute values $\vert\cdot\vert$; especially, understanding that the concept of distance is intervening.
 1. To understand the logical quantifiers and connectives, like "for all" "there exists" or "implies".
 1. To make sense on why we have a particular order $\forall\epsilon\exists\delta$ in the definition.

Practically, the first two lines are already a challenge for a typical freshman calculus students. Especially in the situation where the instruture cannot pay more than two weeks, focusing on the first two (i.e., to understand the words _per se_) would be challenging enough for the students.

The third line is, according to my experience as a student and as an instructor, for a pretty limited number of people. But ironically, this holds all the connection from the infamous "intuitive" definition of limits.

## An Infamous 'Definition'

The infamous "intuitive" definition of the limit $\lim_{x\to c}f(x)=L$ reads as follows.

 > (?) As $x$ approaches to $c$, the value $f(x)$ approaches to $L$.

I have labeled this as (?), to avoid giving any meaningful name for this 'definition.' Nonetheless, this gives some contrast on the definition (?) and the standard definition ($\epsilon$-$\delta$) above, in the following way.

 * Definition (?) starts from a control on the _domain_, and asserts its result on the _range_.
 * Definition ($\epsilon$-$\delta$) starts with $\epsilon>0$ that controls the _range_, then gives the variable $\delta>0$ that controls the _domain_.

So apparently, the order of domain and range controls seems to be inverted between (?) and ($\epsilon$-$\delta$). Understanding this is the main key to the hurdle 3, understanding the order $\forall\epsilon\exists\delta$.

It is not surprising to believe that every instructor in analysis has their rationals to answer why the order makes sense. As one of such rationals, I state my rational as follows.

 > **Claim.** The order $\forall\epsilon\exists\delta$ is coming from the following inputs.
 > * Translating the 'definition' (?) into infinitesimals.
 > * By which we say 'proving something with infinitesimals?'
 > * The compactness principle in mathematical logic.

## Infinitesimal Definition

For brievity, I assume that $c=L=0$ in its sequels. That is, I only focus on the case $\lim_{x\to 0}f(x)=L$.

If one admits to use infinitesimals, one can translate the 'definition' (?) as follows.

 > (INF) If $x\neq 0$ is an infinitesimal, then so is $f(x)$.

Probably this is just a sophisticated wording of the 'definition' (?), which seemed to be an implicit understanding of the limits, but later banned in 19C. A summarized story, following [Mormann & Katz 2013](https://arxiv.org/abs/1304.1027), goes as follows.

 * People started using infinitesimals, despite its ill-logical nature.
 * In late 19C, Cantor, Dedekind, and Weierstrass 'rigorization project' succeeded to ban the infinitesimals from our calculus textbooks.
 * In 1961, A. Robinson succeeded in set-theoretical ontology of defining infinitesimals; a calculus text by [Keisler 1971](https://www.math.wisc.edu/~keisler/calc.html) was then published as the first text in 'calculus with infinitesimals.'

### Infinitesimal Definition taught in classes

Interestingly, the story keeps on even for 21C. A pedagogical 'experiment' reported in [Katz & Polev 2017](https://arxiv.org/abs/1701.05187) gives some interesting data:

 1. The authors asked students to prove
    $$\lim_{x\to 2}(x+5)=7,$$
    and students attempted (INF) and ($\epsilon$-$\delta$) in their solutions:

     * For (INF), 98% attempted this. 85% succeeded among those attempted.
     * For ($\epsilon$-$\delta$), 71% attempted this. 20% succeeded among those attempted.
    
    (To be fair, the course was designed to give an extensive practice on the ($\epsilon$-$\delta$) definition.)
 1. Student poll results, on thoughts regarding how each definition was helping for understanding:

<table>
    <tr>
        <td>&nbsp;</td>
        <td colspan="2">Continuity</td>
        <td colspan="2">Convergence Sequences</td>
    </tr>
    <tr>
        <td>&nbsp;</td>
        <td>General</td>
        <td>Knows def'n</td>
        <td>General</td>
        <td>Knows def'n</td>
    </tr>
    <tr>
        <td>($\epsilon$-$\delta$)</td>
        <td>10%</td>
        <td>9%</td>
        <td>21%</td>
        <td>24%</td>
    </tr>
    <tr>
        <td>(INF)</td>
        <td>69%</td>
        <td>75%</td>
        <td>74%</td>
        <td>80%</td>
    </tr>
</table>

(See [Katz & Polev 2017](https://arxiv.org/abs/1701.05187), sec. 3 for more data.)

Couple of interesting conclusions may be drawn from this:

 1. We still long for infinitesimals (at least for first learners).
 1. Sequences are surprisingly well-understood, even with $\epsilon$-$\delta$ definitions.
 1. (from [Katz & Polev 2017](https://arxiv.org/abs/1701.05187)) Once the students understand the basic concepts via their intuitive (INF) formulations, they are able to relate more easily to the ($\delta$-$\epsilon$) paraphrases of the definition.

### Foudational Details of Infinitesimals

Although the infinitesimal definition is elegant and easy to be understood, things happening under the rug is quite complicated. Even for [Keisler 1971](https://www.math.wisc.edu/~keisler/calc.html), the way how infinitesimals are founded in the main text, is based on the property it enjoys:

 > We say a number $x$ in which $-a<x<a$ holds for all positive real $a>0$, as _infinitesimals_.

The text then develops various calculus notions out of this.

The precise construction is introduced in the epilogue of the text. In analogy with the construction of real numbers (as equivalence classes of Cauchy sequences), the field of _hyperreal numbers_ is defined using the notion of 'ultraproduct equivalence.'

There, any discussions on the existence, or variety of such equivalence were skipped. I view this as a reasonable choice, however. Even for those who are interested in such issues, as far as I know, the minimal backgrounds to understand the precise construction of hyperrreal numbers, is the **Stone-Čech compactification**. This is one of the high-end topics in undergraduate point-set topology courses.

## Compactness

We say a number $x$ is an _infinitesimal_ if we have $-a<x<a$ for all positive real $a>0$. On one hand, this may be viewed as a [hyperreal number](https://en.wikipedia.org/wiki/Hyperreal_number). But logically speaking, we may view this as an object $x$ in which the formulas $-a<x<a$ are always interpreted true, whenever $a$ is a positive real number.<sup><a href="#fn1" id="ref1">1</a></sup>

Applying this logical viewpoint, one can translate the definition (INF) as follows.

 > (INF-logic) From the assumptions $\{0<\vert x\vert<a\mid a>0\}$, one can prove that $\vert f(x)\vert<\epsilon$, no matter what $\epsilon>0$ is.

Equivalently,

 > (INF-logic) For all $\epsilon>0$, the assumptions $\{0<\vert x\vert<a \mid a>0\}$ can prove that $\vert f(x)\vert<\epsilon$.

(So this already clears $\forall\epsilon$ start. But we are still left to quantify $\delta$.)

Now I state a principle in mathematical logic: the _compactness_.

 > **(A version of) Compactness in Math. Logic.** Let $\Gamma$ be a set of assumptions, and let $\Gamma\vdash\phi$ (i.e., $\Gamma$ can prove $\phi$, a statement). Then there is a finite subset $\Gamma'\subset\Gamma$ in which $\Gamma'\vdash\phi$.

The proof is surprisingly easy for this one:<sup><a href="#fn2" id="ref2">2</a></sup>

 > (Proof) <span style="font-family: sans-serif">If we write down a proof of $\phi$, then the lines we use is finite. In particular the lines that introduces assumptions from $\Gamma$ is finite. Putting $\Gamma'$ the set of lines that introduces assumptions, we see that only $\Gamma'$ suffices to get $\phi$.</span>



Work-In-Progress

#### Update Log
 * <span style="font-size:12px">220324: Created</span>
