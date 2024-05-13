---
title: 'An Abstract Nonsense for Gödel Incompleteness'
date: 2024-05-13
permalink: /posts/2024/05/abstract-nonsense-goedel-incompleteness/
author_profile: false
tags:
  - English
  - Mathematical Logic
  - Lindenbaum Algebra
---

Although Gödel's proof of his incompleteness is reknown for the formal construction of the sentence "I cannot be proven," there are ways to illuminate this in a frame of abstract nonsense. In nLab point of view, this is a consequence of [Lawvere's fixed point theorem](https://ncatlab.org/nlab/show/Lawvere's+fixed+point+theorem), as noted in [Yanofsky 2003](https://doi.org/10.2178/bsl/1058448677). But as I am not sure whether I understood the work right, I am presenting my own re-invention of the wheel below.

# Lindenbaum Ring

This concept is defined on the basis of the first-order logic. One can consult to [Smullyan 2007](https://books.google.fr/books/about/Logical_Labyrinths.html?id=8i-FeLk0tCcC&redir_esc=y) Ch.s II and IV; [Manin 2009](https://link.springer.com/book/10.1007/978-1-4419-0615-1) Ch. I; or [Cameron 1998](https://link.springer.com/book/10.1007/978-1-4471-0589-3) Ch. 4 for them. What is presented below is a brief list that I would like to remind.

Recall the first-order language consists of constants, functions, and relations. A *well-formed formula* on that language is recursively built from terms (constants or instances of functions), atomic formulae (instances of relations or equality), propositional connections (joining formulae by operations like AND, OR, NOT, etc.), and quantification of variables ($\forall x$ or $\exists x$, so to speak).

As a local term, we say the *arity* of a well-formed formula as the number of free variables in it. We denote by $$\mathrm{Wff}_n(\mathcal{L})$$ for the set of n-ary well-formed formulae of the language $\mathcal{L}$, whose free variables are restricted to be one of $$x_0,\ldots,x_{n-1}$$. By a 0-ary well-formed formula we say it is a *sentence*. We view that $$\mathrm{Wff}_n(\mathcal{L})\subset\mathrm{Wff}_{n+1}(\mathcal{L})$$ for all n≥0.

Recall that the first-order logic has a notion of *formal proof from a set of axioms* and *models validating a sentence*, denoted by $\Gamma\vdash\varphi$ (the set Γ formally proves φ) and $M\vDash\varphi$ (the model M validates φ) respectively. By a *logical equivalence*, denoted by $\phi\Leftrightarrow\psi$, we mean that $\vdash\phi\leftrightarrow\psi$, i.e., the equivalence is proven without any additional axioms other than the logical ones.

 > **Definition.** (Lindenbaum ring) The set of (n-ary) **Lindenbaum classes** is the quotient $$\mathrm{Lind}_n:=\mathrm{Wff}_n(\mathcal{L})/\Leftrightarrow$$ of well-formed formulae modulo logical equivalence.
 > 
 > Depending on the algebra structure that the set carries, it has two different names:
 >
 > 1. The **null-false (n-ary) Lindenbaum algebra** $$\overline{\mathrm{Lind}}_n=(\mathrm{Lind}_n,0,1,+,\cdot)$$ is defined as
 >
 > $$\begin{array}{rl}0 &:= \bot = \neg(x=x), \\ 1 &:= \top = (x=x), \\\phi+\psi & := \phi\ \mathrm{XOR}\ \psi=(\phi\wedge\neg\psi)\vee(\neg\phi\wedge\psi), \\ \phi\cdot\psi &:= \phi\ \mathrm{AND}\ \psi=\phi\wedge\psi. \end{array}$$
 >
 > 2. The **null-true (n-ary) Lindenbaum algebra** $$\underline{\mathrm{Lind}}_n=(\mathrm{Lind}_n,0',1',+',\cdot')$$ is defined as
 >
 > $$\begin{array}{rl}0' &:= \top, \\ 1' &:= \bot, \\\phi+'\psi & := \phi\ \mathrm{XNOR}\ \psi=(\phi\wedge\psi)\vee(\neg\phi\wedge\neg\psi), \\ \phi\cdot'\psi &:= \phi\ \mathrm{OR}\ \psi=\phi\vee\psi. \end{array}$$

By the above structures, we get Boolean algebras (commutative ring with 1 whose elements are all idempotent) that are isomorphic by the NOT map: i.e., $$x\in\overline{\mathrm{Lind}}_n\mapsto 1+x\in\underline{\mathrm{Lind}}_n$$ is a ring isomorphism. By this we see that null-false and null-true Lindenbaum rings are *Boolean duals*.

These algebras have natural order structure given by $a\leq b$ iff $a\cdot b=b$ (or $a\leq'b$ iff $a\cdot'b=b$, which is equivalent to $a\geq b$). The sense of *filters* are defined by this order.

The upper and lower lines are meant to indicate where the "True" is assigned. For $$\overline{\mathrm{Lind}}_n$$, the "True" is assigned to be 1, and for $$\underline{\mathrm{Lind}}_n$$, the "True" is assigned to be 0.

## Theories, Filters, and Ideals

For a first-order language L, an L-*theory* is a consistent set of sentences closed under logical inferences. This is saturated under logical equivalences, and it surjects onto a filter of the null-false 0-ary Lindenbaum algebra (or an ideal of the null-true algebra).

For an L-theory T, we define the *null-true Lindenbaum ring*, denoted by $$\underline{\mathrm{Lind}}_0(T)$$, as the ring $$\underline{\mathrm{Lind}}_0/(T)$$, where (T) on the right hand side is the ideal (of the null-true algebra) that corresponds to T. The *null-false Lindenbaum ring*, denoted by $$\overline{\mathrm{Lind}}_0(T)$$, is the Boolean dual of this ring. This ring is the same as $$\overline{\mathrm{Lind}}_0/(1+(T))$$.

By a *complete theory* we mean a maximal theory, and by completeness of the first order logic it precisely corresponds to the *theory of a model* M, i.e., the set of all sentences φ such that $M\vDash\phi$.

Therefore we have the following equivalence of data.

 > **Proposition.** The following data bijectively correspond:
 >
 > 1. Prime ideals of the null-true 0-ary Lindenbaum algebra
 > 1. Maximal ideals of the null-true algebra
 > 1. Nonzero ring map from the null-true algebra to the field of order 2
 > 1. Ultrafilters in the null-false algebra
 > 1. Complete L-theory
 > 1. Models modulo elementary equivalence

Recall that two models N, M are *elementarily equivalent* if the theories of N and M conicide, and is denoted by $N\equiv M$.

**(Proof)** Equivalence of 4, 5, and 6 is explained above. The equivalence of 2 and 4 is clear from the negation map. The equivalence of 1 and 2 follows from the fact that (a) any nonzero quotient of a Boolean algebra is also a Boolean algebra, and (b) the only Boolean algebra without zero divisors is the field of two elements. The equivalence of 2 and 3 is from the ring theory. $\square$

So for any model M, it induces a ring map $$M\colon\underline{\mathrm{Lind}}_0\to\mathbb{Z}/2\mathbb{Z}$$. Likewise, one can assign an interpretation of maximal ideals of $$\underline{\mathrm{Lind}}_n$$: it corresponds to a pair of a model M and an n-tuple of elements in M, modulo "elementary equivalence" for the pair. (Say $$(N,(b_0,\ldots,b_{n-1}))\equiv (M,(a_0,\ldots,a_{n-1}))$$ if for all $$\phi(x_0,\ldots,x_{n-1})\in\mathrm{Wff}_n(\mathcal{L})$$ we have $$N\vDash\phi(b_0,\ldots,b_{n-1})$$ iff $$M\vDash\phi(a_0,\ldots,a_{n-1})$$.)

I am not sure whether the latter interpretation yields us to identify the "space of n-types" to the prime spectrum of $$\underline{\mathrm{Lind}}_n$$.

# System Q

According to [Byunghan Kim's lecture note](https://drive.google.com/file/d/1_oooqG0_bHPwSBA6kQzOxxIjjt4YHV9J/view) on the Gödel's incompleteness, one introduces a first-order system which is suitable to introduce a sense of "computability." Just for the purpose of proving the incompleteness, a system which is slightly weaker than the Peano Arithmetic is sufficiently good, whose details and basicmost properties are copied below.

### System Q

Let $$\mathcal{L}_\mathbb{N}=(+,\cdot,S,<,0)$$ be the language of natural numbers. Let Q be the $$\mathcal{L}_\mathbb{N}$$-theory generated by the following 9 sentences.

 1. $(\forall x)(\neg(Sx=0))$.
 1. $(\forall x)(\forall y)((Sx=Sy)\to(x=y))$.
 1. $(\forall x)(x+0=x)$.
 1. $(\forall x)(\forall y)(x+Sy=S(x+y))$.
 1. $(\forall x)(x\cdot 0=0)$.
 1. $(\forall x)(\forall y)(x\cdot Sy=x\cdot y+y)$.
 1. $(\forall x)(\neg(x<0))$.
 1. $(\forall x)(\forall y)((x<Sy)\leftrightarrow((x<y)\vee(x=y)))$.
 1. $(\forall x)(\forall y)((x<y)\vee(x=y)\vee(y<x))$.

Adding the "induction" axiomatic scheme to this list yields the so-called Peano Arithmetic. We say any model of Q is a *model of system Q*.

### Recursive Functions and Relations

Recall that ω is the smallest infinite ordinal, which is a model of natural numbers within the set theory. For a relation $R\subset\omega^n$, following Kim's convention, we define its *characteristic function* in a null-true way:

$$\chi_R(\bar{a}) = \begin{cases} 0 & \text{ if }R(\bar{a}), \\ 1 & \text{ if }\neg R(\bar{a}). \end{cases}$$

A function $\omega^m\to\omega$ is said to be *recursive* if it is obtained by finitely many applications of the constructions below:

  1. (Primitives) The projections $$I^n_i(x_0,\ldots,x_{n-1})=x_i$$, addition $+\colon\omega^2\to\omega$, multiplication $\cdot\colon\omega^2\to\omega$, and comparison $$\chi_<\colon\omega^2\to\omega$$ are all recursive.
  2. (Compositions) For recursive functions $G\colon\omega^k\to\omega$ and $$H_1,\ldots,H_k\colon\omega^m\to\omega$$, the function $F\colon\omega^m\to\omega$ defined by the following is recursive.

  $$F(\bar{x})=G(H_1(\bar{x}),\cdots,H_k(\bar{x})).$$

  3. (Minimization) For a recursive $G\colon\omega^{m+1}\to\omega$ such that for every $\bar{a}\in\omega^m$ we have $x\in\omega$ in which $G(\bar{a},x)=0$, the function $F\colon\omega^m\to\omega$ defined by the following is recursive.

  $$F(\bar{a}) = \mu x(G(\bar{a},x)=0).$$

  (Here, $\mu xP(x)$ is a shorthand notation for "the minimum x such that P(x) holds.")

A relation $\subset\omega^m$ is *recursive* if its characteristic function is recursive. A relation $R\subset\omega^m$ is *recursively enumerable* if there is a recursive relation $Q\subset\omega^{m+1}$ such that $R(\bar{a})\Leftrightarrow(\exists x)(Q(\bar{a},x))$.

Notice that the above definition omits the *primitive recursion operator* as seen in other sources, e.g., [Wikipedia](https://en.wikipedia.org/wiki/General_recursive_function). This is omitted simply because it is redundant; see P13 (p. 8) in Kim's note.

Several "programming features" like equality (P5 in p. 2), constants (P3 in p. 2), logical connectives (P4 in p. 2), if-then branches (P9-10 in p. 4), bounded while loops (P6-7 in p. 3), and the list data type (pp. 5-7) are all implemented under this notion of recursiveness. Because of that, recursive functions can be understood as that one can program (modulo an indefinite capacity of memory) its verity of the input.

### Representability

Any natural number $n\in\omega$ is "representable" in $$\mathcal{L}_{\mathbb{N}}$$ by the term $\underline{n}=S\cdots S0$, where there are n many S's in the term. So for instance, $\underline{0}=0$, $\underline{1}=S0$, $\underline{2}=SS0$, $\underline{10}=SSSSSSSSSS0$, etc.

We say a relation $R\subset\omega^m$ is *representable in Q* if there is an m-ary $$\mathcal{L}_\mathbb{N}$$-formula $$\phi(x_0,\ldots,x_{m-1})$$ such that, for all $$(k_0,\ldots,k_{m-1})\in\omega^m$$,

 * that $R(k_0,\ldots,k_{m-1})$ implies $Q\vdash\phi(\underline{k_0},\ldots,\underline{k_{m-1}})$, and
 * that $\neg R(k_0,\ldots,k_{m-1})$ implies $Q\vdash\neg\phi(\underline{k_0},\ldots,\underline{k_{m-1}})$.

A function $f\colon\omega^m\to\omega$ is *representable in Q* if there exists an (m+1)-ary $$\mathcal{L}_\mathbb{N}$$-formula $$\phi(x_0,\ldots,x_{m-1},y)$$ such that, for all $$(k_0,\ldots,k_{m-1})\in\omega^m$$,

$$Q\vdash(\forall y)\left(\phi(\underline{k_0},\ldots,\underline{k_{m-1}},y)\leftrightarrow y=\underline{f(k_0,\ldots,k_{m-1})}\right).$$

The followings are easy exercises.

 * A relation is representable iff its characteristic function is representable in Q. <br> [From a relation represented by $\phi(\bar{x})$, take $\psi(\bar{x},y)=(\phi(\bar{x})\to(y=0))\wedge(\neg\phi(\bar{x})\to(y=\underline{1}))$. From a characteristic function represented by $\psi(\bar{x},y)$, take $\phi(\bar{x})=\psi(\bar{x},0)$.]
 * If a function is representable, then its graph is also representable. <br> [If $\phi(\bar{x},y)$ represents the function, then it represents the graph as well.]

I do not know whether the converse of the last implication is true.

 > **Representability Theorem.** (see p. 12 of Kim's note) Every recursive function or relation is representable in Q.

### Gödel Numbering

For a countable language $\mathcal{L}$ (potentially this is a language that extends $$\mathcal{L}_\mathbb{N}$$), suppose we let h to be an encoding of constants, functions, relations (including =), logical alphabets (￢, →, ∀, (, )), and variables (specified as $\langle x_i\rangle_{i<\omega}$), so that each encoded set is recursive (for instance, $$h(\{\text{constants}\})\subset\omega$$ is a recursive set).

Together with an encoding of sequences (see the **sequence number** defined in p. 6 of Kim's note), one can use h to define the *Gödel numbering* of $\mathcal{L}$-terms and formulae, which is denoted by $\lceil\sigma\rceil$ if σ is a term or formula. There, this induces an *injective* map $\lceil{}\cdot{}\rceil\colon\mathrm{Wff}_n(\mathcal{L})\to\omega$, for each n=0,1,2,...

The standard first-order logic proof system can be recursively encoded using this formalism; see pp. 14-18 of the note. In particular, a relation on Gödel numbers of sentences that says "a proof (of a given sentence) exists" is a *recursively enumerable* relation.

## Interpretation

For each n-ary formula $\phi(x_0,\ldots,x_{n-1})$, it defines a map

$$\underline{\phi}\colon \omega^n\to\underline{\mathrm{Lind}}_0(Q), \\ (k_0,\ldots,k_{n-1})\mapsto [\phi(\underline{k_0},\ldots,\underline{k_{n-1}})]_Q.$$

If φ represents an n-ary relation on ω, then the image of this map must have values $0=[\top]$ or $1=[\bot]$. Conversely, if $\underline{\phi}$ has values only in {0,1}, then φ must represent an n-ary relation on ω. (So otherwise, it can fall into the "ambiguous zone" where the validity of $\underline{\phi}(k_0,\ldots,k_{n-1})$ depends on the model of Q.)

If φ represents a recursive relation, it is even better: one can systematically reduce the sentence and decide whether it is 0 or 1 at the end. (This reminds me the β-reductions in λ-calculi.)

Now let φ be an 1-ary formula. Then we have a composition

$$\mathrm{Wff}_0(\mathcal{L}_\mathbb{N})\xrightarrow{\lceil{}\cdot{}\rceil}\omega\xrightarrow{\underline{\phi}}\underline{\mathrm{Lind}}_0(Q),$$

whose composition is denoted by $T_h\phi$ instead of more standard $\underline{\phi}\circ\lceil{}\cdot{}\rceil$. (This comes from my old misunderstanding that the Gödel numbering is not far from the encoding map h of the language, so that I intended to say $T_h\phi=\phi\circ h$ as the composition above.)

Now we compare this composition $T_h\phi$ and the natural surjection $$\mathsf{Wff}_0(\mathcal{L}_\mathbb{N})\twoheadrightarrow\underline{\mathrm{Lind}}_0(Q)$$. Then the reknown diagonalization step (for creating "I cannot be proven") can be stated as follows.

 > **Theorem.** (Gödel's Fixed Point Theorem) For any $$\phi(x_0)\in\mathrm{Wff}_1(\mathcal{L}_\mathbb{N})$$, there is $$\sigma\in\mathrm{Wff}_0(\mathcal{L}_\mathbb{N})$$ such that $T_h\phi(\sigma)=[\sigma]_Q$.

The proof requires some constructions, so I will refer to p. 19 of the note where it is stated and proven (in a standard way). Now a corollary of this "diagonalization" follows.

 > **Corollary.** Let M be a model of Q, in which we abuse the notation and denote by $$M\colon\mathrm{Wff}_0(\mathcal{L}_\mathbb{N})\twoheadrightarrow\underline{\mathrm{Lind}}_0\to\mathbb{Z}/2\mathbb{Z}\subset\underline{\mathrm{Lind}}_0(Q)$$ the corresponding ring map. Then for any $$\phi(x_0)\in\mathrm{Wff}_1(\mathcal{L}_\mathbb{N})$$, we have $T_h\phi\neq M$.

That is, no 1-ary formula can realize the model map.

**(Proof)** Given $\phi(x_0)\in\mathrm{Wff}_1$, find $\sigma\in\mathrm{Wff}_0$ such that $[\sigma]_Q=T_h(\neg\phi)(\sigma)=1+T_h\phi(\sigma)$. We claim that $T_h\phi\neq M$ at σ.

If $[\sigma]_Q$ is 0 or 1, then $M(\sigma)=[\sigma]_Q=1+T_h\phi(\sigma)$ implies that $T_h\phi\neq M$ at σ. If $[\sigma]_Q$ is neither 0 nor 1, then $T_h\phi(\sigma)$ cannot be so either, hence it is different from M(σ) (which must be 0 or 1). $\square$

### Why this yields the incompleteness

If the theory of M (a model of Q) is decidable (in the sense of p. 18 of the note), then the subset $$\{\lceil\sigma\rceil : M\vDash\sigma\}\subset\omega$$ is recursive and hence represented by $\phi(x_0)\in\mathrm{Wff}_1$ in Q. As this possibility was ruled out by the corollary above, we see that such theory cannot be decidable.

### Reinventing Yanofsky's Wheel

Basically Yanofsky's work (Yanofsky 2003, Thm. 4 of Sec. 5) contains almost the same argument as I have stated above, except that they exclusively uses Lindenbaum algebra throughout. This is little subtle, in the sense that the Gödel numbeering on the Lindenbaum algebra needs some words to well-define (say defining it as $$\lceil[\sigma]\rceil = \inf\{\lceil\psi\rceil : \psi\in[\sigma]\}$$) which was omitted in the work. Nonetheless, the essential machinery, especially the steps introducing the fixed points, is not harmed.

# Next?

Having built all this, my next question is this:

 > Given that $T_h\phi$ cannot realize the model ring map $M\colon\mathrm{Wff}_0\to\mathbb{Z}/2\mathbb{Z}$, to which extent can we approximate it?

Here is a naïve idea. Suppose T is a subset of the theory of M which is axiomatizable (in the sense of p. 18 of the note). If $\phi(x_0)=Pf_T(x_0)$ is the corresponding provability clause, then although this will only approximate the model map M (and leave many theory of M as "ambiguous"), as we increase T, the map $T_hPf_T$ will approximate M better and better. So the question will become *to suggest a measure that how this approximation improves.*

<!-- There might be nice geometric ideas that may come into play. For instance, as models (modulo elementary equivalence) form a totally disconnected space (by the prime spectrum of the ring $\underline{\mathrm{Lind}}_0(Q)$), we can imagine a geometric context to view this (say as ends of a tree). As the maps $T_h\phi$ will define a map from $\mathrm{Wff}_0$ to $\underline{\mathrm{Lind}}_0(Q)$, by an appropriate currying we might extend this from the tree to the space of functions $\mathrm{Wff}_0\to\mathbb{Z}/2\mathbb{Z}$. Will that be useful? -->

#### Update Log
 * <span style="font-size:12px">240513: Created</span>
