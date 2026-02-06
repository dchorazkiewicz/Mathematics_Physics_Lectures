## Probabilistic space
# Probability Space: Theory and Examples

A probability space is a mathematical triplet $(\Omega, \mathcal{F}, P)$ that fully describes a random process. It consists of three fundamental components.

## 1. Theoretical Definition

### The Sample Space ($\Omega$)
The set of all possible distinct outcomes of the experiment.

### The Sigma-algebra ($\mathcal{F}$)
A collection of subsets of $\Omega$, known as **events**. This collection defines "what can be measured." It must satisfy three properties:

* **Non-empty:** $\Omega \in \mathcal{F}$.
* **Closed under complement:** If event $A$ is in $\mathcal{F}$, then "not A" ($A^c$) is also in $\mathcal{F}$.
* **Closed under countable unions:** If you have a sequence of events, their union is also an event.

### The Probability Measure ($P$)
A function $P: \mathcal{F} \to [0, 1]$ that assigns a probability to every event in $\mathcal{F}$. It must satisfy:

* $P(\Omega) = 1$.
* $P(\emptyset) = 0$.
* **Countable Additivity:** For mutually exclusive events $A_1, A_2, \dots$:

$$
P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)
$$

---

## 2. Example: Single Coin Toss

This is the simplest non-trivial example.

* **Experiment:** Tossing a fair coin once.
* **Sample Space ($\Omega$):** There are two possible outcomes: Heads ($H$) and Tails ($T$).

$$
\Omega = \{H, T\}
$$

* **Sigma-algebra ($\mathcal{F}$):** We need to list all possible events. Since the space is finite and small, we take the Power Set (the set of all subsets).

$$
\mathcal{F} = \big\{ \emptyset, \{H\}, \{T\}, \{H, T\} \big\}
$$

**Interpretation of $\mathcal{F}$ elements:**

* $\emptyset$: The impossible event (neither Heads nor Tails occurs).
* $\{H\}$: The event "Heads occurs".
* $\{T\}$: The event "Tails occurs".
* $\{H, T\}$: The certain event (either Heads or Tails occurs). This is equivalent to $\Omega$.

* **Probability Measure ($P$):** Assuming a fair coin:

$$
P(\{H\}) = 0.5, \quad P(\{T\}) = 0.5
$$

$$
P(\emptyset) = 0, \quad P(\Omega) = 1
$$

---

## 3. Example: Rolling a Die

A slightly more complex discrete example.

* **Experiment:** Rolling a standard six-sided die.
* **Sample Space ($\Omega$):**

$$
\Omega = \{1, 2, 3, 4, 5, 6\}
$$

* **Sigma-algebra ($\mathcal{F}$):**
    Usually, for discrete spaces, we use the Power Set ($2^\Omega$), which contains all possible combinations of outcomes.
    Size of $\mathcal{F} = 2^6 = 64$ events.

**Examples of specific events in $\mathcal{F}$:**

* **Elementary events:** $\{1\}, \{2\}, \dots$ (Rolling a specific number).
* **Compound events:**
    * $A = \{2, 4, 6\}$: The event "Rolling an even number".
    * $B = \{5, 6\}$: The event "Rolling more than 4".

* **Probability Measure ($P$):**
    For a fair die, we assign a probability of $\frac{1}{6}$ to each elementary outcome. The probability of any event $E$ is the sum of the probabilities of the outcomes in $E$.

**Calculations:**

$$
P(\{1\}) = \frac{1}{6}
$$

$$
P(\text{Even}) = P(\{2, 4, 6\}) = \frac{1}{6} + \frac{1}{6} + \frac{1}{6} = \frac{3}{6} = 0.5
$$

