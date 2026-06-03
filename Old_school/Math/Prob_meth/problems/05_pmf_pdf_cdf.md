# Task List 05 — PMF, PDF, and CDF

## Introduction

This task list is technical in character. Its purpose is not primarily to introduce new probabilistic models, but to train the student in the practical and formal use of probability distributions through their standard representations.

Students should learn how to:

- read and interpret a probability law given in tabular, symbolic, or graphical form,
- move fluently between a probability mass or density function and the corresponding cumulative distribution function,
- understand how the parameters of a family of distributions change the shape of its graph,
- compute probabilities using either PMF/PDF formulas or the CDF,
- interpret distributions in terms of real applications,
- and use computational tools to visualize and compare distributions.

In each task, before working with the PMF, PDF, or CDF, first identify:

- the underlying random experiment,
- the sample space $\Omega$,
- the form of an elementary outcome $\omega$,
- the random variable $X$,
- and the support of $X$.

Do not confuse the sample space $\Omega$ with the support of $X$. The sample space consists of elementary outcomes of the experiment, while the support consists of values taken by the random variable.

The emphasis in this list is on **formal technique** and **graphical understanding**.
For that reason, many tasks require plotting several graphs for the same family under different parameter choices, comparing their shapes, and explaining what changes and what remains invariant.

Whenever a distribution has important practical uses, students should also identify and briefly describe some of those applications.

If possible, students are encouraged to prepare a small application, for example in HTML/JavaScript, Python, or another suitable environment, that allows the user to:

- choose a distribution,
- modify its parameters,
- display the corresponding PMF/PDF and CDF,
- and compare values of probabilities for different parameter choices.

The aim is to become technically comfortable with the formal structures used in probability theory.

---

## Task 1 — Discrete Distribution Given by a PMF Table

Consider a discrete random variable $X$ whose probability law is given directly in a table of values.

Assume that the PMF is given by the following table:

| $x$ | -2 | 0 | 1 | 3 | 5 |
| --- | --- | --- | --- | --- | --- |
| $P(X=x)$ | 0.10 | 0.25 | 0.30 | 0.20 | 0.15 |

### Tasks

0. Construct one possible finite probability space $\Omega$ and define a random variable $X$ on $\Omega$ whose PMF is the one given in the table.
1. Verify whether the listed probabilities form a valid probability distribution.
2. Draw the graph of the **probability mass function**.
3. Construct the **cumulative distribution function** $F(x)$.
4. Draw the graph of the CDF.
5. Explain how the jumps of the CDF are related to the values of the PMF.
6. Compute several probabilities using the table, for example:
   - $P(X = a)$,
   - $P(X \le a)$,
   - $P(X < a)$,
   - $P(a < X \le b)$,
   - $P(X \ge a)$.
7. Compare the results obtained directly from the PMF with those read from the CDF.
8. If possible, implement this distribution in a small application and allow the user to inspect the PMF and CDF interactively.

---

## Task 2 — Discrete Distribution Given by a CDF Table

Consider a discrete random variable $X$ whose cumulative distribution function is given in tabular form.

Assume that the CDF is described by the following values:

| $x$ | -1 | 0 | 2 | 4 | 6 |
| --- | --- | --- | --- | --- | --- |
| $F(x)$ | 0.15 | 0.35 | 0.60 | 0.85 | 1.00 |

### Tasks

0. Construct one possible finite probability space $\Omega$ and define a random variable $X$ on $\Omega$ whose CDF is the one given in the table.
1. Reconstruct the PMF from the jumps of the CDF.
2. Draw the graph of the PMF.
3. Redraw the CDF carefully, emphasizing its stepwise character.
4. Identify all points at which the CDF jumps.
5. Explain why the jump size at a point equals the probability of that value.
6. Compute several probabilities using the CDF, for example:
   - $P(X \le a)$,
   - $P(X < a)$,
   - $P(X = a)$,
   - $P(a < X \le b)$,
   - $P(X > a)$.
7. Compare this task with Task 1 and explain what information is immediate from the PMF and what information is immediate from the CDF.
8. If possible, extend the application from Task 1 so that it also accepts input in CDF form.

---

