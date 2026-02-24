# Week 2 Lab: Wireless Link Budget Analysis

## Topic

Physical Layer -- Wireless Communications (Lecture 4)

------------------------------------------------------------------------

## Objective

To analyze a wireless communication link using the Free Space Path Loss
(FSPL) model and determine whether the link is viable under realistic
conditions.

------------------------------------------------------------------------

## 1. Free Space Path Loss Model

The Free Space Path Loss formula (in dB) is:

L_FSPL = 32.45 + 20 log10(f_MHz) + 20 log10(d_km)

Where: - f = frequency in MHz - d = distance in kilometers

------------------------------------------------------------------------

## 2. Example 1: 2.4 GHz WiFi Link at 100 meters

Parameters: - Frequency = 2400 MHz - Distance = 0.1 km - Transmit Power
(Pt) = 20 dBm - Transmit Antenna Gain (Gt) = 2 dBi - Receive Antenna
Gain (Gr) = 2 dBi

### Step 1: Calculate Path Loss

L = 32.45 + 20 log10(2400) + 20 log10(0.1)

20 log10(2400) ≈ 67.6\
20 log10(0.1) = -20

L ≈ 32.45 + 67.6 - 20\
L ≈ 80 dB

### Step 2: Calculate Received Power

Pr = Pt + Gt + Gr - L

Pr = 20 + 2 + 2 - 80\
Pr = -56 dBm

Typical WiFi receiver sensitivity is around -80 to -90 dBm.

Conclusion: The link is viable with approximately 24 dB of margin.

------------------------------------------------------------------------

## 3. Example 2: 5 GHz WiFi at 100 meters

Now change the frequency to 5000 MHz.

L = 32.45 + 20 log10(5000) + 20 log10(0.1)

20 log10(5000) ≈ 74\
20 log10(0.1) = -20

L ≈ 32.45 + 74 - 20\
L ≈ 86.45 dB

Received Power:

Pr = 20 + 2 + 2 - 86.45\
Pr ≈ -62.45 dBm

Observation: Increasing frequency increases path loss. This explains why
5 GHz WiFi generally has shorter range than 2.4 GHz WiFi.

------------------------------------------------------------------------

## 4. Effect of Distance

A key rule from the FSPL model:

-   Increasing distance by 10x adds 20 dB of loss.
-   Doubling distance adds approximately 6 dB of loss.

If distance increases from 100 m to 1 km (10x):

Additional 20 dB loss.

New received power at 1 km (2.4 GHz):

Pr = -56 - 20\
Pr = -76 dBm

This is still above receiver sensitivity but much closer to the limit.

------------------------------------------------------------------------

## 5. Realistic Environment: Path Loss Exponent Model

Real environments are not free space. A common empirical model is:

L(d) = L0 + 10n log10(d/d0)

Where: - n = path loss exponent - n ≈ 2 for free space - n ≈ 3--4 for
urban environments

If n = 3 (urban case), distance increases cause more severe loss.

At 1 km instead of adding 20 dB, loss increases by approximately 30 dB.

New received power:

Pr ≈ -56 - 30\
Pr ≈ -86 dBm

Now the link becomes marginal or unreliable.

------------------------------------------------------------------------

## 6. Key Insights

1.  Higher frequency increases path loss.
2.  Distance increases path loss logarithmically.
3.  Urban environments significantly increase attenuation.
4.  Wireless systems require a fading margin (typically 10--20 dB).
5.  Wireless performance is fundamentally constrained by physics.

------------------------------------------------------------------------

## Reflection

This lab made wireless networking feel quantitative rather than
abstract.

WiFi range is not arbitrary. It is governed by logarithmic path loss,
frequency choice, antenna gains, and environmental factors.

Understanding link budgets explains why:

-   5 GHz WiFi has shorter coverage than 2.4 GHz.
-   Urban environments reduce signal reliability.
-   Engineers must design systems with margin to handle fading and
    interference.

Wireless networking is ultimately limited by physical propagation, not
just protocol design.
