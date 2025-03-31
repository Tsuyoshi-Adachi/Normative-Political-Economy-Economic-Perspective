---
title: 11_informational_content_welfare_measures
---

# The Informational Content of Welfare Measures

## 1. Surplus and Real Income as Welfare Measures

- Until now, we have used **surplus** and **real income** as welfare measures.  
  - **Surplus**: Combines measures like consumer surplus and producer surplus for a particular good.  
    - It can relatively reliably capture each individual’s **change in welfare**, yet it does not inform us of the **total** welfare level.  
    - Moreover, if the price system or the overall market context changes significantly, the absolute level of surplus might become less meaningful.  
  - **Real income**: Potentially reflects an individual’s overall welfare level.  
    - It can be viewed as a candidate for measuring the **total** amount of welfare, but might be less precise than surplus when it comes to changes in welfare under certain assumptions.

- In normative analysis, obtaining a truly **perfect** welfare measure is difficult.  
  - Estimating the total level of welfare requires many assumptions, and even measuring changes in welfare can be uncertain depending on the context.  
- However, even a **partially reliable** welfare measure, if we properly identify which feature of it is reliable, can support policy evaluation to some extent.  
- In this lecture, we explicitly consider **how much information about welfare comparisons** we have, and then explore which types of normative judgments become possible.

---

## 2. Interval Interpersonal Comparability

### 2-1. Each Individual’s Welfare Change Measured in a Common Unit

- Suppose we know, for each policy relative to the baseline, how much an individual’s welfare changes, and that these changes are **additive** and **comparable** across individuals in the same unit.
  - Example: “Under Policy A, Individual 1’s welfare changes by +2, Individual 2’s by +3, and Individual 3’s by -1.”
- In this situation, the **sum of welfare changes** is meaningful: whichever policy yields the largest sum of changes is considered to yield the highest total welfare.

#### Example: Baseline and Changes

| Individual | Baseline Welfare (Unknown) | Policy A Change | Policy B Change | Policy C Change |
|:---------:|:--------------------------:|:---------------:|:---------------:|:---------------:|
| 1         | x (unknown)               | +2              | +0              | +3              |
| 2         | x (unknown)               | +3              | +2              | +2              |
| 3         | x (unknown)               | -1              | +1              |  0              |
| **Sum of Changes** |          –           | +4              | +3              | +5              |

- We do not know the baseline welfare level $ x $, but we assume we **can** measure everyone’s changes in a common unit.
  - Thus, the policy with the largest sum of changes (Policy C, sum = +5) is considered the one that maximizes **total welfare**.

### 2-2. Using Surplus for Policy Evaluation

- A common approach—**maximizing total surplus**—implicitly relies on this concept of comparing welfare changes in a uniform way.
  - Surplus is treated as a reasonably accurate representation of changes in welfare, aggregated across the individuals in a particular market.
  - In reality, if the price system or an individual’s broader consumption/income set changes dramatically, the absolute level of surplus might be questionable.  
  - Even so, if **relative** changes in surplus are considered trustworthy, then finding the policy that **maximizes total surplus** is equivalent to maximizing **total welfare**.

---

## 3. Order Interpersonal Comparability

### 3-1. A Numerical Example

Next, we consider a case where the **differences** (or “changes”) in welfare have no reliable quantitative meaning, but we do know **who is better off or worse off** (an ordinal ranking). 

The table below shows how three individuals would fare under Policies A, B, and C. Each value is higher if welfare is higher, but **differences** (e.g., “4 minus 1 = 3”) cannot be interpreted as “3 units of welfare improvement.” We only use the **ranking**.

| Individual | Welfare under A | Welfare under B | Welfare under C |
|:----------:|:--------------:|:--------------:|:--------------:|
| **1**      |       1        |       2        |       0        |
| **2**      |       2        |       2        |       3        |
| **3**      |       4        |       2        |       3        |

- Individual 1: 1 (A), 2 (B), 0 (C\) 
- Individual 2: 2 (A), 2 (B), 3 (C\) 
- Individual 3: 4 (A), 2 (B), 3 (C\) 

We only treat these numbers as showing that a larger value corresponds to a higher level of welfare.

### 3-2. Why Summation (Total) Lacks Meaning

- For instance, adding up the welfare values for Policy A gives “1 + 2 + 4 = 7,” but calling “7” the total welfare is **unjustified**.  
  - We cannot say “Individual 3’s welfare is 4, which is 3 points higher than Individual 1’s 1” in a cardinal sense. We only know “4 is better than 1,” not “4 is exactly 3 more units than 1.”

### 3-3. What Can We Still Evaluate?

Although we cannot rely on sums or other cardinal operations, we **can** look at which position (worst-off, median, etc.) individuals occupy under each policy.

#### (1) Rawlsian (Maximin) Criterion

- **Rawlsian criterion**: A policy is better if it improves the welfare of the **worst-off** person as much as possible.
- Under each policy, identify the worst-off person’s welfare:
  - Policy A: $$1, 2, 4$$ → **Worst-off = 1**  
  - Policy B: $$2, 2, 2$$ → **Worst-off = 2**  
  - Policy C: $$0, 3, 3$$ → **Worst-off = 0**  

Since the highest worst-off value is 2 (Policy B), **the Rawlsian criterion selects Policy B** as the best.

#### (2) Median Criterion

- **Median**: For three individuals, the median is the second-lowest (or second-highest) value once sorted.
  - Policy A: (1, 2, 4) → Median = 2  
  - Policy B: (2, 2, 2) → Median = 2  
  - Policy C: (0, 3, 3) → Median = 3  

Since the highest median is 3 (Policy C), **the median criterion selects Policy C** as the best.

#### (3) Why the Different Conclusions?

- Rawlsian (maximin) approach → **Policy B** is best.  
- Median approach → **Policy C** is best.  

This discrepancy arises because each criterion focuses on a different part of the distribution (worst-off, median, etc.). Even without cardinal information, **choosing how to evaluate** the distribution of welfare matters greatly.

---

## 4. Summary and Future Developments

- The degree of **confidence** in a welfare measure depends on **how** we can compare welfare across individuals:
  1. **Interval Interpersonal Comparability**: When changes are measured in a common unit, summation is valid → leads to **total surplus** reasoning.  
  2. **Order Interpersonal Comparability**: When only the ranking is reliable (not the magnitude of differences), we can still use frameworks like the **Rawlsian criterion** or **median-based evaluations**.

- In practical policy analysis, exact measurement of welfare is often challenging, and analysts typically have partial information. Thus, combining the pieces of welfare information we do trust—and choosing an appropriate criterion—becomes crucial.  
- In subsequent lectures, we will explore Rawlsian reasoning in more depth, discuss how it connects with fairness, and examine voting-based approaches such as **majority judgment**, showing how each method can shape policy choices differently.