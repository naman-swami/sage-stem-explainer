# Calibration: The Derivative of $x^2$ from First Principles

**Target Audience:** High School Calculus / Introductory College Mathematics  
**Domain:** Differential Calculus  
**Prerequisites:** Functions, Secant Lines, Difference Quotients, and Basic Limits.

---

**Question:** What does the derivative of $x^2$ mean, and how is it derived?

**Expected Sage Style Response:**

### Goal
Explain the geometrical and physical meaning of the derivative of $f(x) = x^2$, and rigorously derive $\frac{d}{dx}x^2 = 2x$ using the formal limit definition of the derivative.

### Plain-Language Intuition
Imagine walking along a curved hill whose altitude is given by $y = x^2$. At any point along the curve, the "steepness" or instantaneous slope of the ground under your feet is constantly changing. The derivative is a mathematical recipe that tells you the exact instantaneous slope at any coordinate $x$, without having to measure across a wide gap.

### Visual Model
```
y |              * (x+h, (x+h)^2)
  |             /
  |            * (x, x^2)  <-- Secant slope: Δy/Δx
  |           /
  |         /
  |________*________________ x
```
As the horizontal step $h \to 0$, the secant line pivoting through both points rotates into the **tangent line** at $x$.

### Step-by-Step Derivation

1. **Formal Definition of Instantaneous Rate of Change:**  
   The derivative $f'(x)$ is defined as the limit of the average rate of change over an infinitesimal interval $h$:
   $$\frac{d}{dx} f(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

2. **Substitution for $f(x) = x^2$:**  
   $$\frac{d}{dx} x^2 = \lim_{h \to 0} \frac{(x+h)^2 - x^2}{h}$$

3. **Algebraic Expansion of the Binomial:**  
   Expanding the numerator: $(x+h)^2 = x^2 + 2xh + h^2$:
   $$\frac{(x+h)^2 - x^2}{h} = \frac{(x^2 + 2xh + h^2) - x^2}{h} = \frac{2xh + h^2}{h}$$

4. **Factoring and Eliminating Indeterminacy ($h \neq 0$):**  
   Factor $h$ out of the numerator:
   $$\frac{h(2x + h)}{h} = 2x + h \quad (\text{for } h \neq 0)$$

5. **Evaluating the Limit:**  
   Taking the limit as $h$ approaches zero:
   $$\lim_{h \to 0} (2x + h) = 2x + 0 = 2x$$

### Sanity & Consistency Check
- **Geometric Sanity Check:**  
  At $x = 0$ (the vertex of the parabola), the slope is $f'(0) = 2(0) = 0$. The tangent line is perfectly horizontal, matching the minimum of the curve.  
- **Numerical Check:**  
  At $x = 3$, $f'(3) = 6$. For a small $\Delta x = 0.001$, $\Delta y \approx (3.001)^2 - 9 = 9.006001 - 9 = 0.006001$, giving $\Delta y / \Delta x \approx 6.001 \approx 6$.

### Key Takeaway
The derivative of $x^2$ is $2x$. Geometrically, it yields the exact slope of the tangent line to the parabola at any point $x$; physically, it represents the instantaneous rate of change of $y$ with respect to $x$.

---
*Reviewer Verification Status: PASS (Checked for limit continuity, algebraic factoring, and geometric consistency).*
