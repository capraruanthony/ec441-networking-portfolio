# Week 1 Report: Information vs Data in Networking

## Topic

Information: Sources and Representation (Lectures 1--2)

------------------------------------------------------------------------

## 1. What Is Information?

Information reduces uncertainty.

Shannon defined the information (surprisal) of an event with probability
p as:

I(p) = -log2(p)

Examples:

-   Fair coin (p = 0.5): I = 1 bit\
-   Rolling a 6 (p = 1/6): I ≈ 2.58 bits\
-   Certain event (p = 1): I = 0 bits

More surprising events carry more information.

------------------------------------------------------------------------

## 2. Entropy: Average Information

Entropy measures the average information of a random variable:

H(X) = - Σ (p_i \* log2(p_i))

Fair coin:\
H = 1 bit

Biased coin (0.9 / 0.1):\
H ≈ 0.47 bits

Key insight:\
Less randomness → less information required to describe outcomes.

This explains why predictable data compresses well.

------------------------------------------------------------------------

## 3. Data ≠ Information

Important distinction:

-   Information = actual content (measured in entropy)\
-   Data = representation (measured in bits/bytes)

Fundamental relationship:

Data size ≥ Information content

Example:

English text entropy ≈ 1.5 bits per character\
ASCII uses 8 bits per character

Efficiency:

1.5 / 8 ≈ 19%

ASCII stores significantly more bits than the theoretical minimum.\
In networking, redundancy may be intentionally added for error detection
(CRC, checksums) and reliability.

------------------------------------------------------------------------

## 4. Units and Networking Confusion

In networking:

-   Bit (b)\
-   Byte (B) = 8 bits\
-   Octet = 8 bits (networking term)

SI prefixes (decimal):

-   1 Mb = 10\^6 bits

Binary prefixes:

-   1 MiB = 2\^20 bytes

Important distinction:

100 Mb/s = 100,000,000 bits per second\
NOT 104,857,600 bits per second.

This matters when comparing ISP speeds, downloads, and storage capacity.

------------------------------------------------------------------------

## 5. Text Encoding and Efficiency

ASCII: - 7 bits (128 characters) - Fixed length - English only

UTF-8: - Variable length (1--4 bytes) - Backward compatible with ASCII -
Efficient for English text

Base64: - Encodes 3 bytes into 4 characters - 33% overhead - Used when
binary data must pass through text-only systems

This demonstrates a core networking tradeoff: Efficiency vs
compatibility vs readability.

------------------------------------------------------------------------

## 6. Applied Example: Encoding Comparison

Consider the string:

"Hello"

ASCII representation: 5 characters × 8 bits = 40 bits

Estimated entropy: 5 × 1.5 ≈ 7.5 bits

Efficiency: 7.5 / 40 ≈ 18.75%

Now consider:

"Hello 你好"

UTF-8 encoding: - "Hello" = 5 bytes\
- Space = 1 byte\
- Each Chinese character = 3 bytes\
- Total = 12 bytes

If encoded in Base64, size would increase by \~33%.

This shows:

-   Representation size depends on encoding\
-   Entropy sets a theoretical lower bound\
-   Text-based systems introduce overhead

------------------------------------------------------------------------

## 7. Magic Numbers and Representation

Binary files begin with identifying bytes ("magic numbers"):

-   PNG: 89 50 4E 47\
-   JPEG: FF D8 FF\
-   PDF: 25 50 44 46\
-   ELF: 7F 45 4C 46

These allow systems to identify file types and prevent
misinterpretation.

This is conceptually similar to network protocol headers, which define
how to interpret bits in packets.

------------------------------------------------------------------------

## 8. Networking Connection

Information theory underlies networking design:

-   Compression reduces bandwidth usage\
-   Protocol headers introduce overhead\
-   Base64 increases transmission size\
-   Multimedia compression makes streaming feasible

Example:

Uncompressed 1080p video at 30 fps ≈ 1.5 Gb/s\
Compressed ≈ 3--10 Mb/s

Without compression, modern networking would be impractical at scale.

------------------------------------------------------------------------

## Reflection

Before this lecture, I associated networking mostly with routing and IP
addresses.

However, this material shows that networking begins with representing
information efficiently and managing uncertainty.

Entropy explains: - Why compression works\
- Why protocols include overhead\
- Why representation choices affect performance

Understanding information theory provides a foundation for everything
that follows in networking.
