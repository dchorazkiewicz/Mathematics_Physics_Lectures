# Problem Set 8 – Statistics and measurements

---

## Problem 1 – Descriptive statistics of a measurement series

Given are the measurements of a rod's length (in cm):

$$
x = [12.10,\ 12.08,\ 12.12,\ 12.11,\ 12.09,\ 12.13,\ 12.07,\ 12.10]
$$

1. Calculate the arithmetic mean $\bar{x}$.
2. Calculate the sample variance and standard deviation $s$.
3. Calculate the uncertainty of the mean:

   $$
   u(\bar{x}) = \frac{s}{\sqrt{n}}
   $$

4. Provide the result in the format:

   $$
   x = \bar{x} \pm u(\bar{x})
   $$

5. Explain the difference between the standard deviation $s$ and the uncertainty of the mean $u(\bar{x})$.
6. Assuming a normal distribution, calculate the intervals:
      - $\bar{x} \pm s$
   - $\bar{x} \pm 2s$
   - $\bar{x} \pm 3s$
   
   and interpret them as confidence levels (68–95–99).

---

## Problem 2 – Propagation of uncertainty using the total differential method (resistance from Ohm's law)

Resistance is determined from voltage and current measurements:

$$
R = \frac{U}{I}
$$

Data:

$$
U = 5.23 \pm 0.04\ \mathrm{V}
$$

$$
I = 0.482 \pm 0.006\ \mathrm{A}
$$

1. Calculate the value of the resistance $R$.
2. Derive the formula for relative uncertainty using the total differential method.
3. Calculate the relative uncertainty $\frac{u(R)}{R}$ and indicate which measurement (U or I) dominates the uncertainty.

---

## Problem 3 – Propagation of uncertainty (density)

Density of a rectangular cuboid:

$$
\rho = \frac{m}{abc}
$$

Data:

$$
m = 128.4 \pm 0.2\ \mathrm{g}
$$

$$
a = 5.20 \pm 0.02\ \mathrm{cm}
$$

$$
b = 2.10 \pm 0.02\ \mathrm{cm}
$$

$$
c = 1.50 \pm 0.01\ \mathrm{cm}
$$

1. Calculate the value of $\rho$.
2. Derive the formula for relative uncertainty using the total differential method.
3. Indicate which measurement gives the largest contribution to the uncertainty.

---

## Problem 4 – Linear regression and determination of acceleration due to gravity (parameter estimation)

Free fall model:

$$
h = \frac{1}{2} g t^2
$$

Data:

$$
h\ [\mathrm{m}] = [0.20,\ 0.40,\ 0.60,\ 0.80,\ 1.00]
$$

$$
t\ [\mathrm{s}] = [0.202,\ 0.287,\ 0.351,\ 0.404,\ 0.452]
$$

1. Transform the model into a linear form:

   $$
   h = k t^2
   $$

2. Perform a linear regression of $h$ with respect to $t^2$.
3. Determine $g$.
4. Estimate the uncertainty $u(g)$.
5. Evaluate the goodness of fit (residual analysis or coefficient of determination $R^2$).

---

## Problem 5 – Systematic vs. statistical errors

Three groups of students measure the length of the same rod.

The results obtained:

Group A:

$$
x = [10.01,\ 9.99,\ 10.02,\ 9.98,\ 10.00]
$$

Group B:

$$
x = [10.42,\ 10.40,\ 10.41,\ 10.43,\ 10.39]
$$

Group C:

$$
x = [9.6,\ 10.5,\ 10.2,\ 9.8,\ 10.4]
$$

1. For each group, calculate:
   - the mean,
   - the standard deviation,
   - the uncertainty of the mean.
2. Assume that the true value is:

   $$
   x_{\mathrm{true}} = 10.00
   $$

   Compare the groups' results with the true value.
3. Determine for each group:
   - whether the statistical error dominates,
   - whether a systematic error occurs.
4. Propose possible causes of the systematic error (min. 2).
5. Explain why increasing the number of measurements does not eliminate the systematic error.
6. (Reflection) Is the result:

   $$
   x = 10.41 \pm 0.01
   $$

   "better" than:

   $$
   x = 10.00 \pm 0.20
   $$

   Justify.

Answer: calculations + interpretation.

---

## Problem 6 (HTML) – Central Limit Theorem

Build an application simulating the distribution of the sample mean.

Requirements:

1. Choice of source distribution (uniform / exponential / two-point / normal).
2. Setting the sample size $n$ and the number of samples $N$.
3. Generating $N$ means $\bar{x}$.
4. Histogram of the $\bar{x}$ distribution.
5. Comparison of the empirical deviation with the theoretical value $\sigma/\sqrt{n}$.
6. Ability to overlay a Gaussian curve.
7. Brief analysis of the effect of $n$ on the shape of the distribution.

To be submitted: HTML file + description of conclusions.

---

## Problem 7 (HTML) – Simple pendulum: measurement of $g$

We want to build an application to measure the acceleration due to gravity $g$ using a simple pendulum by measuring the period of oscillations.

$$
g=4\pi^2 \frac{L}{T^2}
$$

Application requirements:

1. The user sets the length $L$ and its uncertainty $u(L)$.
2. The first press of the spacebar starts the motion and the stopwatch.
3. Subsequent presses register successive passes through the minimum.
4. The application saves the times $t_i$ and determines the periods:

   $$
   T_i = t_{i+1} - t_i
   $$

5. Calculate:
   - the mean period $\bar{T}$,
   - the standard deviation $s_T$,
   - the uncertainty of the mean:

     $$
     u(T) = \frac{s_T}{\sqrt{n}}
     $$

6. Determine:

   $$
   g = 4\pi^2 \frac{L}{\bar{T}^2}
   $$

7. Apply the propagation of uncertainty:

   $$
   u(g)=\sqrt{\left(\frac{\partial g}{\partial L}u(L)\right)^2+
   \left(\frac{\partial g}{\partial T}u(T)\right)^2}
   $$

8. Display the result:

   $$
   g = \hat{g} \pm u(g)
   $$

   and the percentage contributions of uncertainty from $L$ and from $T$.

To be submitted: HTML file + report from min. 5 periods.

---

## Problem 8 (HTML) – Mass-spring oscillator: frequency measurement and determination of $k$

We want to build an application to determine the spring constant $k$ by measuring the period of oscillations of a mass-spring system.

$$
k = 4\pi^2 \frac{m}{T^2}
$$

Application requirements:

1. The user sets the mass $m$ and its uncertainty $u(m)$.
2. The first press of the spacebar starts the motion and the stopwatch.
3. Subsequent presses register successive passes through the minimum.
4. The application determines:
   - the periods $T_i$,
   - the mean period $\bar{T}$,
   - $s_T$,
   - $u(T) = \frac{s_T}{\sqrt{n}}$
5. Determine the frequency:

   $$
   f = \frac{1}{\bar{T}}
   $$

   and its uncertainty:

   $$
   u(f) = \frac{u(T)}{\bar{T}^2}
   $$

6. Determine the spring constant:

   $$
   k = 4\pi^2 \frac{m}{\bar{T}^2}
   $$

7. Apply the propagation of uncertainty:

   $$
   u(k)=\sqrt{\left(\frac{\partial k}{\partial m}u(m)\right)^2+
   \left(\frac{\partial k}{\partial T}u(T)\right)^2}
   $$

8. Display the result:

   $$
   k = \hat{k} \pm u(k)
   $$

   and the percentage contributions of uncertainty from $m$ and from $T$.

To be submitted: HTML file + report from min. 10 periods.