## Task 3 — Binomial Distribution $Bin(n,p)$

Recall that the Bernoulli distribution is the special case $Bin(1,p)$.

### Tasks

0. Model the experiment as $n$ Bernoulli trials. Describe the experiment, specify the sample space $\Omega$, describe one elementary outcome $\omega$, and define $X(\omega)$ as the number of successes.
1. Write the PMF of the binomial distribution.
2. Identify its support.
3. Draw PMF graphs for several choices of parameters, for example:
   - fixed $n$, different values of $p$,
   - fixed $p$, different values of $n$.
4. Draw the corresponding CDF graphs for the same parameter choices.
5. Explain how the shape changes when:
   - $p$ increases,
   - $n$ increases.
6. Compute probabilities such as:
   - $P(X = k)$,
   - $P(X \le k)$,
   - $P(X \ge k)$,
   - $P(a \le X \le b)$.
7. Compute some probabilities directly from the PMF and some using the CDF.
8. Find and briefly describe practical applications of the binomial model.
9. If possible, include this family in the application and allow comparison of two parameter choices on the same plot.

---

## Task 4 — Geometric Distribution

### Tasks

0. Describe the experiment of repeated trials until the first success, specify the sample space $\Omega$, describe one elementary outcome $\omega$, and define $X(\omega)$ as the trial on which the first success occurs.
1. Write the PMF and CDF of the geometric distribution.
2. Identify the support and explain why it is infinite.
3. Draw PMF graphs for several values of the parameter $p$.
4. Draw CDF graphs for the same values of $p$.
5. Explain how the graphs change as $p$ becomes larger or smaller.
6. Compute probabilities such as:
   - $P(X = k)$,
   - $P(X \le k)$,
   - $P(X > k)$,
   - $P(a \le X \le b)$.
7. Interpret the tail probabilities in the context of waiting time.
8. Find and briefly describe practical applications of the geometric model.
9. If possible, add this family to the comparison application.

---

## Task 5 — Poisson Distribution

### Tasks

0. Propose an experiment in which random events occur in a fixed interval, specify a natural sample space $\Omega$, describe one elementary outcome $\omega$, and define $X(\omega)$ as the number of events in the interval.
1. Write the PMF of the Poisson distribution and identify its parameter.
2. Describe its support.
3. Draw PMF graphs for several values of $\lambda$.
4. Draw the corresponding CDF graphs.
5. Explain how the shape changes when $\lambda$ increases.
6. Compute probabilities such as:
   - $P(X = k)$,
   - $P(X \le k)$,
   - $P(X \ge k)$,
   - $P(a \le X \le b)$.
7. Use the CDF to compute cumulative probabilities and compare with direct summation from the PMF.
8. Find and briefly describe practical applications of the Poisson model.
9. If possible, include a slider for $\lambda$ in the application and compare several curves.

---

## Task 6 — Hypergeometric Distribution

### Tasks

0. Describe the experiment of sampling without replacement, specify the sample space $\Omega$, describe one elementary outcome $\omega$, and define $X(\omega)$ as the number of distinguished objects in the sample.
1. Write the PMF of the hypergeometric distribution and explain its parameters.
2. Identify the support.
3. Draw PMF graphs for several parameter choices.
4. Draw the corresponding CDF graphs.
5. Explain how the distribution changes when:
   - the sample size changes,
   - the number of distinguished objects in the population changes.
6. Compute probabilities such as:
   - $P(X = k)$,
   - $P(X \le k)$,
   - $P(X \ge k)$,
   - $P(a \le X \le b)$.
7. Compare this model conceptually with the binomial model.
8. Find and briefly describe practical applications of the hypergeometric model.
9. If possible, include this family in the application and compare it with a binomial distribution having similar parameters.

---

## Task 7 — Negative Binomial Distribution

### Tasks

0. Describe the experiment of repeated trials until the $r$-th success, specify the sample space $\Omega$, describe one elementary outcome $\omega$, and define $X(\omega)$ as the trial on which the $r$-th success occurs.
1. Write the PMF of the negative binomial distribution and explain its parameters.
2. Identify the support.
3. Draw PMF graphs for several values of the parameters.
4. Draw the corresponding CDF graphs.
5. Explain how changing the success probability and the target number of successes changes the distribution.
6. Compute probabilities such as:
   - $P(X = k)$,
   - $P(X \le k)$,
   - $P(X > k)$,
   - $P(a \le X \le b)$.
