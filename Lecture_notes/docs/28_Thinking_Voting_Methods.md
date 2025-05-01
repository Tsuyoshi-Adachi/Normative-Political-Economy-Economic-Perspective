---
title: "28_Thinking_Voting_Methods"
---

## [📹 Watch the introductory video here](https://wsdmoodle.waseda.jp/mod/millvi/view.php?id=5062828)
## Thinking About Voting Methods

### Introduction
When we hear the word “voting” in our daily lives, many of us probably assume the “plurality voting” method (also known as single-choice voting). In other words, we choose exactly one candidate we prefer among multiple candidates. However, in reality, there are numerous proposals for what are considered democratic voting methods, and the single-choice (plurality) method is just one of them.

For a comparison of election methods, [this Wikipedia page](https://en.wikipedia.org/wiki/Comparison_of_voting_rules) provides a detailed list. Even just skimming through the variety of methods listed there can give you a sense of how diverse “voting mechanisms” can be. In upcoming lectures, we will focus on some of the most commonly discussed methods—such as the Borda count, Approval Voting, and Majority Judgment—and examine their characteristics and evaluations in detail.

---

### Goals of This Session
In this session, we will focus on the problems inherent in the plurality voting system. Interestingly, research and surveys by experts in this field often conclude that **“plurality voting is not particularly desirable”**. There is even a specialist survey paper titled “*And the Loser Is…Plurality Voting*,” which illustrates the strong criticism directed toward this method. What exactly are its issues? Let’s look at some representative problems.

---

## Problems with Plurality Voting

### 1. Vulnerability to the Spoiler Effect
One well-known problem with plurality voting is the so-called “spoiler effect.”

- **What kind of situation is this?**  
  Consider an election where candidates A and B are in a close race, and a new candidate C—whose positions are similar to A—enters the race. Votes for A might get siphoned off to C, splitting support between A and C, which relatively benefits B.  
- **Why is this a problem?**  
  Supporters of A and C might agree on at least one point: “We don’t want B to win.” But because voters can only choose one candidate in a plurality system, their support splits, and there is a higher risk of inadvertently helping B win.  
- **Distortion of democratic intent**  
  Even if voters’ true preference would be “either A or C is acceptable, as long as it prevents B from winning,” the spoiler effect can lead to B’s victory. This is known as the **spoiler effect** and is often cited as a major weakness of plurality voting.

---

### 2. Failure to Respond to Information Beyond First Choice
Plurality voting only incorporates information about which candidate each voter ranks as their top choice. It does not consider second-place or lower rankings at all. This can lead to serious paradoxes, such as:

- **A candidate who would lose in a head-to-head matchup against every other candidate can still win.**  
  Suppose there is a candidate X who is so unpopular that “X would lose in a head-to-head contest against every other candidate.” If X nevertheless receives strong first-place support from a certain group of passionate voters, X can win under plurality rules.  
  - A candidate who would be defeated in a direct contest with any other candidate is known as a **Condorcet loser**. Under plurality voting, such a candidate can paradoxically be elected.  

- **A candidate widely disliked by many voters can still win.**  
  It may happen that a candidate is the top choice for some group of people (gaining first-place votes) while being deemed “the worst possible choice” by the majority. Because no information about second or lower preferences is considered, the fact that **“many people strongly dislike this candidate”** is never reflected in the vote count.

---

### 3. Intense Strategic Voting
Plurality voting is also criticized for easily inducing **strategic voting**.

- **What is strategic voting?**  
  It refers to voting not for “the candidate you truly like best,” but rather for “a candidate who has a real chance of winning and is still acceptable to you,” in order to prevent the worst outcome. If your ideal candidate has little chance of winning, you might shift your vote to a more viable candidate to defeat one you strongly oppose.

- **Example: A, B, and C**  
  Suppose you most prefer candidate C, but polling suggests C has a very low chance of winning. Also suppose you really don’t want candidate B to win.  
  In this situation, you might think, “Voting for C would be a wasted vote, so I should vote for A instead to stop B from winning.” This is often referred to as voting for the “lesser evil,” but it is essentially an example of strategic voting.

- **Instability**  
  The outcome of strategic voting heavily depends on polls and predictions of how others will vote. If the perception of “which candidate is most likely to win” changes even slightly, voters might massively shift their votes. This can make the results quite unstable. Moreover, if the prediction turns out to be incorrect, some voters may end up regretting their choices—“I should have voted for A after all…”—raising concerns that the final outcome does not accurately reflect the voters’ true preferences.

---

## Appropriate for Less Critical Decisions
A frequently cited advantage of plurality voting is its **low implementation cost**. Voters simply choose a single candidate, so the voting instructions, ballot marking, and vote counting are all extremely straightforward.

- **“Plurality voting is best suited for decisions that don’t matter much”**  
  In decisions of relatively low social importance (or situations where strategic voting or spoiler effects are not catastrophic), the simplicity of plurality voting can actually be a benefit. One expert has even sarcastically suggested that we should use plurality voting **only for decisions of lower importance**.

---

### Voting Methods in the IT Age
With the advance of online voting and automated tabulation systems, complex voting methods are not as costly as they once were. Nevertheless, plurality voting remains widely used in many elections and decision-making situations, largely due to its familiarity and simplicity.

- **Is it difficult to move away from plurality voting?**  
  Introducing new voting methods requires public education, institutional change, and sometimes legal revisions, which can involve substantial social and political hurdles.  
- **A compromise: Runoff Voting**  
  One relatively simple method that can mitigate some of plurality voting’s flaws is **runoff voting**. By holding an initial vote, identifying the top two candidates, and then conducting a final runoff, spoiler and strategic-voting issues can be reduced to some extent. However, the cost of holding a second round of voting remains a drawback.

---

## Conclusion and What’s Next
- **Summary**  
  Plurality voting suffers from issues such as the spoiler effect, ignoring secondary (and lower) preferences, and encouraging strategic voting. Despite these problems, it remains widespread, in part because it is simple, easy to understand, low-cost to implement, and historically entrenched.  
- **Looking ahead**  
  In the upcoming sessions, we will explore other well-known voting methods—Borda count, approval voting, majority judgment, and more—and discuss their potential advantages and disadvantages. By learning about alternative counting rules, you will gain deeper insights into the complexities of voting methods and the fascinating field of social choice theory.
### [📝 Take the mini-quiz here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5062835)

