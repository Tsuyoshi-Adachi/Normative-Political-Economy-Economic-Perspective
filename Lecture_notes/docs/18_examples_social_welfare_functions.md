---
title: 18_examples_social_welfare_functions
---

## [📹 Watch the introductory video here](https://wsdmoodle.waseda.jp/mod/millvi/view.php?id=5062555)
# Examples of Social Welfare Functions

## 1. Atkinson-Type Social Welfare Function

### 1.1 Definition and Inequality Aversion
The Atkinson-type social welfare function (Atkinson’s Social Welfare Function) often takes the following form. Let $x_i$ denote the welfare level of individual $i$, and let there be $n$ individuals in total. The parameter $\epsilon$ represents the degree of inequality aversion:



$$
W_{\epsilon}(x_1, x_2, \ldots, x_n) = \begin{cases}
\left(\frac{1}{n} \sum_{i=1}^n x_i^{\,1-\epsilon}\right)^{\frac{1}{\,1-\epsilon}}\quad (\epsilon \neq 1),\\
\left(\prod_{i=1}^n x_i\right)^{\frac{1}{n}} \quad (\epsilon = 1). 
\end{cases}
$$

- When $\epsilon = 0$, this reduces to the simple average $\left(\tfrac{1}{n}\sum x_i\right)$, aligning with a **utilitarian** social welfare function (i.e., maximizing total welfare).  
- As $\epsilon \to \infty$, the function approaches the **Rawlsian** social welfare function, focusing on maximizing the minimum welfare level (Max–Min criterion).  
- A larger $\epsilon$ places greater weight on those with lower welfare levels, thus reflecting a stronger aversion to inequality.