7. Explain how this distribution generalizes the geometric distribution.
8. Find and briefly describe practical applications of the negative binomial model.
9. If possible, include this family in the application and compare it with the geometric distribution.

---

## Task 8 — Beta Distribution

### Tasks

0. Consider a continuous experiment on $[0,1]$. Specify a simple sample space $\Omega = [0,1]$, describe one elementary outcome $\omega$, and define $X(\omega)=\omega$.
1. Write the PDF of the beta distribution and identify its parameters.
2. Identify its support.
3. Draw PDF graphs for several parameter choices, for example cases where:
   - the density is symmetric,
   - the density is skewed to the left,
   - the density is skewed to the right,
   - the density is concentrated near the endpoints.
4. Draw the corresponding CDF graphs.
5. Explain how the parameters influence the shape of the density and the growth of the CDF.
6. Compute probabilities such as:
   - $P(X \le a)$,
   - $P(X \ge a)$,
   - $P(a \le X \le b)$,
   using the CDF or numerical tools where needed.
7. Explain why probabilities for continuous distributions are computed from areas under the PDF.
8. Find and briefly describe practical applications of the beta distribution.
9. If possible, implement parameter sliders for this family in the application.

---

## Task 9 — Gamma Distribution

Note that the chi-square distribution is a special case of the gamma family.

### Tasks

0. Propose a continuous waiting-time experiment, specify a simple sample space $\Omega = [0,\infty)$, describe one elementary outcome $\omega$, and define $X(\omega)=\omega$ as the waiting time.
1. Write the PDF of the gamma distribution and identify its parameters.
2. Identify its support.
3. Draw PDF graphs for several parameter choices.
4. Draw the corresponding CDF graphs.
5. Explain how the shape changes as the parameters vary.
6. Show explicitly how the chi-square distribution appears as a special case.
7. Compute probabilities such as:
   - $P(X \le a)$,
   - $P(X \ge a)$,
   - $P(a \le X \le b)$,
   using the CDF or numerical tools where needed.
8. Find and briefly describe practical applications of the gamma distribution and of the chi-square distribution.
9. If possible, include this family in the application and allow comparison with the chi-square case.

---

## Task 10 — Normal Distribution $N(\mu,\sigma^2)$

### Tasks

0. Propose a continuous measurement experiment, specify a simple sample space $\Omega = \mathbb{R}$, describe one elementary outcome $\omega$, and define $X(\omega)=\omega$ as the measured value.
1. Write the PDF of the normal distribution and identify its parameters.
2. Identify its support.
3. Draw PDF graphs for several parameter choices:
   - fixed variance, changing mean,
   - fixed mean, changing variance.
4. Draw the corresponding CDF graphs.
5. Explain how $\mu$ and $\sigma^2$ influence location and spread.
6. Compute probabilities such as:
   - $P(X \le a)$,
   - $P(X \ge a)$,
   - $P(a \le X \le b)$,
   using the CDF or standardization where appropriate.
7. Explain why $P(X=a)=0$ for a continuous distribution.
8. Find and briefly describe practical applications of the normal distribution.
9. If possible, include this family in the application and allow comparison of several normal curves on one plot.

---

## Final Technical Project — Optional Distribution Visualizer

If possible, prepare a small application that allows the user to explore the distributions from this list.

### Minimum functionality

1. The user can choose one of the distributions from the list.
2. The user can enter or modify its parameters.
3. The application displays the corresponding PMF or PDF.
4. The application displays the corresponding CDF.
5. The application allows comparison of at least two parameter choices on the same graph.
6. The application allows the user to compute selected probabilities numerically.

### Recommended extensions

1. Display the support of the distribution clearly.
2. Highlight the interval corresponding to a probability such as $P(a \le X \le b)$.
3. Allow switching between exact formulas and numerical approximations where relevant.
4. Include short notes about typical applications of the selected distribution.
