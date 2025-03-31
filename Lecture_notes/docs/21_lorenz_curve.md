---
title: 21_lorenz_curve
---

## [📹 Watch the introductory video here](https://wsdmoodle.waseda.jp/mod/millvi/view.php?id=5062558)
# **The Lorenz Curve**

---

## 1. Introduction
When examining the distribution of income (or wealth), one important way to assess the degree of inequality is by using the **Lorenz curve**. The Lorenz curve goes beyond simple statistics like the mean or variance by visually illustrating the shape of the distribution and providing deeper insight into inequality. Specifically, it helps us:

- Identify which segments of the distribution experience the greatest inequality.  
- Compare different distributions to see which is relatively more (or less) equal.  
- Determine whether there is a clear dominance relationship (Lorenz dominance) between two distributions or if additional social preferences are needed to decide which is more equal.

In these lecture notes, we will introduce the definition and shape of the Lorenz curve, then discuss how to use it to compare multiple distributions. We will pay particular attention to **Lorenz dominance**, **single-crossing**, and cases where the curve “dips” in the middle—situations that complicate any straightforward ranking of inequality.

---

## 2. Definition of the Lorenz Curve
The Lorenz curve represents the relationship between the **cumulative population share** and the **cumulative income share** when individuals (or households) are ordered from the lowest to the highest income. Formally:

1. **Order individuals (households) by ascending income.**  
2. **Horizontal axis (X-axis):** The cumulative share of the population, ranging from 0 to 1 (or 0% to 100%).  
3. **Vertical axis (Y-axis):** The cumulative share of total income, calculated for the group up to each point on the X-axis.

For example, if at the 0.50 mark on the horizontal axis (the bottom 50% of the population), the vertical axis reads 0.20, this means **the bottom 50% earn only 20% of total income**.  
In a perfectly equal distribution, every segment of the population would get a proportional share of total income, so the Lorenz curve would match the diagonal line (the so-called **line of perfect equality**). Any deviation from that diagonal indicates some level of inequality.

![download](https://hackmd.io/_uploads/ry-S-fP3ye.png)

---

## 3. Shape of the Lorenz Curve
1. **Line of Perfect Equality**  
   - In a perfectly equal distribution, the Lorenz curve coincides with the diagonal line from the origin (0,0) to (1,1). At each point along that line, the cumulative population share equals the cumulative income share.

2. **Real-World Convexity (Bowing Downward)**  
   - In practice, because higher-income individuals are towards the upper end of the distribution, cumulative income tends to rise more sharply in the later portion of the distribution. This causes the Lorenz curve to bend below the diagonal and be **convex** (bowed downward toward the X-axis).

The farther the Lorenz curve lies from the diagonal, the greater the inequality; the closer it is to the diagonal, the more equal the distribution.


---

## 4. Interpreting Inequality with the Lorenz Curve
The Lorenz curve is a powerful visual tool for comparing two or more income distributions. We can often see if one distribution is unequivocally more equal than another or if we need further analysis. Below, we discuss key scenarios: **Lorenz dominance**, **single crossing**, and cases where the curve “dips” in the middle.

### 4-1. Lorenz Dominance
**Definition:**  
Suppose there are two distributions, A and B. If the Lorenz curve for distribution A lies **entirely above** that of distribution B over the entire 0–1 range (i.e., they do not intersect), then we say **“A Lorenz-dominates B.”** Intuitively, this means that for every cumulative share of the population (from the poorest up to a given point), distribution A grants a greater share of total income than B does.

- When A Lorenz-dominates B, most standard inequality measures (such as the Gini coefficient) would identify A as more equal.  
- Consequently, if we observe Lorenz dominance, we can confidently conclude that A has **less inequality** than B.  
- The reverse situation, where B dominates A, would imply B is strictly more equal than A.

### 4-2. Single-Crossing Distributions
In reality, it is common for two Lorenz curves to intersect **exactly once**. Let’s consider distributions A and B again, and suppose their Lorenz curves intersect at one point. For instance:

- **In the lower portion of the distribution (say, up to 30% of the population),** A’s Lorenz curve is above B’s, suggesting that the bottom groups in distribution A receive a higher cumulative share of total income. Thus, for that segment, A seems **more equal**.  
- **However, beyond that intersection point (say, in the 30–100% range),** B’s Lorenz curve might be above A’s, indicating that from the middle to the top income groups, B is more equal.

In other words, **A is more equal with respect to the poorest segment**, while **B appears more equal among higher segments**. Because of these **mixed outcomes**, there is no universal way to say which distribution is “better” or “more equal” without specifying additional **social value judgments** (such as placing greater weight on the well-being of the poorest). When a single crossing occurs, **Lorenz dominance does not hold**, and the assessment of which distribution is more equal depends on your chosen criteria.

### 4-3. A “Dip” in the Middle (More Complex Crossings)
A more complex scenario arises when the Lorenz curves intersect multiple times or when one distribution’s Lorenz curve **“dips” significantly** around the middle. This can happen if the distribution is:

- **Bimodal:** concentrated at both low- and high-income levels, with a thinner middle class, or  
- **Heavily skewed:** in various ways that create multiple points of intersection.

For example, if distribution A has a **thin middle class** but substantial low- and high-income groups, the Lorenz curve may drop more around the 40–60% mark. If distribution B has a heavier middle class and fewer low- or high-income individuals, its Lorenz curve could appear relatively higher in the middle. In such cases:

- There might be multiple crossing points where A is above B in one range, then B is above A in another, and so on.  
- The question “Which distribution is more equal?” may change depending on whether you focus on low-, middle-, or high-income segments.  
- Again, **no single, definitive ordering** emerges unless we impose additional normative judgments on which part of the distribution matters most.

![download](https://hackmd.io/_uploads/H1HFZMPnJl.png)

---

## 5. Conclusion
The Lorenz curve is an essential tool in measuring and comparing income inequality:

1. **Lorenz Dominance:**  
   - If one distribution’s Lorenz curve is entirely above another’s (no intersections), we say it dominates the other. This implies the dominating distribution is **more equal** for most standard measures of inequality.

2. **Single Crossing:**  
   - When two Lorenz curves intersect exactly once, distribution A may appear more equal in one segment (e.g., the poorest portion), while distribution B appears more equal elsewhere (e.g., middle or upper income).  
   - **A universal ranking is impossible** without additional assumptions about which part of the distribution you care about most.

3. **Dips in the Middle & Multiple Crossings:**  
   - Some distributions have complex shapes (e.g., large shares in very low and very high income brackets but a “hollow” middle). Their Lorenz curves may intersect multiple times, further complicating comparisons.  
   - In these scenarios, deciding which distribution is more equal depends heavily on **social preferences**—for example, whether you prioritize supporting the bottom deciles, the middle class, or reducing top-end income concentration.

In summary, Lorenz curves provide a **visual and intuitive** way to examine how incomes are shared across a population, highlighting not only the overall level of inequality but also which segments of the population are most affected. However, if there is no clear Lorenz dominance, additional value judgments regarding different income segments become necessary. Studying these nuances and understanding the structure of distributions is a fundamental part of welfare economics.
### [📝 Take the mini-quiz here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5062855)
