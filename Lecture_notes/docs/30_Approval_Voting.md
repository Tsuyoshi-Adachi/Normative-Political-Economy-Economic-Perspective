---
title: "30_Approval_Voting"
---

## [📹 Watch the introductory video here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5169769)
## Approval Voting

### Introduction
In the previous session, we introduced the Borda Count, a well-known example of the **scoring rule** family. The Borda method can capture a broad range of voter preferences by asking voters to rank the candidates and assign points accordingly. However, it also has drawbacks, such as a heavy burden on voters when there are many candidates. **Approval Voting**, the focus of this session, has attracted attention as a voting system that allows **broader preference expression** than plurality voting while keeping the voting procedure as simple as possible. Let’s take a look at its definition and key characteristics.

---

## 1. Definition of Approval Voting
**Approval Voting** is a voting method where each voter casts a vote for every candidate they “approve” of (i.e., support). Specifically:

- If there are multiple candidates, voters mark all of the candidates they consider acceptable (they can select more than one).  
- During tallying, each candidate’s total “approvals” are counted, and the candidate with the **highest number of approval votes** wins.

In other words, unlike single-choice (plurality) voting—which restricts voters to choosing only **one** candidate—approval voting lets voters select **as many candidates as they wish**. At the same time, it does **not** require ranking or assigning point values, like the Borda method. Voters merely decide whether to approve each candidate or not, making both ballot marking and counting straightforward.

---

## 2. Strengths of Approval Voting

### 2.1 Simplicity and Low Implementation Cost
- **Compared to the Borda Count**  
  Under the Borda Count, each voter must **rank all candidates**, and this process becomes more demanding as the number of candidates grows.  
  In contrast, approval voting requires only **checking a box** for candidates one wishes to approve, minimizing administrative complexity and reducing the burden on voters.  
- **Implementation Cost**  
  Counting votes involves simply **tallying the number of approvals** each candidate receives. The design of ballots and the actual vote counting process are also uncomplicated, making approval voting relatively easy to implement even in large-scale elections.

### 2.2 Mitigating the Spoiler Effect
- **Voting for Multiple Candidates**  
  In plurality systems, when there are multiple similar candidates, votes can be split among them, inadvertently helping an opposing candidate win (the spoiler effect). Approval voting **alleviates** this problem to some degree because each voter can approve both similar candidates.  
- **Reason**  
  If multiple candidates have similar positions, a voter can approve all of them. This avoids splitting votes between those candidates and can help ensure that someone in that “political camp” or “ideological group” has a better chance of winning.

### 2.3 Straightforward Strategic Choices
- **Strategic Voting Is Not Completely Eliminated**  
  In approval voting, voters still must decide **how many** candidates to approve. A common dilemma might be: “Should I approve my favorite candidate plus a second-best compromise, or just my top choice?”  
- **No Need to “Lower a Candidate’s Rank”**  
  Under scoring rules (such as the Borda Count), voters can engage in complex manipulations like deliberately **lowering** their actual favorite’s rank and boosting another candidate. By contrast, approval voting offers only two options per candidate—approve or not.  
  - **Stability**: Because voters simply decide how many candidates to approve, large-scale blunders or regrets are less likely. Approval voting is thus sometimes seen as a relatively **stable** design, even if strategic voting occurs, because errors in the approval process are less damaging—voters are not forced to drop a favored candidate far down the order.  
  - This **simplicity** helps reduce confusion and unintentional negative consequences, one of the reasons approval voting is viewed as stable even in the face of strategy.

---

## 3. Weaknesses of Approval Voting

### 3.1 It Does Not Reflect Any Information Beyond “Approval”
Approval Voting operates on a simple yes-or-no metric. For instance:

- Suppose Candidate X barely receives approval from many voters, while other candidates do not.  
- X might still win with a slightly higher count of approvals, **even if a large number of voters strongly oppose X**.

Unlike the Borda Count, where voters can express nuanced preferences such as “Candidate A is my second choice, Candidate B is my third,” approval voting only distinguishes approved from not approved. It does not capture degrees of preference or levels of dislike. This could lead to situations where:

- A “universal second choice” candidate doesn’t get fully recognized, or  
- A candidate who is only modestly supported by a minority—but **deeply disliked** by the majority—could still emerge victorious if enough voters approve them.

---

## 4. Conclusion and Future Outlook

- **What Is Approval Voting?**  
  - A voting method where voters decide “approve or not” for each candidate, and the candidate with the most approvals wins.  
  - Unlike plurality voting, which restricts voters to a single choice, approval voting allows them to select multiple candidates, capturing broader voter preferences.

- **Strengths**  
  1. **Simplicity and Low Cost**  
     - No need to rank all candidates; voters only choose whether to approve each candidate.  
  2. **Reduced Spoiler Effect**  
     - If several candidates have similar platforms, a voter can approve them all, thus mitigating vote-splitting.  
  3. **Relatively Straightforward Strategic Decisions**  
     - Because the choice is merely whether to approve each candidate, large voting blunders or regrets are less likely.

- **Weaknesses**  
  - Fails to capture nuanced preference information—only yes/no data is collected.  
  - A candidate who is heavily disliked by many could still win if enough people approve them, neglecting the strength of that dislike.

Approval Voting has attracted interest among political reformers and institutional researchers because it imposes a **lower burden on voters** than the Borda Count while incorporating **more voter preference information** than simple plurality voting. Going forward, we will compare Approval Voting with methods like **Majority Judgment** to explore which situations each method may best serve, as well as their inherent limitations.
### [📝 Take the mini-quiz here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5169769)

