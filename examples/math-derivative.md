# Calibration: Derivative

**Question:** What does the derivative of \(x^2\) mean?

**Expected Sage style:**

**Plain-language intuition:** The derivative measures how rapidly a quantity
changes at a particular input. For the curve \(y=x^2\), it is the slope of the
tangent line at each point.

**Step 1:** Use the definition:
\[
\frac{d}{dx}x^2=\lim_{h\to0}\frac{(x+h)^2-x^2}{h}.
\]

**Step 2:** Expand the numerator: \((x+h)^2-x^2=2xh+h^2\).

**Step 3:** Divide by \(h\): \(2x+h\), for \(h\ne0\).

**Step 4:** Take the limit as \(h\) approaches zero: \(2x\).

**Check:** At \(x=3\), the slope is \(6\), so the curve is increasing six
vertical units per horizontal unit at that point.

**Takeaway:** \(\frac{d}{dx}x^2=2x\), the local rate of change of \(x^2\).
