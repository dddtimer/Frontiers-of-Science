# **Using Regex for Input Validation in Argos Lessons**

In Argos, we often ask students to enter numerical answers in a specific format, such as to one decimal place. Argos allows us to validate these inputs using regular expressions (regex) when we choose the "Short text" input type. Regex is a powerful tool for ensuring that students' answers meet specific criteria and for providing targeted feedback when their answers are incorrect.

This document will explain:
1. What regex is and how it works.
2. How to create regex patterns for validating answers.
3. How to provide targeted feedback based on student inputs.
4. Examples for common scenarios such as ensuring fixed decimal places, checking numeric input, and allowing for ranges due to rounding.

---
# Table of Contents
- [Using Regex for Input Validation in Argos Lessons](#using-regex-for-input-validation-in-argos-lessons)
- [TL;DR (Quick Examples)](#tldr-quick-examples)
- [1. Introduction to Regular Expressions (Regex)](#1-introduction-to-regular-expressions-regex)
  - [What is Regex?](#what-is-regex)
  - [Key Regex Concepts and Symbols](#key-regex-concepts-and-symbols)
- [2. How to Construct Basic Regex Expressions](#2-how-to-construct-basic-regex-expressions)
  - [Matching Digits](#matching-digits)
  - [Matching Decimal Numbers](#matching-decimal-numbers)
  - [Matching Numbers Within a Range](#matching-numbers-within-a-range)
  - [Combining Patterns](#combining-patterns)
- [3. How to Create Regex for Argos](#3-how-to-create-regex-for-argos)
  - [Why Use Regex in Argos?](#why-use-regex-in-argos)
  - [Example: Confidence Interval](#example-confidence-interval)
- [4. How to Provide Targeted Feedback](#4-how-to-provide-targeted-feedback)
- [5. Examples of Common Scenarios](#5-examples-of-common-scenarios)
  - [a. Matching Fixed Decimal Places](#a-matching-fixed-decimal-places)
  - [b. Ensuring Numeric Input Only](#b-ensuring-numeric-input-only)
  - [c. Matching Numbers in a Specific Range](#c-matching-numbers-in-a-specific-range)
  - [d. Checking for Special Characters](#d-checking-for-special-characters)
- [6. Adjusting Ranges for Different Tolerances](#6-adjusting-ranges-for-different-tolerances)
- [Appendix: Advanced Regex and Useful Patterns](#appendix-advanced-regex-and-useful-patterns)
  - [Advanced: Constructing Your Own Regex](#advanced-constructing-your-own-regex)
  - [Useful Regex Patterns](#useful-regex-patterns)

---
**TL;DR (Quick Examples)**

> **1. Match a number between 23.0 and 24.0 with exactly one decimal place**:
>    ```regex
>    23\.[0-9]|24\.0
>    ```
>    - Use this to ensure students enter a number between 23.0 and 24.0.
>
> **2. Allow any number with exactly one decimal place**:
>    ```regex
>    ^\d+\.\d$
>    ```
>    - Use this to match numbers like 3.4, 12.7, or 100.5.
>
> **3. Check for numbers below 6.0 with one decimal place**:
>    ```regex
>    ([0-5]\.[0-9])
>    ```
>    - Use this to provide feedback if the student’s answer is too low.
>
> **4. Check if a student’s answer contains non-numeric characters**:
>    ```regex
>    ^\d+(\.\d+)?$
>    ```
>    - Use this to ensure the input contains only numbers and a valid decimal point.
>
> **5. Target feedback for students entering values greater than 7.0**:
>    ```regex
>    7\.[1-9]|8\.[0-9]
>    ```
>    - Use this to catch and provide feedback for students whose answer exceeds the acceptable range.

---

## **1. Introduction to Regular Expressions (Regex)**

### **What is Regex?**

Regular expressions (regex) are sequences of characters that form search patterns. In our context, we use regex to determine whether a student's input matches a specific format, such as a number within a range or with a fixed number of decimal places. This allows us to validate answers and provide specific feedback when students are incorrect.

Regex is commonly used to:
- Validate input (e.g., making sure the input is numeric).
- Search for patterns in text (e.g., looking for email addresses in a document).
- Replace or extract text (e.g., pulling numbers out of a string).

### **Key Regex Concepts and Symbols**

Here are some basic building blocks of regex that you’ll use frequently:

| Symbol         | Meaning                                        | Example                   |
|----------------|------------------------------------------------|---------------------------|
| `\d`           | Matches any digit (0–9).                       | `\d` matches 0, 1, 2, etc.|
| `\w`           | Matches any word character (a–z, A–Z, 0–9).    | `\w` matches letters/numbers|
| `\.`           | Matches a literal period (decimal point).      | `\.` matches `.` in `3.5` |
| `+`            | Matches one or more of the preceding character.| `\d+` matches 1 or more digits|
| `^`            | Matches the start of a string.                 | `^3` matches if the string starts with 3 |
| `$`            | Matches the end of a string.                   | `3$` matches if the string ends with 3 |
| `[abc]`        | Matches any one of the characters inside.      | `[1-3]` matches 1, 2, or 3 |
| `(x|y)`        | Matches either x or y.                         | `(a|b)` matches a or b    |

---

## **2. How to Construct Basic Regex Expressions**

Let's walk through some examples to see how regex patterns are built:

### **Matching Digits**

To match a single digit (0-9), we use:

```
\d
```

This pattern matches any single digit. If you wanted to match a number with multiple digits, you could add a `+` to allow one or more digits:

```
\d+
```

### **Matching Decimal Numbers**

If you want to match a decimal number, you need to include a pattern for the digits before and after the decimal point. Here's a simple example to match numbers with exactly one decimal place:

```
\d+\.\d
```

- `\d+` matches one or more digits before the decimal point.
- `\.` matches the literal decimal point.
- `\d` matches exactly one digit after the decimal point.

This pattern will match numbers like 12.3, 45.6, etc.

### **Matching Numbers Within a Range**

Regex can also be used to match numbers within specific ranges. For example, if you want to match any number from 1 to 3:

```
[1-3]
```

This will match 1, 2, or 3. For more complex ranges (like numbers between 10 and 99), you can use:

```
[1-9]\d
```

- `[1-9]` matches the first digit (1–9).
- `\d` matches the second digit (0–9).

### **Combining Patterns**

Regex allows you to combine different elements to create more complex patterns. For example, to match a number with **either zero or one decimal point**, you could use:

```
\d+(\.\d)?
```

This pattern breaks down as:
- `\d+` matches one or more digits.
- `(\.\d)?` optionally matches a decimal point followed by a digit (the `?` makes this part optional).

---

## **3. How to Create Regex for Argos**

Now that we’ve covered the basics of regex, let's apply this knowledge to our Argos lessons. In Argos, we often use the "input" question type to ask students for numerical answers.

When we choose the input type as "Short text", we can use regex to:
1. **Validate the correctness of the student’s answer**.
2. **Provide targeted feedback** based on common errors.

### **Why Use Regex in Argos?**

While Argos provides a "numeric" input type, using the "Short text" input with regex gives us more control. For example, we can:
- Validate that the number has exactly one decimal place.
- Allow answers within a range (e.g., accounting for rounding errors).
- Catch specific mistakes (like values that are too high or too low) and provide customized feedback.

### **Example: Confidence Interval**

Suppose you’re asking students to enter a confidence interval where the **correct lower bound** is 6.4. We want to allow some flexibility, accepting any number between 6.0 and 7.0 due to rounding. The regex pattern for this would be:

```regex
6\.[0-9]|7\.0
```

- `6\.[0-9]` matches numbers from 6.0 to 6.9.
- `7\.0` matches exactly 7.0.

In Argos, you can use this pattern to validate the student's answer. If their input matches the pattern, it is considered correct. You can then create targeted feedback for answers outside this range.

---

## **4. How to Provide Targeted Feedback**

Regex also lets you provide specific feedback when a student's answer is incorrect. For example, if their lower bound is **too low** (below 6.0), you can catch that with a different regex pattern:

```regex
([0-5]\.[0-9]|0)
```

This pattern matches numbers from 0.0 to 5.9. In Argos, you can use this pattern to display feedback like:

> "Your lower bound is too low. Recalculate by subtracting (2 × SE) from the sample mean."

For answers that are **too high** (greater than 7.0):

```regex
7\.[1-9]|8\.[0-9]
```

This matches numbers from 7.1 to 8.9, and you can provide feedback like:

> "Your lower bound is too high. Double-check your rounding."

---

## **5. Examples of Common Scenarios**

### **a. Matching Fixed Decimal Places**

If you need to ensure that a number has exactly **one decimal place**, use this pattern:

```regex
^\d+\.\d$
```

- `^\d+` ensures the number starts with one or more digits.
- `\.` ensures there is a decimal point.
- `\d$` ensures there is exactly one digit after the decimal.

### **b. Ensuring Numeric Input Only**

To ensure that students only input numbers (and no letters or special characters), you can use:

```regex
^\d+(\.\d+)?$
```

This will allow numbers with or without decimal points.

### **c. Matching Numbers in a Specific Range**

To match numbers within a range (e.g., between 23.0 and 24.0), use:

```regex
23\.[0-9]|24\.0
```

This will match any number from 23.0 to 23.9, as well as exactly 24.0.

### **d. Checking for Special Characters**

If you want to disallow special characters like `#`, `$`, or `@` in the input:

```regex
^[^#@$]+$
```

This ensures the input does not contain the characters `#`, `$`, or `@`. You can adapt it to disallow other characters as needed.

---

## **6. Adjusting Ranges for Different Tolerances**

If you need to adjust the tolerance for error in a range (for example, if a rounding tolerance of ±0.2 is allowed), you can simply modify the range in the regex. For instance:

- **Correct Answer Range: 5.0–5.4**:
    ```regex
    5\.[0-4]
    ```

- **Correct Answer Range with Higher Tolerance: 5.0–5.6**:
    ```regex
    5\.[0-6]
    ```

Adjust the acceptable range in the regex to meet the required tolerance for student answers.

---

## **Appendix: Advanced Regex and Useful Patterns**

### **Advanced: Constructing Your Own Regex**

Now that you understand the basics, you can start constructing your own regex patterns to meet specific needs in your lessons. Here’s a general approach to follow:

1. **Identify the pattern** you need to match (e.g., a number with two decimal places, a range of values, etc.).
2. **Use the appropriate regex symbols** (e.g., `\d`, `\.`) to construct your pattern.
3. **Test your regex** to ensure it matches all valid inputs and excludes

 invalid ones.

You can also use online tools like [regex101](https://regex101.com/) to build and test your patterns interactively.

---

### **Useful Regex Patterns**

| Pattern                       | Description                                    |
|-------------------------------|------------------------------------------------|
| `^\d+(\.\d)?$`                 | Number with exactly one decimal place          |
| `^\d+(\.\d{2,})?$`             | Number with more than one decimal place        |
| `\d+\.\d`                      | Matches a number with one decimal              |
| `^\d+$`                        | Matches integers only                         |
| `6\.[0-9]|7\.0`                | Matches numbers between 6.0 and 7.0           |
| `^[^#@$]+$`                    | Matches input without special characters       |
| `(2[3-4]\.[0-9])`              | Matches numbers between 23.0 and 24.0         |
| `([0-5]\.[0-9]|0)`             | Matches numbers below 6.0                     |
| `7\.[1-9]|8\.[0-9]`            | Matches numbers above 7.0                     |

--- 
