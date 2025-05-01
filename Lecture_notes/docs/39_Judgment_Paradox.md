---
title: "39_Judgment_Paradox"
---

## [📹 Watch the introductory video here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5169781)
# Judgment Paradox

## 1. Step‑by‑Step Agreements in Collective Decision‑Making

So far we have focused on voting schemes that choose **an option directly**—for example, which policy, which candidate, which arm of an experiment.  In many real‑world settings, however, a group first reaches agreement on **facts or logical premises** and then, on the basis of those premises, derives a final conclusion.

*Examples*

* **Criminal trials.** A jury must first decide whether certain facts are true— *Was the defendant at the scene?* *Did the act satisfy the statutory requirements?*—before it can reach a verdict of guilty or not‑guilty.  
* **Public‑policy design.** Before choosing a policy, a committee may have to settle which values to prioritise, which data to trust, how to measure success, and so on.

A natural hope is that step‑by‑step voting might avoid the paradoxes we met earlier.  Unfortunately that hope is ill‑founded, as the **Judgment (or Doctrinal) Paradox** shows.

---

## 2. The Judgment (Doctrinal) Paradox

### 2.1 Basic set‑up **with a numerical example**

Consider three yes/no propositions and three jurors:

* **A:** “The defendant was at the crime scene.”  
* **B:** “Anyone at the scene was a party to the crime.”  
* **C:** “The defendant is guilty.”  –– By law, **C** is true exactly when **A ∧ B** is true.

|           | Vote on A | Vote on B | Individual conclusion C (= A ∧ B) |
|-----------|:---------:|:---------:|:----------------------------------:|
| Juror 1   | **Yes**   | **Yes**   | **Yes** |
| Juror 2   | **Yes**   | **No**    | **No**  |
| Juror 3   | **No**    | **Yes**   | **No**  |

*Each juror is internally consistent:* she accepts **C** exactly when she accepts both **A** and **B**.

Now compare two aggregation procedures:

| Aggregation step | Majority on A | Majority on B | ⇒ Legal conclusion C | Direct majority on C |
|------------------|---------------|---------------|----------------------|----------------------|
| Vote totals      | 2 Yes – 1 No  | 2 Yes – 1 No  | **Yes** (guilty)     | 1 Yes – 2 No → **No** (not‑guilty) |

> **Contradiction:**  The group majority affirms both premises **A** and **B**, yet by a separate majority votes that the defendant is *not* guilty.

In short, majority voting on each individual proposition can yield a *logically inconsistent* collective outcome.  This is the core of the **Judgment Paradox**.

### 2.2 Why does it arise?

* Individual ballots are **coherent**, but collective majorities are computed **issue‑by‑issue**.  
* Logical consistency is **not preserved** when the winning coalitions for different propositions overlap in conflicting ways.  
* The phenomenon mirrors Condorcet cycles (A ≻ B, B ≻ C, C ≻ A) in preference aggregation, but in a propositional rather than ordinal setting.

### 2.3 No voting rule can guarantee global consistency

Even though each judgment is a binary choice, any rule that aggregates them independently is liable to such contradictions.  Impossibility theorems in *judgment aggregation* show that we cannot simultaneously satisfy (i) proposition‑wise majority, (ii) collective rationality, and (iii) a handful of mild fairness axioms.

---

## 3. A Broader View of Voting Paradoxes

### 3.1 From preference cycles to propositional inconsistency

Condorcet’s voting paradox and the judgment paradox are two faces of the same **coherence problem**:

* **Preference aggregation:** majority comparisons A ≻ B, B ≻ C, C ≻ A violate transitivity.  
* **Judgment aggregation:** majority truth‑values violate logical entailment.

### 3.2 Can clever voting rules fix the problem?

Clever design helps in special cases (single‑peaked preferences, Median Voter Rule, etc.), but **no purely mechanical voting rule** dissolves every paradox.  Some dilemmas stem from the very task of converting many minds into one consistent “group mind.”

---

# **Section III Wrap‑Up: Why Voting Alone Cannot Settle Value‑Judgments**

* **Majority rule is not inherently “best.”** Depending on the context, more “democratic” or more “fair” rules can be devised—and some problems defeat **every** rule.  
* **Voting is no magic wand.** Relying reflexively on majority vote (or any automatic procedure) may obscure deeper issues of evidence, values, or deliberation.  
* **Practical implication:**  recognise the limits of formal aggregation; combine voting with expert input, dialogue, and critical reflection.

> **Bottom line:**  Collective choice is hard not because we lack the *right* voting formula, but because consistency, fairness, and truth are often mutually at odds.  Understanding those limits is the first step toward wiser collective decisions.

---

### [📝 Take the mini-quiz here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5169781)