<div style="font-family: sans-serif; border: 1px solid #ddd; padding: 20px; border-radius: 8px; max-width: 600px; background-color: #f9f9f9; color: #333;">
    <h2 style="margin-top: 0; color: #2c3e50;">Probability Simulator</h2>

    <div style="margin-bottom: 30px; border-bottom: 1px solid #ccc; padding-bottom: 20px;">
        <h3 style="margin: 0 0 10px 0;">1. Coin Toss (Bernoulli Trial)</h3>
        <p style="font-size: 0.9em; color: #666;">Theoretical Probability: P(Heads) = 0.5, P(Tails) = 0.5</p>
        
        <button onclick="tossCoin()" style="background-color: #3498db; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-size: 14px;">Toss Coin</button>
        <button onclick="resetCoin()" style="background-color: #95a5a6; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-size: 14px; margin-left: 5px;">Reset</button>
        
        <div id="coinResult" style="font-weight: bold; margin-top: 10px; height: 24px;">Result: -</div>
        
        <div style="margin-top: 15px;">
            <div style="display: flex; align-items: center; margin-bottom: 5px;">
                <span style="width: 60px; font-size: 12px;">Heads:</span>
                <div style="flex-grow: 1; background-color: #eee; height: 20px; border-radius: 3px; overflow: hidden;">
                    <div id="barHeads" style="width: 0%; background-color: #2ecc71; height: 100%; transition: width 0.3s;"></div>
                </div>
                <span id="countHeads" style="width: 80px; text-align: right; font-size: 12px; font-family: monospace;">0 (0%)</span>
            </div>
            <div style="display: flex; align-items: center;">
                <span style="width: 60px; font-size: 12px;">Tails:</span>
                <div style="flex-grow: 1; background-color: #eee; height: 20px; border-radius: 3px; overflow: hidden;">
                    <div id="barTails" style="width: 0%; background-color: #e74c3c; height: 100%; transition: width 0.3s;"></div>
                </div>
                <span id="countTails" style="width: 80px; text-align: right; font-size: 12px; font-family: monospace;">0 (0%)</span>
            </div>
            <p style="font-size: 11px; color: #888; text-align: right; margin: 5px 0 0 0;">Total Tosses: <span id="totalCoin">0</span></p>
        </div>
    </div>

    <div>
        <h3 style="margin: 0 0 10px 0;">2. Die Roll (Uniform Distribution)</h3>
        <p style="font-size: 0.9em; color: #666;">Theoretical Probability: P(k) ≈ 16.67% for k ∈ {1..6}</p>
        
        <button onclick="rollDie()" style="background-color: #8e44ad; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-size: 14px;">Roll Die</button>
        <button onclick="resetDie()" style="background-color: #95a5a6; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-size: 14px; margin-left: 5px;">Reset</button>
        
        <div id="dieResult" style="font-weight: bold; margin-top: 10px; height: 24px;">Result: -</div>
        
        <div id="dieBars" style="margin-top: 15px;">
            </div>
        <p style="font-size: 11px; color: #888; text-align: right; margin: 5px 0 0 0;">Total Rolls: <span id="totalDie">0</span></p>
    </div>

    <script>
        // --- COIN LOGIC ---
        let coinStats = { heads: 0, tails: 0, total: 0 };

        function tossCoin() {
            // Random space: [0, 1). < 0.5 is Heads, >= 0.5 is Tails
            const isHeads = Math.random() < 0.5;
            coinStats.total++;
            
            if (isHeads) {
                coinStats.heads++;
                document.getElementById('coinResult').innerText = "Result: HEADS";
                document.getElementById('coinResult').style.color = "#2ecc71";
            } else {
                coinStats.tails++;
                document.getElementById('coinResult').innerText = "Result: TAILS";
                document.getElementById('coinResult').style.color = "#e74c3c";
            }
            updateCoinUI();
        }

        function updateCoinUI() {
            const pctHeads = coinStats.total === 0 ? 0 : (coinStats.heads / coinStats.total * 100).toFixed(1);
            const pctTails = coinStats.total === 0 ? 0 : (coinStats.tails / coinStats.total * 100).toFixed(1);

            document.getElementById('barHeads').style.width = pctHeads + '%';
            document.getElementById('barTails').style.width = pctTails + '%';
            
            document.getElementById('countHeads').innerText = `${coinStats.heads} (${pctHeads}%)`;
            document.getElementById('countTails').innerText = `${coinStats.tails} (${pctTails}%)`;
            document.getElementById('totalCoin').innerText = coinStats.total;
        }

        function resetCoin() {
            coinStats = { heads: 0, tails: 0, total: 0 };
            document.getElementById('coinResult').innerText = "Result: -";
            document.getElementById('coinResult').style.color = "#333";
            updateCoinUI();
        }

        // --- DIE LOGIC ---
        let dieStats = { counts: [0,0,0,0,0,0,0], total: 0 }; // index 0 unused

        // Init Die UI
        const dieContainer = document.getElementById('dieBars');
        let dieHTML = '';
        for(let i=1; i<=6; i++) {
            dieHTML += `
            <div style="display: flex; align-items: center; margin-bottom: 4px;">
                <span style="width: 20px; font-size: 12px; font-weight:bold;">${i}</span>
                <div style="flex-grow: 1; background-color: #eee; height: 16px; border-radius: 3px; overflow: hidden;">
                    <div id="barDie${i}" style="width: 0%; background-color: #8e44ad; height: 100%; transition: width 0.3s; opacity: 0.7;"></div>
                </div>
                <span id="countDie${i}" style="width: 80px; text-align: right; font-size: 12px; font-family: monospace;">0 (0%)</span>
            </div>`;
        }
        dieContainer.innerHTML = dieHTML;

        function rollDie() {
            // Random integer 1-6
            const result = Math.floor(Math.random() * 6) + 1;
            dieStats.total++;
            dieStats.counts[result]++;
            
            document.getElementById('dieResult').innerText = "Result: " + result;
            updateDieUI();
        }

        function updateDieUI() {
            document.getElementById('totalDie').innerText = dieStats.total;
            for(let i=1; i<=6; i++) {
                const count = dieStats.counts[i];
                const pct = dieStats.total === 0 ? 0 : (count / dieStats.total * 100).toFixed(1);
                
                document.getElementById(`barDie${i}`).style.width = pct + '%';
                document.getElementById(`countDie${i}`).innerText = `${count} (${pct}%)`;
            }
        }

        function resetDie() {
            dieStats = { counts: [0,0,0,0,0,0,0], total: 0 };
            document.getElementById('dieResult').innerText = "Result: -";
            updateDieUI();
        }
    </script>
</div>