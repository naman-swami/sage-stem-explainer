# Calibration: Newton's Second Law of Motion

**Target Audience:** High School / Introductory Undergraduate Physics  
**Domain:** Classical Mechanics  
**Prerequisites:** Concept of Mass ($m$), Net Force ($\Sigma F$), Acceleration ($a$), and Rate of Change of Velocity.

---

**Question:** Why does doubling the net force double acceleration if mass stays fixed?

**Expected Sage Style Response:**

### Goal
Connect net force, inertial mass, and linear acceleration from first principles using Newton's Second Law, demonstrating direct proportionality under constant mass.

### Plain-Language Intuition
Think of pushing a shopping cart. The cart's mass represents its inertia—its natural resistance to changing its motion. If you push the cart twice as hard without changing what is inside it, you overcome that same resistance with double the effort, causing its speed to increase twice as fast every second.

### Visual Representation
```
[ Net Force: F ] ----> [ Mass: m ] ====> Acceleration: a
[ Net Force: 2F ] ---> [ Mass: m ] ========> Acceleration: 2a
```

### Step-by-Step Derivation

1. **Premise & Fundamental Definition:**  
   Newton's Second Law states that the time rate of change of momentum is directly proportional to the applied net external force:
   $$\vec{F}_{\text{net}} = \frac{d\vec{p}}{dt} = \frac{d(m\vec{v})}{dt}$$

2. **Constant Mass Assumption:**  
   In non-relativistic classical mechanics, the object's mass $m$ does not depend on time or velocity ($dm/dt = 0$). By applying the product rule:
   $$\vec{F}_{\text{net}} = m \frac{d\vec{v}}{dt} + \vec{v}\frac{dm}{dt} = m\vec{a}$$

3. **Isolating the Observable Variable (Acceleration):**  
   Dividing both sides by the scalar inertial mass $m$ ($m > 0$):
   $$\vec{a} = \frac{\vec{F}_{\text{net}}}{m}$$

4. **Applying the Scaling Transformation:**  
   Let the initial acceleration be $a_1 = F_1 / m$. When the force is doubled such that $F_2 = 2F_1$:
   $$a_2 = \frac{F_2}{m} = \frac{2F_1}{m} = 2 \cdot \left(\frac{F_1}{m}\right) = 2a_1$$

### Rigorous Sanity & Dimensional Check
- **Dimensional Verification:**
  $$[\text{Force}] = \text{N} = \text{kg} \cdot \text{m}/\text{s}^2$$
  $$[\text{Acceleration}] = \frac{[\text{Force}]}{[\text{Mass}]} = \frac{\text{kg} \cdot \text{m}/\text{s}^2}{\text{kg}} = \text{m}/\text{s}^2$$
  The dimensions are consistent.
- **Limiting Case Check:**  
  As $F_{\text{net}} \to 0$, $a \to 0$, satisfying Newton's First Law (an object in equilibrium maintains constant velocity).

### Key Takeaway
For an object with constant mass, acceleration is strictly linear and directly proportional to net applied force ($a \propto F_{\text{net}}$). Doubling the force doubles the acceleration.

---
*Reviewer Verification Status: PASS (Checked for unit consistency, Galilean invariance, and premise validity).*
