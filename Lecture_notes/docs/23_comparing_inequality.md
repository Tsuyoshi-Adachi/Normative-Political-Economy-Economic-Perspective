---
title: 23_comparing_inequality
---

## [📹 Watch the introductory video here](https://wsdmoodle.waseda.jp/mod/millvi/view.php?id=5062563)
# Comparing Inequality

### Gini Coefficient

#### Lorenz Dominance and the Need for a Scalar Measure
As discussed previously, if there is no intersection between two Lorenz curves (i.e., one curve is always above the other), we can conclude that one distribution is unequivocally more equal than the other. This situation is referred to as **Lorenz dominance**. However, **when the Lorenz curves intersect**, there is no straightforward way to compare the degree of inequality between the two distributions. Hence, while Lorenz dominance avoids value conflicts in those cases where comparison is possible, it also leaves many cases **unresolved**.

To deal with this limitation, we often use a **single scalar index** derived from the Lorenz curve called the **Gini coefficient**. This allows us to compare inequality even when the Lorenz curves intersect, by providing a single numerical value that summarizes the shape of the distribution.

#### Definition of the Gini Coefficient
The Gini coefficient $ G $ is defined using the area between the Lorenz curve and the line of perfect equality (the 45-degree line). Specifically,

$$
G = 1 - 2 \times (\text{area under the Lorenz curve}),
$$

where:
- The horizontal axis represents the cumulative proportion of the population (from 0 to 1).
- The vertical axis represents the cumulative proportion of income (also from 0 to 1).

For discrete individual-level or household-level data, there are established formulas to calculate this area (or directly compute the Gini coefficient).

#### Intuitive Interpretation
- $ G = 0 $ means perfect equality (everyone has the same income).  
- $ G $ closer to 1 means near-perfect inequality (one person holds virtually all the income).  
- In real-world contexts, the Gini coefficient rarely goes below 20%, and once it exceeds 40%, it is often considered a signal of serious inequality.

#### “Average Income $\times$ Gini Coefficient” Interpretation
An important interpretation of the Gini coefficient is:
> “Average Income $\times$ Gini Coefficient” = “Average of the absolute income differences between all possible pairs of individuals.”

In other words, the Gini coefficient indicates **what percent of the mean income** corresponds to the expected income gap between two randomly chosen individuals in the society.

#### International Comparisons
Because the Gini coefficient distills inequality into a single number, it is a convenient tool for comparing different countries or different time periods. For example:
- If Country A’s Gini is 30% and Country B’s Gini is 25%, we can say that Country A has higher income inequality.  
- Caution is required regarding data definitions (pre-tax vs. post-tax income, how data is collected, etc.) when making these comparisons.

**[Imagine here a chart comparing Gini coefficients across various countries.]**

---

### Different Types of Distributions

When discussing inequality, we may focus on several types of income or wealth measures. Each has different implications:

1. **Disposable Income (Post-Redistribution Income)**
   - Income after taxes and social security benefits.  
   - The Lorenz curve or Gini coefficient for this distribution reflects the actual inequality people face in terms of their take-home pay.  
   - Comparing this distribution’s inequality with other distributions reveals how effective a society’s redistribution policies are in reducing inequality.

2. **Pre-Redistribution Income**
   - Income before taxes and social security transfers.  
   - By comparing the Lorenz curve or Gini coefficient of pre-redistribution income with that of disposable income, one can gauge the extent to which public policy redistributes income.  
   - This helps in discussions about the cost and extent of redistribution in a society.

3. **Wealth Distribution**
   - Wealth data is often more skewed and more difficult to capture accurately than income data.  
   - Wealth distribution typically shows greater inequality. Wealth is also considered to represent the “current status” of inequality more directly, while income might reflect longer-term tendencies or labor market status.  
   - Arguments exist that accumulated capital or wealth is the fundamental source of inequality. (See, for example, Piketty’s work on capital and inequality.)  
   - **[Imagine a chart or Lorenz curve for wealth distribution here.]**

---

## Summary
- **Lorenz dominance** can cleanly determine which of two distributions is more equal, but only when their Lorenz curves do not intersect.  
- **The Gini coefficient** is a widely used scalar index of inequality that allows for comparison even when Lorenz curves intersect. It represents “the expected income gap as a percentage of mean income” for two randomly selected individuals.  
- Typically, a Gini coefficient below 20% is very rare, and above 40% is considered indicative of a serious social problem in terms of inequality.  
- The choice of distribution (disposable income, pre-redistribution income, or wealth) affects both the numerical results and the policy implications. Disposable income focuses on immediate conditions, while wealth distribution highlights accumulated inequality.
### [📝 Take the mini-quiz here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5062830)
