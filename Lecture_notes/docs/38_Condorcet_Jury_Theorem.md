---
title: "38_Condorcet_Jury_Theorem"
---

## [📹 Watch the introductory video here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5169782)
# Condorcet Jury Theorem

## 1. Background and Motivation  

Up to now we have focused on **aggregating heterogeneous preferences**—how society should combine many different value judgments.  
The **Condorcet Jury Theorem**, by contrast, studies situations where **one option is objectively correct** for everyone, yet voters only have partial information about which option that is. The theorem shows how and why a simple majority vote can outperform other decision methods under such conditions.

### 1.1  Two Very Different Problems  

| Preference Aggregation | Information Aggregation |
|---|---|
| People hold different tastes or values; no option is “objectively correct.” | Exactly one option is truly correct, but no one is completely sure which it is. |
| Goal: pick the option society most prefers. | Goal: identify the objectively correct option. |

**Example**  
- *Preference*: Where should a new leisure facility be built? People’s judgments differ because their interests differ.  
- *Information*: A lost child’s identity is either A or B. Each witness has noisy, independent clues; the group wants the truthful answer.

## 2. Standard Setting of the Theorem  

1. There are two alternatives, \(A\) and \(B\); exactly one is “true.”  
2. Each voter independently identifies the true option with probability \(p\), where \(p>½\).  
3. Votes are cast **independently** (no herding or copying).

### 2.1 Result  

Even if \(p\) exceeds \(½\) by only an epsilon, the probability that **simple majority rule** selects the correct alternative converges to 1 as the number of voters \(n\) goes to infinity.  
Statistics behind the theorem: with independent Bernoulli trials of success rate \(p>½\), the sample majority almost surely reflects the true state by the law of large numbers / central‑limit reasoning.

### 2.2 “Wisdom of Crowds”  

A large crowd of mildly informed amateurs can—under the independence assumption—beat a single expert with a higher individual accuracy. The power comes from information aggregation, not from any one voter’s brilliance.

### 2.3  Critical Assumption: Independence  

The theorem fails if voters merely echo each other. Copying another person’s guess double‑counts the same evidence, so information is not really “pooled.” Independent signals are essential.

---

# Young’s Method for More Than Two Alternatives

## 1. Why Two‑Alternative Logic Does Not Extend Directly  

With three or more options the notion of “the true choice” is subtler. In many practical cases:

* **The candidate set can vary** (spoiler problem).  
* Rather than one absolutely correct alternative, there may be a **true underlying order** of social desirability shared by everyone, obscured by noise.

We now ask: *Which voting rule maximizes the probability of recovering that true order?* The answer depends on how noise distorts individual rankings.

## 2. A Simple Noise Model and Young’s Proposal  

Assume:

* The **true ranking** of all options is most likely,  
* Rankings that deviate from it are possible, but their probability falls smoothly the more they deviate.

Under that model, the rule with greatest chance of returning the true order is the **Young Method**.

### 2.1  Intuitive Definition of the Young Method  

1. Each voter submits a complete ranking.  
2. For any societal ranking \(R\), count the **minimum number of voters whose ballots must be deleted** so that the remaining ballots are perfectly consistent with \(R\).  
3. Choose the ranking(s) that minimize this deletion number; the top candidate in that ranking is elected.

Interpretation: pick the order that requires the smallest “editing distance” to explain the electorate as nearly unanimous.

### 2.2  Properties  

* **Condorcet consistency**: if a Condorcet winner (pairwise undefeated option) exists, Young’s method always elects it.  
* **Computational cost**: finding the minimal deletion set is NP‑hard; the rule is conceptually elegant but harder to compute than scoring rules like Borda.

---

# Summary

* **Condorcet Jury Theorem**: with independent voters who are each slightly better than random (\(p>½\)), majority rule almost surely identifies the objectively correct alternative as the electorate grows.  
* The theorem highlights the power—and the limits—of **collective intelligence**; independence of signals is critical.  
* For **more than two options**, determining what “objective correctness” even means is tricky.  
* Under a simple noise model where one true ranking exists, the **Young Method** maximizes the probability of recovering that ranking and, interestingly, still satisfies Condorcet consistency—though at significant computational expense.

These results shift our view of voting from preference aggregation to information aggregation, illuminating when and why majority procedures can function as powerful inference machines.
### [📝 Take the mini-quiz here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5169782)

