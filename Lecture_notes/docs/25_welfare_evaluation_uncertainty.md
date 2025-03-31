---
title: 25_welfare_evaluation_uncertainty
---

## [📹 Watch the introductory video here](https://wsdmoodle.waseda.jp/mod/millvi/view.php?id=5062565)
# Welfare Evaluation under Uncertainty

### 1. Uncertainty and Welfare Distribution
In real-world policy decisions, it is extremely difficult to predict exactly how a policy will affect each individual’s well-being. For instance, even if we try to forecast who will benefit from Policy A and who will lose, both theoretical and empirical predictions are often accompanied by uncertainty. Consequently, we have no choice but to rely on probabilistic information—e.g., “Policy A yields outcome X with some probability \(p\), and outcome Y with probability \(1-p\).”

However, this probabilistic information itself may be imperfect and not necessarily shared by all members of society. Despite these challenges, let us first assume that there is a consensus on the relevant probability distribution of outcomes (i.e., a known risk). We will then consider how to evaluate social welfare under this assumption. Afterward, we will explore scenarios in which the probability distribution itself is uncertain (i.e., subjective and potentially disagreeable among individuals).

---

### 2. Two Approaches to the Social Welfare Function
When the outcome of a policy is random, there are two major ways to incorporate probability into social welfare evaluations:

1. **Ex-ante Approach (Expected Individual Welfare):**  
   Each individual’s welfare is replaced by its expected value before applying the social welfare function. Formally, if \(u_i\) denotes person \(i\)’s (random) welfare, then in this approach we compute
   \[
     W\bigl(E[u_1], E[u_2], \dots, E[u_N]\bigr),
   \]
   where \(E[u_i]\) is the expected welfare of individual \(i\), and \(W(\cdot)\) is the social welfare function.

2. **Ex-post Approach (Expected Value of the Social Welfare):**  
   We apply the social welfare function to each possible outcome of the random welfare vector and then take the expectation. Formally,
   \[
     E\bigl[ W(u_1, u_2, \dots, u_N) \bigr].
   \]
   In other words, we first consider the social welfare in each possible realized state, and then average these values over the probability distribution of outcomes.

Although both methods incorporate uncertainty, **they can yield different policy evaluations** depending on the nature of the social welfare function, especially when the function is sensitive to the distribution of welfare among individuals (e.g., Rawlsian social welfare).

---

### 3. Example: Ex-post vs. Ex-ante (Rawlsian Case)
Consider a simple example with two individuals (labeled 1 and 2) and two policies, A and B:

- **Policy A**:  
  - There are two possible outcomes, \((0,10)\) and \((10,0)\), each with 50% probability.  
- **Policy B**:  
  - There is only one outcome, \((3,3)\), with 100% probability.

Let us use a **Rawlsian social welfare function** defined by
\[
  W(u_1, u_2) = \min\{u_1, u_2\}.
\]

#### 3.1 Ex-post Approach (Expected Social Welfare)
1. **Policy A**:  
   \[
     0.5 \times \min\{0, 10\} \;+\; 0.5 \times \min\{10, 0\} 
     = 0.5 \times 0 + 0.5 \times 0 = 0.
   \]
2. **Policy B**:  
   \[
     \min\{3, 3\} = 3.
   \]
Thus, the expected ex-post Rawlsian welfare is
\[
  E[W(u)]_A = 0, 
  \quad
  E[W(u)]_B = 3.
\]
By this criterion, **Policy B** is strictly preferred.

#### 3.2 Ex-ante Approach (Social Welfare of Expected Welfare)
1. **Policy A**:  
   - Individual 1’s expected welfare is \(0.5 \times 0 + 0.5 \times 10 = 5\).  
   - Individual 2’s expected welfare is also 5.  
   - Thus, the welfare vector in expectation is \((5,5)\). Applying the Rawlsian function,
     \[
       \min\{5, 5\} = 5.
     \]
