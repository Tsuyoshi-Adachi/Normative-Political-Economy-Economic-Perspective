---
title: 26_intergenerational_equity_social_welfare_functions
---

## [📹 Watch the introductory video here](https://wsdmoodle.waseda.jp/mod/millvi/view.php?id=5062566)
# Intergenerational Equity and Social Welfare Functions

Contemporary macroeconomic policy discussions—especially in growth theory and public debt—must consider the welfare of different generations. To evaluate policies, we use a social welfare function (SWF). In this framework, we often focus on **welfare across generations** in equilibrium (rather than individual utilities per se), and these generations extend indefinitely. Consequently, the welfare distribution is an **infinite-dimensional** vector, which poses unique conceptual and mathematical challenges.

---

## 1. Social Welfare Function

A commonly used form of the social welfare function employs discounting:

$$
 W = \sum_{t=0}^{\infty} \beta^t u_t,
$$

where $u_t$ is the welfare of generation $t$, and $\beta$ $(0<\beta<1)$ is the social discount factor. In practical policy terms, this reflects the notion that distant future generations receive smaller weights (much like discounting future cash flows). However, the **normative** justification for such discounting can be controversial.

---

## 2. Monetary vs. Utility Discounting

1. **Monetary Discounting**  
   - Based on the risk-free interest rate.  
   - Converts future monetary values into their present equivalents.

2. **Utility Discounting**  
   - Reflects people’s tendency to value **current** welfare more than **future** welfare.  
   - Criticized for potentially **underweighting** the long-term welfare of future generations.  
   - Democratic politics often exhibits a bias toward current constituents, yet this is not the same as a purely normative principle.

---

## 3. Fair Treatment of Generations and the Pareto Principle

One might desire a function that treats all generations **symmetrically**, not favoring any particular generation. This approach mirrors the symmetry often imposed on individual-level social welfare functions (e.g., an Atkinson-type function). Yet, an infinite sequence of generational welfare levels reveals non-intuitive properties.

Consider the two sequences:

$$
\begin{cases}
(1,\tfrac12,\; 2,\; \tfrac13,\; 3,\; \tfrac14,\; 4,\; \tfrac15,\;5,\;\dots)\\
(2,\; 1,\; 3,\; \tfrac12,\; 4,\; \tfrac13,\; 5,\;\tfrac14,\; 4,\;\dots).
\end{cases}
$$

- The second sequence can be seen as a reordering (shifting) of the first, so if we insist on **complete symmetry**, we would consider them equally desirable.  
- However, from a **Pareto** standpoint, the second strictly improves each generation’s welfare over the first, suggesting it should be viewed as strictly better.

Thus, strictly adhering to symmetry across infinitely many generations **conflicts** with the Pareto principle. One must, in some sense, compromise between these two ideals.

---

## **4. ⭐️Advanced (Optional). No-Discount Social Welfare Function**

An alternative framework **without discounting** can be considered. One example is a social welfare function based on the *limit inferior* (“lim inf”) of the welfare sequence:

- If the welfare sequence $(u_t)$ **converges**, the social welfare score is simply its **limit**.  
- If $(u_t)$ **oscillates** or does not converge, then the social welfare score is the **lower limit** (i.e., $\liminf_{t\to\infty} u_t$).

### Implications
- A policy that **significantly reduces** the welfare of a finite number of current generations but **permanently improves** the welfare of all far-future generations would be **supported** under this lim inf criterion.  
  - In contrast, a discounted SWF might not endorse such a policy, since heavy costs in the near term can outweigh distant future gains once discounting is applied.  
  - This idea resonates with certain sustainable development goals (SDGs), which emphasize the well-being of distant future populations.
- In the **Solow model**, the *golden rule* level of capital (which maximizes steady-state consumption per capita) is supported only under such a criterion that does not discount future welfare. A discounted SWF might deviate from the golden rule because heavily distant generations contribute relatively little to the objective once discounting is considered.

This approach, therefore, reflects an extreme form of intertemporal equity, where distant future generations are given **equal priority** to present generations. Although conceptually appealing, it raises other technical and ethical debates in practical policy design.

---

## 5. A Strong—Though Controversial—Rationale for Discounting
One arguably consistent justification for discounting is the possibility that future generations might not exist at all. If there is a nonzero probability that society could collapse at each point in time, then the expected welfare of distant generations necessarily diminishes. From this perspective, discounting does not merely reflect a subjective preference for the present but an acknowledgment of existential risk.

---

## 6. Summary

- **Infinite-Horizon Considerations**: Social welfare functions must handle infinite-dimensional utility vectors. Discounting is common but subject to normative scrutiny.  
- **Symmetry vs. Pareto**: A fully symmetric treatment of all generations can conflict with the Pareto improvement principle, revealing a fundamental tension.  
- **No-Discount SWF (Optional)**:  
  - Using a “lim inf” approach places **no temporal discount** on future generations.  
  - Such a criterion can support policies that sacrifice current welfare for perpetual improvements in the far future.  
  - This perspective offers insight into sustainability and the golden rule in growth models.

By examining these approaches—discounted vs. non-discounted, symmetric vs. Pareto-oriented—we gain a deeper appreciation of the complexities in **intergenerational welfare analysis** and the policy trade-offs they entail.
### [📝 Take the mini-quiz here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5062833)
