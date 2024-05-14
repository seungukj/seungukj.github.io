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

Although Gödel's proof of his incompleteness is renowned for the formal construction of the sentence "I cannot be proven," there are ways to illuminate this within the framework of abstract nonsense. From the nLab point of view, this is a consequence of [Lawvere's fixed point theorem](https://ncatlab.org/nlab/show/Lawvere's+fixed+point+theorem), as shown in [Lawvere 1969](http://tac.mta.ca/tac/reprints/articles/15/tr15abs.html) or [Yanofsky 2003](https://doi.org/10.2178/bsl/1058448677). However, since I am not entirely sure if I understood the work correctly, I will present my own re-invention of the wheel below.

# Lindenbaum Ring

This concept is defined based on first-order logic. One can consult to [Smullyan 2007](https://mathscinet.ams.org/mathscinet/relay-station?mr=2474164) Chapters II and IV; [Manin 2009](https://link.springer.com/book/10.1007/978-1-4419-0615-1) Chapter I; [Enderton 2001](https://mathscinet.ams.org/mathscinet/relay-station?mr=1801397) ([OpenLogic ed.](https://builds.openlogicproject.org/courses/enderton/open-logic-enderton.pdf) Part II; or [Cameron 1998](https://link.springer.com/book/10.1007/978-1-4471-0589-3) Chapter 4 for more information. What is presented below is a brief summary that I would like to provide.

Recall that the first-order language consists of constants, functions, and relations. A *well-formed formula* in that language is recursively built from terms (constants, variables, or instances of functions), atomic formulae (instances of relations or equality), propositional connectors (joining formulae by operations like AND, OR, NOT, etc.), and quantification of variables (∀x or ∃x, so to speak).

As a local convention, we define the *arity* of a well-formed formula as the number of free variables in it. We denote by $$\mathrm{Wff}_n(\mathcal{L})$$ the set of n-ary well-formed formulae of the language $\mathcal{L}$, where free variables are restricted to be one of $$x_0,\ldots,x_{n-1}$$. A 0-ary well-formed formula is called a *sentence*. We consider $$\mathrm{Wff}_n(\mathcal{L})$$ to be a subset of $$\mathrm{Wff}_{n+1}(\mathcal{L})$$ for all n≥0.

Recall that first-order logic has a notion of *formal proof from a set of axioms*. This means we have a sequence of formulae where each term is (a) one of the given axioms, (b) one of the logical axioms, or (c) a consequence of inference rules from the terms before it. If Γ is a set of formulae and there is a finite list of formulae $\phi_1,\ldots,\phi_n$ which is a formal proof from the set Γ, then we say that Γ formally proves $\phi_n$ and denote it by $\Gamma\vdash\phi_n$. A *logical equivalence*, denoted by $\phi\Leftrightarrow\psi$, means that $\vdash\phi\leftrightarrow\psi$, indicating that the equivalence is proven without any additional axioms other than the logical ones. A set of axioms is *inconsistent* if it can formally prove every sentence, and it is *consistent* when it is not inconsistent.

Recall also that first-order logic has *models validating a sentence*. This means we have a set M with (a) various elements representing constants of the language, (b) various functions $M^k\to M$ representing functions of the language (respecting the arity), and (c) various relations $\subset M^k$ of the language. The additional structures depicted in (a)-(c) is called the *interpretation* of the language, and a set with an interpretation is called a *model*. For a sentence σ, we denote by M⊨σ if the interpretation of the model M views σ as a true sentence, and say that M validates σ, or M is a model of σ. A *theory* of a model M is the set of sentences σ such that M⊨σ.

 > **Definition.** (Lindenbaum algebra) The set of (n-ary) **Lindenbaum classes** is the quotient $$\mathrm{Lind}_n:=\mathrm{Wff}_n(\mathcal{L})/\Leftrightarrow$$ of well-formed formulae modulo logical equivalence.
 > 
 > Depending on the algebra structure that the set carries, it has two different names:
 >
 > * The **null-false (n-ary) Lindenbaum algebra** $$\overline{\mathrm{Lind}}_n=(\mathrm{Lind}_n,0,1,+,\cdot)$$ is defined as
 >
 > $$\begin{array}{rl}0 &:= \bot = \neg(x=x), \\ 1 &:= \top = (x=x), \\\phi+\psi & := \phi\ \mathrm{XOR}\ \psi=(\phi\wedge\neg\psi)\vee(\neg\phi\wedge\psi), \\ \phi\cdot\psi &:= \phi\ \mathrm{AND}\ \psi=\phi\wedge\psi. \end{array}$$
 >
 > * The **null-true (n-ary) Lindenbaum algebra** $$\underline{\mathrm{Lind}}_n=(\mathrm{Lind}_n,0',1',+',\cdot')$$ is defined as
 >
 > $$\begin{array}{rl}0' &:= \top, \\ 1' &:= \bot, \\\phi+'\psi & := \phi\ \mathrm{XNOR}\ \psi=(\phi\wedge\psi)\vee(\neg\phi\wedge\neg\psi), \\ \phi\cdot'\psi &:= \phi\ \mathrm{OR}\ \psi=\phi\vee\psi. \end{array}$$

Through these structures, we get Boolean algebras (commutative rings with 1 whose elements are all idempotent) that are isomorphic by the NOT map: i.e., $$x\in\overline{\mathrm{Lind}}_n\mapsto 1+x\in\underline{\mathrm{Lind}}_n$$ is a ring isomorphism. Thus, we see that null-false and null-true Lindenbaum rings are *Boolean duals*.

These algebras have a natural order structure given by $a\leq b$ iff $a\cdot b=b$ (or $a\leq'b$ iff $a\cdot'b=b$, which is equivalent to $a\geq b$). The concept of *filters* is defined based on this order.

The upper and lower lines indicate where the "True" value is assigned. For $$\overline{\mathrm{Lind}}_n$$, the "True" is assigned to be 1, while in $$\underline{\mathrm{Lind}}_n$$, the "True" is assigned to be 0.

## Theories, Filters, and Ideals

For a first-order language L, an L-*theory* is a consistent set of sentences closed under logical inferences. This set is the preimage of a filter of the null-false 0-ary Lindenbaum algebra (or an ideal of the null-true algebra), along the natural projection map $$\mathrm{Wff}_0\twoheadrightarrow\overline{\mathrm{Lind}}_0$$.

For an L-theory T, we define the *null-true Lindenbaum algebra of T*, denoted by $$\underline{\mathrm{Lind}}_0(T)$$, as the ring $$\underline{\mathrm{Lind}}_0/(T)$$, where (T) on the quotient is the ideal (of the null-true algebra) that corresponds to the theory T. The *null-false Lindenbaum algebra of T*, denoted by $$\overline{\mathrm{Lind}}_0(T)$$, is the Boolean dual of this ring. This ring is equivalent to $$\overline{\mathrm{Lind}}_0/(1+(T))$$. These algebras are also known as [Lindenbaum-Tarski algebras](https://en.wikipedia.org/wiki/Lindenbaum%E2%80%93Tarski_algebra).

For an n-ary formula $\phi$, denote by $$[\phi]_T\in\mathrm{Lind}_n(T)$$ the corresponding equivalence class. That is, $$[\phi]_T=\{\psi : T\vdash\phi\leftrightarrow\psi\}$$.

A *complete theory* is a maximal theory, and according to the completeness of first order logic, it precisely corresponds to the *theory of a model* M, i.e., the set of all sentences $\phi$ such that $M\vDash\phi$.

Therefore we have the following equivalence of data.

 > **Proposition.** The following data bijectively correspond:
 >
 > 1. Prime ideals of the null-true 0-ary Lindenbaum algebra
 > 1. Maximal ideals of the null-true algebra
 > 1. Nonzero ring maps from the null-true algebra to the field of order 2
 > 1. Ultrafilters in the null-false algebra
 > 1. Complete L-theories
 > 1. Models modulo elementary equivalence

Recall that two models N, M are *elementarily equivalent* if the theories of N and M conicide. This concept is denoted by $N\equiv M$.

**(Proof)** Equivalence of 4, 5, and 6 is explained above. The equivalence of 2 and 4 is clear from the negation map. The equivalence of 1 and 2 follows from the fact that (a) any nonzero quotient of a Boolean algebra is also a Boolean algebra, and (b) the only Boolean algebra without zero divisors is the field of two elements. The equivalence of 2 and 3 is from the ring theory. $\square$

Therefore, for any model M, it induces a ring map $$M\colon\underline{\mathrm{Lind}}_0\to\mathbb{Z}/2\mathbb{Z}$$. Likewise, one can assign an interpretation of maximal ideals of $$\underline{\mathrm{Lind}}_n$$: it corresponds to a pair of a model M and an n-tuple of elements in M, modulo "elementary equivalence" for the pair. (Say $$(N,(b_0,\ldots,b_{n-1}))\equiv (M,(a_0,\ldots,a_{n-1}))$$ if for all $$\phi(x_0,\ldots,x_{n-1})\in\mathrm{Wff}_n(\mathcal{L})$$ we have $$N\vDash\phi(b_0,\ldots,b_{n-1})$$ iff $$M\vDash\phi(a_0,\ldots,a_{n-1})$$.)

I am uncertain whether the latter interpretation allows us to identify the "space of complete n-types" with the prime spectrum of $$\underline{\mathrm{Lind}}_n$$.

# System Q

According to [Byunghan Kim's lecture note](https://drive.google.com/file/d/1_oooqG0_bHPwSBA6kQzOxxIjjt4YHV9J/view) on Gödel's incompleteness, a first-order system suitable for introducing a sense of "computability" is introduced. For the purpose of proving incompleteness, a system slightly weaker than Peano Arithmetic is sufficient. Below are the details and basic properties of the system, copied from the note quoted above.

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

Adding the "induction" axiomatic scheme to this list yields the so-called Peano Arithmetic. Any model of Q is refrerred to as a *model of system Q*.

### Recursive Functions and Relations

Recall that ω is the smallest infinite ordinal, which serves as a model of natural numbers within the set theory. For a relation $R\subset\omega^n$, following Kim's convention, we define its *characteristic function* in a null-true way:

$$\chi_R(\bar{a}) = \begin{cases} 0 & \text{ if }R(\bar{a}), \\ 1 & \text{ if }\neg R(\bar{a}). \end{cases}$$

A function $\omega^m\to\omega$ is said to be *recursive* if it is obtained by finitely many applications of the constructions below:

  * (Primitives) The projections $$I^n_i(x_0,\ldots,x_{n-1})=x_i$$, addition $+\colon\omega^2\to\omega$, multiplication $\cdot\colon\omega^2\to\omega$, and comparison $$\chi_<\colon\omega^2\to\omega$$ are all recursive.
  * (Compositions) For recursive functions $G\colon\omega^k\to\omega$ and $$H_1,\ldots,H_k\colon\omega^m\to\omega$$, the function $F\colon\omega^m\to\omega$ defined by the following is recursive:

  $$F(\bar{x})=G(H_1(\bar{x}),\cdots,H_k(\bar{x})).$$

  * (Minimization) For a recursive $G\colon\omega^{m+1}\to\omega$ such that for every $\bar{a}\in\omega^m$ we have $x\in\omega$ in which $G(\bar{a},x)=0$, the function $F\colon\omega^m\to\omega$ defined by the following is recursive:

  $$F(\bar{a}) = \mu x(G(\bar{a},x)=0).$$

  (Here, $\mu xP(x)$ is a shorthand notation for "the minimum x such that P(x) holds.")

A relation $\subset\omega^m$ is *recursive* if its characteristic function is recursive. A relation $R\subset\omega^m$ is *recursively enumerable* if there is a recursive relation $Q\subset\omega^{m+1}$ such that $R(\bar{a})\Leftrightarrow(\exists x)(Q(\bar{a},x))$.

Notice that the above definition omits the *primitive recursion operator* seen in other sources, e.g., [Wikipedia](https://en.wikipedia.org/wiki/General_recursive_function). This omission is because it is redundant; see P13 (p. 8) in Kim's note.

Several "programming features" like equality (P5 in p. 2), constants (P3 in p. 2), logical connectives (P4 in p. 2), if-then branches (P9-10 in p. 4), bounded while loops (P6-7 in p. 3), and the list data type (pp. 5-7) are all implemented under this notion of recursiveness. Because of that, recursive functions can be understood as those functions that can be programmed (provided an indefinite capacity of memory).

### Representability

Any natural number $n\in\omega$ is "representable" in $$\mathcal{L}_{\mathbb{N}}$$ by the term $\underline{n}=S\cdots S0$, where there are n many S's in the term. For instance, $\underline{0}=0$, $\underline{1}=S0$, $\underline{2}=SS0$, $\underline{10}=SSSSSSSSSS0$, etc.

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

The significance of the above cannot be underestimated. This implies that in Q, any programmable relation is expressed as a logical predicate. Furthermore, any recursively enumerable relation is also written as a logical predicate. So (even without induction!) Q is a system that is suitable for bringing "computers" into the study of logic. Together with the Gödel numbering below, it can even bring its provability clause as a 1-ary formula.

### Gödel Numbering

For a countable language $\mathcal{L}$ (which may extend $$\mathcal{L}_\mathbb{N}$$), suppose we let h to be an ω-valued encoding of constants, functions, relations (including =), logical alphabets (￢, →, ∀, (, )), and variables (specified as $\langle x_i\rangle_{i<\omega}$), such that each encoded set is recursive (for instance, $$h(\{\text{constants}\})\subset\omega$$ is a recursive set).

Together with an encoding of sequences (see the **sequence number** defined on p. 6 of Kim's note), one can use h to define the *Gödel numbering* of $\mathcal{L}$-terms and formulae, denoted by $\lceil\sigma\rceil$ if σ is a term or formula. This induces an *injective* map $\lceil{}\cdot{}\rceil\colon\mathrm{Wff}_n(\mathcal{L})\to\omega$, for each n=0,1,2,...

The standard first-order logic proof system can be recursively encoded using this formalism; see pp. 14-18 of the note. In particular, a relation on Gödel numbers of sentences that states "a proof (of a given sentence) exists" is *recursively enumerable*.

## Interpretation

For each n-ary formula $\phi(x_0,\ldots,x_{n-1})$, it defines a map

$$\underline{\phi}\colon \omega^n\to\underline{\mathrm{Lind}}_0(Q), \\ (k_0,\ldots,k_{n-1})\mapsto [\phi(\underline{k_0},\ldots,\underline{k_{n-1}})]_Q.$$

If $\phi$ represents an n-ary relation on ω, then the image of this map must have values $0=[\top]$ or $1=[\bot]$. Conversely, if $\underline{\phi}$ has values only in {0,1}, then $\phi$ must represent an n-ary relation on ω. (So otherwise, it falls into the "ambiguous zone" where the validity of $\underline{\phi}(k_0,\ldots,k_{n-1})$ depends on the model of Q.)

If $\phi$ represents a recursive relation, it is even better: one can systematically reduce the sentence and decide whether it is 0 or 1 at the end. (This reminds me the β-reductions in λ-calculi.)

Now let $\phi$ be a 1-ary formula. Then we have a composition

$$\mathrm{Wff}_0(\mathcal{L}_\mathbb{N})\xrightarrow{\lceil{}\cdot{}\rceil}\omega\xrightarrow{\underline{\phi}}\underline{\mathrm{Lind}}_0(Q),$$

whose composition is denoted by $T_h\phi$ instead of more standard $\underline{\phi}\circ\lceil{}\cdot{}\rceil$. (This comes from my old misunderstanding that the Gödel numbering is not far from the encoding map h of the language, so I intended to say $T_h\phi=\phi\circ h$ as the composition above.) This map $T_h\phi$ leads us to view that $\phi(x_0)$ is a "function that takes sentences as its inputs," whose output is the Lindenbaum class of another sentence.

The fixed point of this function $T_h\phi$ is fundamental to the renowned diagonalization step (for creating "I cannot be proven"). Its existence is stated as follows.

 > **Theorem.** (Gödel's Fixed Point Theorem) For any $$\phi(x_0)\in\mathrm{Wff}_1(\mathcal{L}_\mathbb{N})$$, there is $$\sigma\in\mathrm{Wff}_0(\mathcal{L}_\mathbb{N})$$ such that $T_h\phi(\sigma)=[\sigma]_Q$.

The proof requires some constructions, so I will refer to p. 19 of the note where it is stated and proven (in a standard way), or a [section below](#reinventing-yanofsky-s-wheel) for the version using ideas of Lawvere fixed point theorem. Now a corollary of this diagonalization follows.

 > **Corollary.** Let M be a model of Q, in which we abuse the notation and denote by $$M\colon\mathrm{Wff}_0(\mathcal{L}_\mathbb{N})\twoheadrightarrow\underline{\mathrm{Lind}}_0\to\mathbb{Z}/2\mathbb{Z}\subset\underline{\mathrm{Lind}}_0(Q)$$ the corresponding ring map. Then for any $$\phi(x_0)\in\mathrm{Wff}_1(\mathcal{L}_\mathbb{N})$$, we have $T_h\phi\neq M$.

That is, no 1-ary formula can realize the model map.

**(Proof)** Given $\phi(x_0)\in\mathrm{Wff}_1$, find $\sigma\in\mathrm{Wff}_0$ such that $[\sigma]_Q=T_h(\neg\phi)(\sigma)=1+T_h\phi(\sigma)$. We claim that $T_h\phi\neq M$ at σ.

If $[\sigma]_Q$ is 0 or 1, then $M(\sigma)=[\sigma]_Q=1+T_h\phi(\sigma)$ implies that $T_h\phi\neq M$ at σ. If $[\sigma]_Q$ is neither 0 nor 1, then $T_h\phi(\sigma)$ cannot be so either, hence it is different from M(σ) (which must be 0 or 1). $\square$

### Why this yields the incompleteness

Suppose M is a model of Q whose theory is decidable (in the sense of p. 18 of the note). Then the subset $$\{\lceil\sigma\rceil : M\vDash\sigma\}\subset\omega$$ is recursive and hence is represented by $\phi(x_0)\in\mathrm{Wff}_1$ in Q. As this possibility was ruled out by the corollary above, we see that such theory cannot be decidable.

Now, suppose T is a set of sentences whose Gödel numbers form a recursive set, and T entails Q. (Examples include Peano Arithmetic and Q itself.) If T generates a complete theory, then it is decidable (by the 2nd theorem in p. 18 of the note). However, on the other hand, T has only one model up to elementary equivalence. Hence, by the discussion on the previous paragraph, we arrive at a contradiction. Therefore, T cannot be complete; this is usually referred as "there is a sentence that is neither proven nor disproven" yet true (in a model of T; choose any maximal extension of T containig that not-proven-nor-disproven sentence). 

Nonetheless, Gödel's fixed point theorem suggests a recursive way to extend T to be "more complete," i.e., we can add a sentence into T that was not proven nor disproven from T. However, such a construction at best yields a recursive set of axioms after a finite number of steps, so we still have an incomplete theory. I do not know if we continue this process indefinitely, we result in a complete theory.

Finally, we note that [Shoenfield 1967](https://www.karlin.mff.cuni.cz/~krajicek/shoenfield.pdf), Problem 6.5.a), is about characterizing a theory generated by a recursive set of sentences. It is characterized by a provability clause that is recursively enumerable.

# Reinventing Yanofsky's Wheel

It is known that Gödel's fixed point theorem can be abstractized using the Lawvere fixed point theorem. A recent account on this would be Yanofsky's work ([Yanofsky 2003](https://doi.org/10.2178/bsl/1058448677), Thm. 4 of Sec. 5). This work presents almost the same argument as I have stated above, with the difference being that they exclusively uses the Lindenbaum algebra throughout. This is a little subtle, in the sense that the Gödel numbering on the Lindenbaum algebra needs some words to well-define (for example, defining it as $$\lceil[\sigma]_Q\rceil = \inf\{\lceil\psi\rceil : \psi\in[\sigma]_Q\}$$), which was omitted in the work.

To get away from this subtlety, I am going to reformulate the "Lawvere box" as follows (note its 'heterogeneous' nature):

$$\begin{array}{ccc} \mathrm{Wff}_1\times\mathrm{Wff}_1 & \xrightarrow{F} & \mathrm{Wff}_0 \\ {\scriptstyle \mathrm{diag}}\uparrow & & \downarrow {\scriptstyle T_h\phi} \\ \mathrm{Wff}_1 & \xrightarrow{g} & \underline{\mathrm{Lind}}_0(Q). \end{array}$$

Here, each arrow is defined as follows.

 * The map $$F\colon\mathrm{Wff}_1\times\mathrm{Wff}_1\to\mathrm{Wff}_0$$ is defined as $$F(\alpha(x_0),\beta(x_0))=\beta(\underline{\lceil\alpha(x_0)\rceil})$$.
 * The map $$T_h\phi\colon\mathrm{Wff}_0\to\underline{\mathrm{Lind}}_0(Q)$$ is as usual, i.e., $$T_h\phi(\sigma)=[\phi(\underline{\lceil\sigma\rceil})]_Q$$.

We furthermore introduce a recursive function
  
 * $dg\colon\omega\to\omega$, such that $dg(\lceil\phi(x_0)\rceil)=\lceil\phi(\underline{\lceil\phi(x_0)\rceil})\rceil$. (See Lemma in p. 19 of Kim's note.)

As the map $dg$ is recursive, it is represented by a formula $\psi(x_0,y)$ (i.e., $Q\vdash(\forall y)(\psi(\underline{n},y)\leftrightarrow y=\underline{dg(n)})$ for all $n\in\omega$). Let $\gamma(x_0):=(\exists y)(\psi(x_0,y)\wedge\phi(y))$, so that $Q\vdash\gamma(\underline{n})\leftrightarrow\phi(\underline{dg(n)})$ for all $n\in\omega$. 
Then the map $g(\beta)=T_h\phi(F(\beta,\beta))$ in the box is represented by F via the formula $\gamma(x_0)$, by the following computation:

$$\begin{array}{rl} g(\beta) &= T_h\phi(F(\beta,\beta)) \\ &= [\phi(\underline{\lceil\beta(\underline{\lceil\beta\rceil})\rceil})]_Q \\ &= [\phi(\underline{dg(\lceil\beta\rceil)})]_Q \\ &= [\gamma(\underline{\lceil\beta\rceil})]_Q = [F(\beta,\gamma)]_Q. \end{array}$$

Hence by the proof of the Lawvere fixed point theorem, we see that $g(\gamma)$ is the demanded fixed point; indeed, $g(\gamma)=T_h\phi(F(\gamma,\gamma))=T_h\phi(g(\gamma))$.

<!-- Nonetheless, the essential machinery, especially the steps introducing the fixed points, should not be harmed. -->

# Next?

Having built all this, my next question is this:

 > Given that $T_h\phi$ cannot realize the model ring map $M\colon\mathrm{Wff}_0\to\mathbb{Z}/2\mathbb{Z}$, to what extent can $T_h\phi$ approximate M?

Here is a naïve idea. Suppose T is a subset of the theory of M which is axiomatizable (in the sense of p. 18 of the note). If $\phi(x_0)=Pf_T(x_0)$ is the corresponding provability clause, then although this will only approximate the model map M (and leave many theory of M as "ambiguous"), as we increase T, the map $T_hPf_T$ will approximate M better and better. So the question will become *to suggest a measure of how this approximation improves.*

<!-- There might be some nice geometric ideas that could come into play. For instance, since models (modulo elementary equivalence) form a totally disconnected space (by the prime spectrum of the ring $\underline{\mathrm{Lind}}_0(Q)$), we can imagine a geometric context to view this (say as ends of a tree). As the maps $T_h\phi$ will define a map from $\mathrm{Wff}_0$ to $\underline{\mathrm{Lind}}_0(Q)$, by appropriate currying, we might extend this from the tree to the space of functions $\mathrm{Wff}_0\to\mathbb{Z}/2\mathbb{Z}$. Would that be useful? -->

#### Update Log
 * <span style="font-size:12px">240513: Created</span>
 * <span style="font-size:12px">240514: Added some remarks, suggested by [Junekey Jeon](https://jk-jeon.github.io/)</span>