2. **Policy B**:  
   - Both individuals have welfare of 3 for sure, so the expected welfare for each is 3.
     \[
       \min\{3, 3\} = 3.
     \]
Hence, **under the ex-ante approach**, we get
\[
  W_A = 5, \quad W_B = 3,
\]
so **Policy A** is strictly preferred.

#### 3.3 Summary of the Discrepancy
- **Ex-post (Expected Score of the Social Welfare)** emphasizes “how poorly off the worst-off person is in each realized outcome,” and then averages that over the possible states.
- **Ex-ante (Social Welfare of Expected Outcomes)** emphasizes “how poorly off the worst-off person is in terms of expected welfare,” effectively smoothing over states before identifying the worst-off.

As shown, for a **Rawlsian** (maximin) social welfare function, the policy ranking can differ significantly between these two methods. By contrast, when the social welfare function is **utilitarian**, i.e. \(W(u_1, u_2) = u_1 + u_2\), the two approaches yield the same ranking because the expectation of sums is the sum of expectations.

---

### 4. When Probabilities Are Unknown
Up to now, we have assumed that everyone agrees on the probability distribution (e.g., a 50% chance of \((0,10)\) or \((10,0)\) under Policy A). In reality, however, people may disagree on those probabilities. Indeed, there might be no universally accepted data or model to pin them down.

Suppose:

- There are two individuals (1 and 2).
- **Policy A** could yield welfare \((0,10)\) or \((10,0)\), but the probabilities are uncertain.
- **Policy B** yields a certain outcome of \((8,8)\).

Imagine that:

- Individual 1 strongly believes that \((10,0)\) will happen under Policy A.
- Individual 2 strongly believes that \((0,10)\) will happen under Policy A.

These two beliefs may be **objectively inconsistent**—they can’t both be correct at the same time—yet:

- Individual 1 sees a high chance of getting 10 under Policy A and thus prefers A to \((8,8)\).
- Individual 2 sees a high chance of getting 10 under Policy A and likewise prefers A to \((8,8)\).

Both would then favor Policy A over B, even though their probability assessments are mutually contradictory from a purely objective standpoint.

---

### 5. Handling Differences in Subjective Probabilities
When the probability distribution itself is uncertain or contested, there are at least two possible ways to proceed:

1. **Aim for Agreement on Probabilities First**  
   - Try to unify the available information so that all members of society come to share the same probability model.  
   - Then, proceed with social welfare evaluation (either ex-ante or ex-post, Rawlsian or utilitarian, etc.).

2. **Accept Divergent Subjective Beliefs**  
   - Allow each individual to hold different probability judgments and let them evaluate policy based on their own subjective probabilities.  
   - This may result in paradoxical outcomes—for example, everyone “prefers” a policy that cannot realistically favor them all at once.

In the second case, one might ask, “Why do they hold such favorable beliefs for themselves, and should society respect them?” But in the first case, “How do we create a rational or objective consensus on probabilities when real-world data are incomplete or contested?” Both paths present practical and philosophical challenges.

---

### 6. Conclusion and Next Steps
In evaluating social welfare under uncertainty, key points include:

1. **Ex-ante (expected welfare) vs. Ex-post (expected social welfare)** can produce different policy rankings, particularly for inequality-averse social welfare functions like Rawlsian.  
2. **Utilitarian** social welfare is the unique case (under certain symmetry conditions) for which ex-ante and ex-post evaluations coincide.  
3. When probabilities themselves are unknown, subjective probability differences can lead to paradoxical collective decisions, hinting at deeper issues of belief and information sharing.  

From here, further exploration might involve distinguishing between **risk** (known probabilities) and **true uncertainty** (unknown probabilities), investigating decision-making principles such as **maximin**, **minimax regret**, or **Bayesian** approaches, and considering how society might reach an agreement on models of uncertainty or whether it should respect divergent beliefs.
### [📝 Take the mini-quiz here](https://wsdmoodle.waseda.jp/mod/quiz/view.php?id=5062832)
