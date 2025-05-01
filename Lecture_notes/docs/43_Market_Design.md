---
title: "43_Market_Design"
---

## [📹 Watch the introductory video here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5169777)
# Market Design

## 1  What Is Market Design?

- **Market design** is the research field that creates new allocation mechanisms for public services or resources where ordinary private markets are absent, importing the **“good properties of markets”**—efficiency, incentive compatibility, and fairness.

- Fairness concepts you have already encountered—such as **envy‑freeness** and **core stability**—are applied directly in concrete market‑design tools (e.g., school‑choice mechanisms, auction formats).

---

## 2  Public‑School Choice: The Boston Mechanism vs. Stable Matching

### (1) The traditional “standard procedure” (Boston mechanism, etc.)

Many countries assign students to public schools as follows:

1. **Students (parents) submit a ranked list of preferred schools.**  
2. **Schools (or the board of education)** use capacity limits and selection criteria (test scores, lotteries, …) to accept or reject first‐choice applicants.  
3. Rejected students move to their second choice, then third, and so on if seats are already filled.

#### Why it can look unfair

- Suppose student A is rejected by the first choice and finds the second‑choice school full; some admitted students there may have lower scores than A.

- If “A would have been admitted had that school been listed first,” one wonders, “Is this really fair?”

### (2) Can mutually preferred matches be blocked?

- A child C and a school S may **mutually prefer each other**, yet the traditional procedure assigns them elsewhere.

- When the parties themselves want the match but it does not occur, the outcome seems **unjust**.

### (3) Matching stability: core stability

- Treat the problem as a two‑sided matching game where **children and schools are both players** and design a mechanism satisfying **“no one prefers an alternative partner enough to deviate.”** This is the idea of **Stable Matching Theory**.

- Formally, stability requires  
  \[
    \text{For every child }C\text{ and school }S,\; C\text{ and }S\text{ do not both prefer each other to their current partners.}
  \]

- This is the matching analogue of **core stability** in cooperative games.

### (4) SOSM (Student‑Optimal Stable Matching)

- Research shows a mechanism that always yields a stable outcome and, among stable outcomes, gives children their most preferred one—the **student‑proposing Gale–Shapley algorithm** (SOSM).

- The United States, for example, uses this for public‑school assignment and medical‑residency matching, producing **better outcomes for participants** than older methods.

---

## 3  Auctions: Second‑Price Auctions and Envy‑Freeness

### (1) Designing auctions for public procurement

- While “auctions” have long been used in procurement, market‑design research asks **which rules allocate resources efficiently and fairly without distorting incentives.**

- A celebrated example is the **Second‑Price Auction**.

### (2) Definition

- In a standard (first‑price) auction, the **winner pays their own bid**.  
- In a second‑price auction, the **winner pays the second‑highest bid**.

#### Why this odd‑looking rule works

- Because **payment depends on the next‑highest bid**, bidders gain nothing by inflating their own bids.

- Overbidding does not raise what you pay (the second price determines that), so “pretend‑to‑bid‑high” offers no benefit—and may be risky.

- Hence **truthfully bidding your real willingness‑to‑pay** is the dominant strategy.

### (3) Envy‑freeness

- In a second‑price auction **losers do not envy the winner, and the winner does not feel overcharged**.

  *Simple example*  
  - A: value 100, bid 100  
  - B: value 80, bid 80  
  - C: value 70, bid 70  
  - Winner A pays 80 (the second price).  
  - B and C would lose money at 80, so they feel no envy; A values the item at 100, so paying 80 is a gain—also no envy.

- Thus the mechanism lets **“the highest valuer” win** and achieves both **efficiency** and **envy‑freeness**.

### (4) Lowest payment among efficient, envy‑free allocations

- The payment in a second‑price auction is **the smallest amount that still satisfies efficiency and envy‑freeness**.

- Consequently, this format is prized for “allocating resources efficiently and fairly while minimizing incentive distortions” and is widespread (e.g., online‑advertising auctions).

---

## 4  Summary

- **Market design** adapts **market‑like properties—efficiency, incentive alignment, fairness—** to allocation problems for public goods, resources, and services where private markets work poorly.

- In **public‑school choice**, stable‑matching mechanisms satisfy **core stability** and outperform traditional methods for both children and schools.

- In **auction design**, the second‑price auction simultaneously achieves **efficiency and envy‑freeness** while inducing truthful bids, and it is widely used from public procurement to online advertising.

- These cases show how theoretical ideas such as **envy‑freeness and core stability** can shape real‑world institutional design.

---
### [📝 Take the mini-quiz here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5169777)

