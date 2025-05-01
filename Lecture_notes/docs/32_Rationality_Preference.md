---
title: "32_Rationality_Preference"
---

## [📹 Watch the introductory video here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5169766)

# Rationality and Preference

## 1. What Is a Comparison Criterion?

When we compare options (e.g., consumption plans, bundles of goods) in a set \(X\) and judge “which is more desirable” or “whether they are equally desirable,” the **collective outcome of all such judgments** is called a **comparison criterion**.

- Let \(X\) be the set of all possible options under consideration.  
  For example, suppose \(X = \{a, b, c, d, e\}\) consists of five options.

- Consider the following statement:
  
  > **One comparison criterion on \(X\): “\(a\) is more desirable than \(b\), \(b\) is more desirable than \(c\), \(c\) and \(d\) are equally desirable, and \(d\) is more desirable than \(e\).”**
  
  - This is a **concrete example of a single comparison criterion**.  
  - Note especially that multiple pairwise comparisons—“\(a\) is more desirable than \(b\),” “\(b\) is more desirable than \(c\),” “\(c\) is as desirable as \(d\),” “\(d\) is more desirable than \(e\)”—are **collectively referred to** as **one** comparison criterion.  
  - We denote this single criterion (the collection of pairwise comparison results) using the symbol \(\succsim\). In other words,  
    \[
      \text{everything within the above quotation marks} \;=\; \succsim.
    \]

In this way, we can regard “**one comparison criterion**” as a **‘single set’ that aggregates the outcomes of every pairwise comparison among the options in \(X\)**.

---

## 2. Preference

### 2.1 How \(\succsim\) Relates to \(\succ\) and \(\sim\)

As described in Section 1, \(\succsim\) denotes “the totality of pairwise comparisons among all options in \(X\) according to a certain criterion.” From this, we derive the following expressions:

- **\(a \succ b\)**  
  Means “\(a\) is strictly more desirable than \(b\).”  
  This holds when “\(a \succsim b\)” is true but “\(b \succsim a\)” is not.

- **\(a \sim b\)**  
  Means “\(a\) and \(b\) are equally desirable.”  
  This holds when both “\(a \succsim b\)” and “\(b \succsim a\)” are true.

Put differently, \(\succ\) and \(\sim\) are auxiliary notations that help distinguish whether “\(x\) is more desirable” or “\(x\) is equally desirable” based on judgments of the form \(\succsim\) (“\(x\) is at least as desirable as \(y\)” or not). You can think of them as analogous to “\(\geq\),” “\(>\),” and “\(=\)” in ordinary inequality notation.

Hence, comparing two options \(x\) and \(y\) using \(\succsim\) boils down to determining:
- whether \(x \succsim y\),
- whether \(y \succsim x\),

and from that, deciding whether \(x \succ y\), \(y \succ x\), or \(x \sim y\). This structure allows us to **consistently represent the desirability of one option over another**.

---

### 2.2 Completeness and Transitivity

In economics, a comparison criterion \(\succsim\) is called a **preference** if it satisfies the following **two conditions**:

1. **Completeness**  
   - For any two options \(x, y \in X\), either  
     \[
       x \succsim y \quad \text{or} \quad y \succsim x
     \]
     must hold.  
   - Interpretation: For any pair of alternatives, the person can determine whether one is more desirable or they are equally desirable.

2. **Transitivity**  
   - For any three options \(x, y, z \in X\),  
     \[
       x \succsim y \quad \text{and} \quad y \succsim z \quad \Longrightarrow \quad x \succsim z
     \]
     must hold.  
   - Interpretation: There are no “cycles” in the comparisons of desirability.  
   - For instance, it is not possible that “\(x\) is more desirable than \(y\),” “\(y\) is more desirable than \(z\),” but “\(z\) is more desirable than \(x\).”

When a comparison criterion \(\succsim\) satisfies **completeness** and **transitivity**, we call it a **preference**.

