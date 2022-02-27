---
title: '중국인의 나머지 정리 2'
date: 2022-02-26
permalink: /posts/2022/02/chinese-remainder-theorem-2/
tags:
  - Korean
  - Number Theory
  - Partial Fractions
  - p-adic Numbers
  - Adele
---

앞선 [포스트](/posts/2021/12/chinese-remainder-theorem/)에서는 부분분수 분해와 중국인의 나머지 정리 사이의 관계를 짚어보았으나, 막상 부분분수 분해를 중국인의 나머지 정리의 결과인 것으로 묘사한 바 있었다. 그러나 계산의 흐름을 보면 둘이 동치라 생각하는 편이 자연스러운데, 이 후속 포스트에서는 그 점을 명확히 하고자 한다.

이 포스트에서는 [p진수](https://ko.wikipedia.org/wiki/P%EC%A7%84%EC%88%98)에 대한 기초적인 내용은 이미 알고 있다고 가정한다. 또한, 이 포스트의 앞부분은 [K. Conrad](https://kconrad.math.uconn.edu/blurbs/gradnumthy/characterQ.pdf)의 $\mathbb{Q}$의 character group에 대한 글을 거의 그대로 따르고 있어, (배경설명 등의) 자세한 내용은 그 쪽을 참고하기를 바란다.

다음과 같이 가정한다.

 1. 정수 $m_1,\cdots,m_k$는 양의 정수로, 둘씩 서로 소이다. 여기서는 특별히 $m_i=p_i^{\alpha_i}$ 꼴 숫자라 둔다.
 1. 정수 $M = \prod_{j=1}^km_j=m_1\cdot m_2\cdot\cdots\cdot m_k$라 둔다.
 1. 정수 $$M_i=M/m_i=m_1\cdots m_{i-1}{\widehat{m}}_{i} m_{i+1}\cdots m_k$$라 두고, 또 $e_i$는 $M_i$의 mod $m_i$ inverse라 둔다. (즉, $e_iM_i\equiv 1\mod m_i$.)

얻고자 하는 목표는 다음과 같다.

\begin{equation}
\label{eqn:goal-equation}
\frac1M \equiv \sum_{j=1}^k\frac{e_j}{m_j}\mod 1.
\end{equation}

## 부분분수 분해 (정수론)

앞선 [포스트](/posts/2021/12/chinese-remainder-theorem/)의

$$\frac1{60}\equiv 2\cdot\frac13-\frac14+3\cdot\frac15\mod 1$$

와 같은 부분분수 분해는 보다 어려운 맥락에서 해석할 수 있다. ([K. Conrad](https://kconrad.math.uconn.edu/blurbs/gradnumthy/characterQ.pdf)의 수식 (2.1) 참고.)

유리수 $x$ 및 소수 $p$에 대해, $x$의 [p진수](https://ko.wikipedia.org/wiki/P%EC%A7%84%EC%88%98) **분수부**를 취하는 함수 $$\{x\}_p$$를 생각할 수 있다. 곧, 법 $p$의 [완전잉여계](https://mathworld.wolfram.com/CompleteResidueSystem.html) $0,1,\cdots,p-1$에 대한 $x$의 $p$진 전개에

$$x=\frac{a_{-k}}{p^k}+\frac{a_{-k+1}}{p^{k-1}}+\cdots+\frac{a_{-1}}{p}+a_0+a_1p+a_2p^2+\cdots$$

(단 각 $a_i\in\{0,1,\cdots,p-1\}$) 대해,

$$\{x\}_p:=\frac{a_{-k}}{p^k}+\frac{a_{-k+1}}{p^{k-1}}+\cdots+\frac{a_{-1}}{p}$$

라 정의한다.

그러면 유리수 $r\in\mathbb{Q}$에 대해 다음이 성립한다.

\begin{equation}
\label{eqn:partial-fraction-decomposition-adele}
r-\sum_p\{r\}_p\in\mathbb{Z}.
\end{equation}

여기서, $r$의 분모를 나누지 않는 소수 $q$에 대해서 $$\{r\}_q=0$$인 고로, 관계 \eqref{eqn:partial-fraction-decomposition-adele}는 사실상 유한합에 대한 결과이다.

 > (증명, \eqref{eqn:partial-fraction-decomposition-adele}) 임의의 소수 $q$에 대해, $$r-\sum_p\{r\}_p\in\mathbb{Z}_q$$가 성립함을 알면 된다. 이 때 $\{r\}_p$의 정의 상, $p\neq q$이면 $$\{r\}_p\in\mathbb{Z}_q$$가 따른다. 또한 $p=q$이면 $$r-\{r\}_q\in\mathbb{Z}_q$$이다.

가령 \eqref{eqn:partial-fraction-decomposition-adele}에 $r=\frac1{60}$을 적용하면,

$$\left\{\frac1{60}\right\}_2=\frac34, \\ \left\{\frac1{60}\right\}_3=\frac23, \\ \left\{\frac1{60}\right\}_5=\frac35,$$

을 얻고, 실제로 이들을 더하면

$$\frac1{60} = \frac34 + \frac23 + \frac35 - 2$$

를 얻는다.

## 중국인의 나머지 정리

이제 분해 \eqref{eqn:partial-fraction-decomposition-adele}을 활용해서 중국인의 나머지 정리에 대해 논하고자 한다. 이에 앞서, 다음 성질을 먼저 지적한다.

 > 유리수 $x,y$에 대해, $x\equiv y$ (mod $p$)면 (즉 $\dfrac{x-y}{p}$가 유리수이되 기약꼴의 분모가 $p$의 배수가 아니면) $$\{x\}_p=\{y\}_p$$이다.

그러면 $\frac1M$에 \eqref{eqn:partial-fraction-decomposition-adele}을 적용하면 다음을 얻는다.

$$\frac1M \equiv \sum_p\left\{\frac1M\right\}_p\mod 1.$$

이 때 $p\neq p_1,\cdots,p_k$인 (즉 $m_1,\cdots,m_k$의 **유일한** 소인수들과 다른) 경우 $M$ 자체가 $p$의 배수가 아니기 때문에, $$\{\frac1M\}_p=0$$이다. 따라서 위 합은 다음과 같이 다시 쓰일 수 있다.

\begin{equation}
\label{eqn:eqn-1} \frac1M \equiv \sum_{j=1}^k\left\{\frac1M\right\}_{p_j}\mod 1 \\ 
=\sum_{j=1}^k\left\{\frac1{m_jM_j}\right\}_{p_j}.
\end{equation}

$e_jM_j\equiv 1\mod m_j$이므로, 다음이 따른다.

$$\frac{1}{m_jM_j}-\frac{e_j}{m_j}=\frac{1-e_jM_j}{m_j}\cdot\frac{1}{M_j}.$$

두 분수 중 앞선 분수 $\dfrac{1-e_jM_j}{m_j}$는 사실 정수이며, 뒷 분수 $\dfrac{1}{M_j}$의 분모는 $p_j$와 서로 소이다. 따라서 $1/(m_jM_j)\equiv e_j/m_j\mod p_j$인 고로, 다음이 따른다.

\begin{equation}
\label{eqn:eqn-2}\left\{\frac1{m_jM_j}\right\}_{p_j}=\left\{\frac{e_j}{m_j}\right\}_{p_j}.
\end{equation}

한편으로, 분수 $e_j/m_j$의 분모는 $p_j$ 외의 소인수를 가지지 않기 때문에, 다음이 성립한다.

\begin{equation}
\label{eqn:eqn-3}\left\{\frac{e_j}{m_j}\right\}_{p_j}=\sum_p\left\{\frac{e_j}{m_j}\right\}_{p}\equiv \frac{e_j}{m_j}\mod 1.
\end{equation}

따라서 \eqref{eqn:eqn-1}, \eqref{eqn:eqn-2}, \eqref{eqn:eqn-3}을 모두 종합하면,

$$\frac1M \equiv \sum_{j=1}^k\left\{\frac1{m_jM_j}\right\}_{p_j}\mod 1 \\
=\sum_{j=1}^k\left\{\frac{e_j}{m_j}\right\}_{p_j}\phantom{\mod{}} \\
\equiv \sum_{j=1}^k\frac{e_j}{m_j}\mod 1.\phantom{9999}$$

이것으로 \eqref{eqn:goal-equation}을 보였다. 이하 여기서 중국인의 나머지 정리까지는 양변에 미지수 $x$를 곱하고, $x/m_j\equiv a_j/m_j\mod 1$이 주어졌다는 사실을 활용하면 된다.

#### Update Log
 * <span style="font-size:12px">220226: Created</span>
