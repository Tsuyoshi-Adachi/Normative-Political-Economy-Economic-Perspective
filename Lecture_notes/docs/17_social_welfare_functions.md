---
title: 17_social_welfare_functions
---

## [📹 Watch the introductory video here](https://wsdmoodle.waseda.jp/mod/millvi/view.php?id=5062554)
# Social Welfare Functions

---

### Introduction
In previous discussions, we examined how economists estimate the distribution of welfare (or well-being) in equilibrium for various policy proposals, and then society chooses the most desirable policy based on those distributions. However, in reality, decisions about “which welfare distribution is desirable” are made concurrently with the policy review process. As society identifies issues with its current welfare distribution—such as concerns about efficiency or equity—economists propose new policy options and analyze their potential welfare impacts.

This framework, where society and economists collaborate through a division of labor, is central to what is called the **“social welfare function approach.”** To make this approach work, society needs to have a clear standard or criterion for what constitutes a desirable distribution of well-being. The formal theoretical device that captures this criterion is the **social welfare function**.

---

### Requirements for an Evaluation Criterion of Welfare Distributions

#### 1. Economics’ Stance on Value Judgments
Economics as a discipline does not prescribe which outcomes are intrinsically “better.” Rather, if society provides a value judgment—for example, “we want to prioritize equity over efficiency up to a certain point”—then economics can identify which policy would achieve that aim most effectively. Therefore, if society has no coherent stance on what kind of welfare distribution it prefers, economists cannot offer concrete policy prescriptions.

#### 2. Addressing Trade-Offs (Completeness)
Simply stating that “efficiency matters” or “equity matters” is too abstract. In practice, society must articulate how much equity it wants to improve and how much efficiency it is willing to sacrifice, or vice versa. To do this, the evaluation criterion must be able to compare any two possible welfare distributions:

> For any two distributions, can we say “Distribution A is preferable,” “Distribution B is preferable,” or “They are equally desirable”?

This property is known as **completeness**.

#### 3. Consistency (Transitivity)
Another critical requirement is **transitivity**. If society prefers (100, 50) over (60, 60), and prefers (60, 60) over (80, 55), it must not happen that society prefers (80, 55) over (100, 50). A violation of transitivity could lead to cyclical preferences, meaning that by sequentially adopting “better” policy options according to the stated criterion, society might eventually cycle back to the original distribution. This would undermine the premise that following society’s evaluation criterion leads to genuinely better outcomes.

---

### Definition and Representation of the Social Welfare Function
If a societal criterion for evaluating welfare distributions is **complete** and **transitive**, it can be represented by a **single numeric score** that assigns to each welfare distribution $\mathbf{u} = (u_1, u_2, \dots, u_n)$. That is, there exists some function $W(\mathbf{u})$ such that
$$
W(\mathbf{u}) > W(\mathbf{v}) \quad \Longleftrightarrow \quad \text{Society prefers } \mathbf{u} \text{ over } \mathbf{v}.
$$
This function $W$ is known as the **social welfare function**.

---

### Representative Examples

- **Utilitarian Criterion**  
  In utilitarianism, social welfare is the sum or average of individual welfare levels. Concretely, for $n$ individuals,
  $$
    W_{\text{util}}(u_1, u_2, \dots, u_n)
      = \frac{1}{n} \sum_{i=1}^n u_i
  $$
  or simply the total $\sum_{i=1}^n u_i$. Utilitarianism aims to maximize this aggregate or average.

- **Rawlsian Criterion**  
  Influenced by John Rawls’s theory of justice, this approach emphasizes improving the welfare of the least advantaged member of society:
  $$
    W_{\text{Rawls}}(u_1, u_2, \dots, u_n)
      = \min\{u_1, u_2, \dots, u_n\}.
  $$
  The goal here is to maximize the welfare of the worst-off individual.

These are two well-known benchmarks, but many other social welfare functions—representing various moral and philosophical perspectives—can be defined.

![eabf9855-36ba-489d-bf0e-2379e5ac2db7](https://hackmd.io/_uploads/HJnP6-Dh1e.gif)


---

## Utility Functions and Social Welfare Functions (For Those Who Have Completed Intermediate Microeconomics)

From intermediate microeconomics, we know that a **utility function** maps an individual’s consumption bundle to that individual’s level of utility. By analogy, a **social welfare function** maps a vector of individuals’ welfare levels $(u_1, u_2, \dots, u_n)$ to the overall “desirability” for society. 

- Hence, we can think of a social welfare function much like we think of a utility function, but at the societal level.  
- Just as utility functions can be represented with **indifference curves**, social welfare functions can be represented with **social indifference curves** (sometimes called **equal-welfare curves**).  
  - For a two-person society, we might plot $u_1$ on the horizontal axis and $u_2$ on the vertical axis. Points on the same “social indifference curve” indicate the same level of social welfare according to the chosen social welfare function.  
  - In a utilitarian function $W = (u_1 + u_2)/2$, these curves would be straight lines with a negative slope (reflecting constant sums).  
  - In a Rawlsian function $W = \min(u_1, u_2)$, the indifference curves resemble L-shaped contours, where both $u_1$ and $u_2$ must increase to raise the minimum.

This graphical approach provides insight analogous to that of utility analysis in microeconomics, helping us understand trade-offs between individuals’ welfare levels.

---

### The Social Welfare Function Approach: Its Significance
When the social evaluation criterion fulfills completeness and transitivity (and practically, **continuity**, as we will see below), it can be expressed as a **social welfare function**. Society can then choose which specific form of social welfare function to adopt—whether utilitarian, Rawlsian, or something in between. Economists, in turn, analyze which policy would maximize that function.

- Society supplies the value judgment (what is considered “desirable” in terms of welfare distribution).  
- Economists provide scientific analysis to compare policy options and identify which one yields the highest social welfare according to that value judgment.

This is the essence of the “social welfare function approach”: a division of labor where **society** clarifies its normative goals, and **economists** offer empirical and theoretical expertise on how to achieve those goals.

---

### Additional Note (Advanced)
Strictly speaking, representing society’s preference as a social welfare function also requires **continuity**. Informally:
- Given any three welfare vectors $w, w', w''$, if society prefers $w'$ to $w$, and prefers $w$ to $w''$, there should exist a point between $w'$ and $w''$ (e.g., $a\,w' + (1-a)\,w''$ for some $a \in (0,1)$) that society finds indifferent to $w$.  
- In other words, small changes in the welfare distribution should not cause erratic “jumps” in preference.  

A well-known mathematical result states that if a preference relation is **complete**, **transitive**, and **continuous**, then it can indeed be represented by a real-valued function, such as a social welfare function $W$. Continuity thus underpins the idea that we can model societal preferences as a single, smooth function of welfare levels.

---

### Summary
1. The social welfare function approach envisions a cooperative process between society and economists for policy selection.  
2. Society must provide a clear evaluation criterion for welfare distributions. Key requirements are:  
   - **Completeness**: Any two welfare distributions can be compared.  
   - **Transitivity**: Preferences do not cycle.  
   - (Additionally, **continuity** for a fully functional representation.)  
3. A criterion meeting these requirements can be numerically represented as a **social welfare function**.  
4. Various forms (e.g., **utilitarian** vs. **Rawlsian**) each reflect different ethical or philosophical judgments.  
5. Economists, using the chosen social welfare function, identify and propose policies that maximize it.

This system allows a clear division of labor between **value judgments** (society’s domain) and **scientific analysis** (economists’ domain), enabling society to choose more effectively among policy options based on its own normative perspectives.
### [📝 Take the mini-quiz here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5062859)