---

## 3. Rational Choice

### 3.1 Why Completeness and Transitivity Matter

In decision-making based on preferences, “to act rationally” means to make consistent choices in any situation according to a preference \(\succsim\). Here is why completeness and transitivity are important:

1. **Completeness**  
   - When a subset \(X' \subseteq X\) of feasible options is presented, completeness guarantees that in any pairwise comparison within \(X'\), one can always determine “which is better” (or that both are equally good).  
   - If completeness does not hold, there might be two options that cannot be compared, making it impossible to decide which one to choose.

2. **Transitivity**  
   - When there are three or more options, transitivity allows for an ordering of which option is more (or equally) desirable than which.  
   - If transitivity fails, you might get a cycle like “\(a \succ b\),” “\(b \succ c\),” yet “\(c \succ a\),” leading to inconsistent choices.  
   - For example, suppose \(X' = \{a, b, c\}\). If you have the cycle
     \[
       a \succ b,\quad b \succ c,\quad c \succ a,
     \]
     - In the two-option subset \(\{a, b\}\), you would “choose \(a\).”  
     - In \(\{b, c\}\), you would “choose \(b\).”  
     - In \(\{c, a\}\), you would “choose \(c\).”  
     This obviously creates a contradiction.  
     - Looking at the entire set \(\{a, b, c\}\), no matter which one you pick, there would be some other option that is supposedly “more desirable,” so rational choice breaks down.

### 3.2 Consistency Even if the Feasible Set Changes

- A decision-maker who has a complete and transitive preference \(\succsim\) can consistently choose “the most desirable option” from any subset \(X' \subseteq X\) based on the **same preference \(\succsim\)**.  
- Having a preference that is both complete and transitive makes it possible to make coherent choices in any context. In this sense, completeness and transitivity are considered the key requirements for “rationality.”

---

## 4. The Number of Preferences

### 4.1 The Case \(X = \{a, b, c\}\)

- Even when there are only three options, there are **13** possible preferences that satisfy completeness and transitivity (i.e., all pairwise comparisons are possible and contain no cycles).  
- Enumerating these 13 patterns, for example, yields:

  1. \(a \sim b \sim c\)  
  2. \(a \sim b \succ c\)  
  3. \(a \sim c \succ b\)  
  4. \(b \sim c \succ a\)  
  5. \(a \succ b \sim c\)  
  6. \(b \succ a \sim c\)  
  7. \(c \succ a \sim b\)  
  8. \(a \succ b \succ c\)  
  9. \(a \succ c \succ b\)  
  10. \(b \succ a \succ c\)  
  11. \(b \succ c \succ a\)  
  12. \(c \succ a \succ b\)  
  13. \(c \succ b \succ a\)

Each of these satisfies the criteria that for every pair \((x, y)\), either \(x \succsim y\) or \(y \succsim x\) holds, with no cycles arising.

### 4.2 The Case \(X = \{a, b, c, d\}\)

- When there are four options, the total number of preferences is **67**.  
- Though listing them all is lengthy, the idea is the same: they are all the ways to arrange a complete and transitive relationship among four elements.

---

## Summary

- A **comparison criterion** \(\succsim\) is the collective set of pairwise judgments such as “\(a \succ b\)” or “\(c \sim d\).”  
- A comparison criterion that satisfies **completeness** and **transitivity** is called a **preference**, a core concept in economics for modeling rational decision-making.  
- Thanks to completeness and transitivity, a decision-maker can make consistent choices from any subset of options. These properties are thus key to “rationality.”  
- The number of possible preferences grows rapidly with the number of options. For instance,  
  - there are **13** when \(X = \{a,b,c\}\)  
  - there are **67** when \(X = \{a,b,c,d\}\).  

These ideas about “rationality and preference” form the basis for what we will study next, including **utility representation** and various applied analyses.
### [📝 Take the mini-quiz here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5169766)