![91a7f739-3e32-4404-a760-af4c7311dba1](https://hackmd.io/_uploads/BJJeJfP3kx.gif)


### 1.2 Scale Invariance
A key property of the Atkinson-type social welfare function is **scale invariance**: if all welfare levels $x_i$ are scaled by the same positive factor (e.g., multiplied by 100 or by 1/1000), the ranking of different policy outcomes or distributions remains unchanged.

- In other words, the choice of a policy is unaffected by whether welfare is measured in, say, monthly income or annual income, as long as all individuals’ measures are scaled equally.  
- Mathematically, it can be shown that any social welfare criterion that treats all individuals symmetrically and is invariant to uniform scaling of all welfare levels must be representable by an Atkinson-type function for some $\epsilon$.

#### Significance
Because the evaluation does not depend on absolute levels of welfare but rather on relative differences or distributional shape, this framework is highly practical for policymaking. It allows flexibility in the units used for welfare measurement without altering conclusions.

### 1.3 Relationship to Utilitarianism
For $\epsilon = 0$, the Atkinson function is simply the arithmetic mean $\left(\tfrac{1}{n}\sum x_i\right)$, which coincides with the classical utilitarian focus on maximizing total (or average) welfare.

### 1.4 Relationship to the Rawlsian Criterion
As $\epsilon$ becomes very large, the Atkinson function places increased emphasis on the individual(s) with the lowest welfare level. In the limit, it converges to the Rawlsian Max–Min rule (maximizing the minimum welfare).

---

## 2. Nash-Type Social Welfare Function

### 2.1 Definition and Main Characteristics
When $\epsilon = 1$, the Atkinson-type social welfare function is called the **Nash-type social welfare function**. It takes the form

$$
W_{1}(x_1, x_2, \ldots, x_n) 
= \left(\prod_{i=1}^n x_i\right)^{\frac{1}{n}},
$$

which is the **geometric mean** of the individual welfare levels. Equivalently, taking logarithms yields a sum of logs: $\sum_{i=1}^n \log x_i$. This is why it is also referred to as the “log-sum criterion.”

### 2.2 Individual Scale Invariance
The Nash-type function ($\epsilon = 1$) exhibits not only invariance to uniformly scaling everyone’s welfare levels, but also a form of invariance when scaling only one person’s welfare by a positive factor. In essence, even if each individual’s “1 unit” of welfare could differ in meaning, as long as zero is a common baseline, the overall ranking of outcomes remains consistent under the Nash-type function.

- This property is significant when we suspect that different individuals perceive or measure welfare in different subjective scales, but we still share a common notion of “the worst possible value is 0.”

---

## Optional Section: Proof of Individual Scale Invariance

**Proposition**  
For any $x, y, i,$ and $c$ $(c>0)$, if  
$W_{\text{Nash}}(x_1,x_2,\dots,x_n) \ge W_{\text{Nash}}(y_1,y_2,\dots,y_n)$,  
then  
$W_{\text{Nash}}(x_1,x_2,\dots,c \cdot x_i,\dots,x_n) \ge W_{\text{Nash}}(y_1,y_2,\dots,c \cdot y_i,\dots,y_n)$.

**Proof**  

1. The inequality $W_{\text{Nash}}(x_1,x_2,\dots,x_n) \ge W_{\text{Nash}}(y_1,y_2,\dots,y_n)$ means

   $$
   \prod_{j=1}^n x_j \;\;\ge\;\; \prod_{j=1}^n y_j.
   $$

2. Next, consider multiplying the $i$-th component by a positive constant $c$. Then

   $$
   W_{\text{Nash}}(x_1,x_2,\dots, c\cdot x_i,\dots,x_n)
   = c \cdot x_i \prod_{j \neq i} x_j
   = c \cdot \prod_{j=1}^n x_j,
   $$
   and similarly,  
   $$
   W_{\text{Nash}}(y_1,y_2,\dots, c\cdot y_i,\dots,y_n)
   = c \cdot \prod_{j=1}^n y_j.
   $$

3. Because $c>0$, multiplying each side of an inequality by $c$ does not change its direction. Therefore,

   $$
   c \cdot \prod_{j=1}^n x_j 
   \;\;\ge\;\; 
   c \cdot \prod_{j=1}^n y_j,
   $$

   holds. Hence,

   $$
   W_{\text{Nash}}(x_1,x_2,\dots, c\cdot x_i,\dots,x_n)
   \;\;\ge\;\;
   W_{\text{Nash}}(y_1,y_2,\dots, c\cdot y_i,\dots,y_n).
   $$

This completes the proof.

---

### 2.3 Example: Subjective Well-Being Applications
- In subjective well-being surveys, we might agree that 0 is the worst possible state, yet the meaning of a score of 50 may vary across individuals.  
- Even if these individual scales are not strictly comparable, the **Nash-type social welfare function** (i.e., $\sum \log x_i$ or the geometric mean) allows us to make consistent welfare comparisons, provided that “0” is shared as a baseline.

### 2.4 Applications to the Human Development Index (HDI), etc.
When combining multiple indicators—such as life expectancy, education, and income—into a single index, it can be difficult to unify their scales precisely.  
- A Nash-type approach, i.e., taking the **geometric mean**, helps mitigate arbitrariness arising from different units of measurement.  
- The **Human Development Index (HDI)** by the United Nations, for instance, aggregates three indices (life expectancy, education, income) via a geometric mean, thus penalizing any extremely low component. This reflects a feature akin to the Nash-type emphasis on balancing all dimensions—no dimension can be near-zero without drastically lowering the overall index.

---

## 3. Summary

1. **Atkinson-Type Social Welfare Function**  
   - Exhibits scale invariance, meaning that if all welfare levels are multiplied by the same factor, the ranking of policy options remains the same.  
   - By adjusting the inequality aversion parameter $\epsilon$, one can span from a utilitarian criterion ($\epsilon=0$) to a Rawlsian criterion ($\epsilon \to \infty$).

2. **Nash-Type Social Welfare Function** ($\epsilon = 1$)  
   - Uses the geometric mean of welfare levels (or equivalently, the sum of logarithms).  
   - Ensures that even if only one individual’s welfare is rescaled by a positive factor, the ordinal evaluation of policies remains consistent—provided that zero is a shared baseline.  
   - Stands as the unique social welfare criterion that maintains this individual-level scale invariance while treating individuals symmetrically.

3. These properties are particularly relevant for **subjective well-being surveys** (where “0” is recognized as the worst case but individual scales may vary) and for **composite indices** of multiple, potentially incommensurable indicators (e.g., the HDI), where taking the geometric mean controls for extreme disparities.

### [📝 Take the mini-quiz here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5062858)
