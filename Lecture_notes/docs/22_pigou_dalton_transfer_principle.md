---
title: 22_pigou_dalton_transfer_principle
---

# Pigou-Dalton Transfer Principle

### Comparison with the Pareto Principle
Previously, we discussed the Pareto Principle, which states that if a change makes at least one person better off without making anyone else worse off, that change is considered more efficient. This principle is appealing because, despite being an ethical or philosophical concept, when it does apply, it is usually accepted intuitively by almost everyone. However, the Pareto Principle cannot compare many real-world situations (its comparisons are often “incomplete,” leaving many cases “unranked”).

Similarly, judging whether one state of income distribution is “more equal” than another often involves deep value judgments that differ among people. Yet even here, there is a limited set of changes for which almost everyone would agree that one distribution is “more equal” than another. **Pigou-Dalton Transfer Principle** formalizes this idea for those intuitively agreeable cases.

---

## Formalizing the Pigou-Dalton Transfer Principle

### Pigou-Dalton Transfer
- **Basic idea of the transfer**: Take a small amount of income (e.g., 1 unit) from someone with higher income and transfer it to someone with lower income, under the condition that after the transfer, the donor still has a higher income than the recipient.
- **Intuition**: Such a transfer does not satisfy the Pareto condition because someone’s income decreases. However, it is often viewed as leading to a “more equal” distribution, in a way that many people find intuitively acceptable.

### The Transfer Principle
- **Repeated Pigou-Dalton transfers**: If one can reach a new distribution from the original distribution by applying a sequence of these small transfers from higher-income individuals to lower-income individuals, the new distribution is deemed “less unequal” (i.e., “more equal” in some sense).  
- The key is that **everyone tends to agree** that repeated applications of such transfers move us toward a distribution with smaller inequality. This provides a way to compare certain distributions without invoking deeper, more contentious value judgments.

### Limitations and Incompleteness
- Like the Pareto Principle, the Pigou-Dalton Transfer Principle cannot rank all possible distributions. Many pairs of distributions cannot be transformed from one to the other purely by the repeated application of these small transfers. In those cases, there is no definitive statement on “which distribution is more equal.”  
- **Example**: If distributions A and B cannot be transformed into one another through any sequence of Pigou-Dalton transfers, then the principle offers no conclusion about their relative equality (an incomplete ranking).

---

## Lorenz Curve and the Pigou-Dalton Transfer

### Visualizing the Lorenz Curve: Stacked Bars
In the previous session, we introduced the **Lorenz Curve**, which plots cumulative population share on the x-axis and cumulative income share on the y-axis. One intuitive way to view it is through a series of “stacked bar” images:
1. Place the bar representing the lowest-income individual across all positions along the horizontal axis.
2. Then stack the bar for the second-lowest-income individual from the second position onward.
3. Continue in this manner for the third, fourth, fifth, and so on, until everyone’s bars are stacked in a cumulative way.  
By connecting the heights of these cumulative bars, you get the Lorenz Curve.  

![1bf9552c-d620-4d79-90ae-d6bf75861f27](https://hackmd.io/_uploads/rkC3fzvn1g.gif)


### How a Pigou-Dalton Transfer Affects the Lorenz Curve
- **Example**: Suppose we have five individuals. We take 1 unit of income from the 4th richest person and give it to the 3rd richest, ensuring the 4th person is still wealthier than the 3rd.  
  - The cumulative income for persons 1 and 2 remains unchanged.  
  - The 3rd person’s income goes up by 1 unit, so at the “3rd person’s position,” the cumulative share in the Lorenz curve increases.  
  - For the 4th person, even though their income decreases by 1, the Lorenz curve’s overall shape from the 3rd person onward shifts upward because the 3rd person’s share is now greater at that earlier point.  
- The **key**: Even if total income is unchanged, moving some portion of that income to a lower-income individual pushes the Lorenz curve “upward” in the cumulative sense, leading to a new curve that may “dominate” the original one.

![69045c2d-b51e-4b91-a210-330cb297cfae](https://hackmd.io/_uploads/H1QCfzvhye.gif)


### Repeated Transfers
Repeating Pigou-Dalton transfers moves more income shares to lower-income individuals step by step. Each such step causes the Lorenz curve to shift upward in the lower segments, resulting in a distribution that, by this principle, is considered less unequal. Over multiple transfers, if we can go from one distribution to another in such a manner, there is a **dominance relation** between the corresponding Lorenz curves.

---

## Relationship Between Lorenz Dominance and the Pigou-Dalton Transfer Principle

- **From Lorenz dominance to Pigou-Dalton transfers**  
  If two distributions (with the same population and the same mean income) satisfy Lorenz dominance—i.e., one distribution’s Lorenz curve lies entirely above the other—then one can transform the dominated distribution into the dominating one through a sequence of Pigou-Dalton transfers.
- **From Pigou-Dalton transfers to Lorenz dominance**  
  Conversely, if you can reach distribution B from distribution A by repeated Pigou-Dalton transfers, then the Lorenz curve for A must lie on or below the Lorenz curve for B at all points.

Because these two perspectives are equivalent, we say **Pigou-Dalton Transfer Principle and Lorenz dominance are essentially the same**. This equivalence justifies why the Lorenz Curve is so central in studies of inequality: it visually and analytically encodes exactly those changes we can all intuitively agree make a distribution “more equal.”

---

## Conclusion
- The **Pigou-Dalton Transfer Principle** parallels the Pareto Principle by focusing on a subset of changes that are broadly acceptable—here in terms of reduced inequality rather than increased efficiency.  
- Although it cannot provide a complete ranking among all distributions, it does conclusively rank those pairs where one can reach the other by repeated small transfers from higher- to lower-income individuals (without reversing their income order).  
- **Lorenz curves** illustrate these changes in a cumulative fashion, and any clear dominance in Lorenz curves corresponds directly to the existence of a sequence of Pigou-Dalton transfers.  
- Hence, Lorenz dominance is not just a convenient graphical tool; it reflects a deeper theoretical rationale—namely the Pigou-Dalton Transfer Principle—that highlights a universal form of “inequality reduction” most observers accept without significant dispute.