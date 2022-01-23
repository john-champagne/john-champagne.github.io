---
layout: post
title: Orthogonality of Hermite polynomials
author: Johnny Champagne
math: true
tags:
- math
- proof
date: 2021-03-03 20:00 +0500
---
This is a problem I encountered in one of my math classes. I enjoyed the problem and figured I'd document the results.

___

# Problem

The n<sup>th</sup> degree Hermite polynomial, $$H_{n}(x)$$, is defined as

$$
H_{n}(x) = (-1)^n e^{x^2}\frac{d^n}{dx^n}e^{-x^2}
$$

In this post, I will prove that

$$
\int_{-\infty}^{\infty}{H_n(x)H_m(x)e^{x^2}dx=2^{n}n!\sqrt{\pi}\delta_{nm}}
$$

## 1. Recurrence relationship

We will first take the derivative of the Hermite polynomial

$$
\frac{d}{dx}H_n(x) =  \frac{d}{dx}\left[(-1)^n e^{x^2}\frac{d^n}{dx^n}e^{-x^2}\right]
$$

$$
= (-1)^n \left[ 2xe^{x^2}\frac{d^n}{dx^n}e^{-x^2} + e^{x^2}\frac{d^{n+1}}{dx^{n+1}}e^{-x^2} \right]
$$

$$
= (-1)^n \left[ 2xe^{x^2}\frac{d^n}{dx^n}e^{-x^2} + e^{x^2}\frac{d^{n}}{dx^{n}}(-2xe^{-x^2}) \right]
$$

$$
= (-1)^n \left[ 2xe^{x^2}\frac{d^n}{dx^n}e^{-x^2} - 2e^{x^2}\frac{d^{n}}{dx^{n}}(xe^{-x^2}) \right]
$$

Focusing for a moment on the second term in this result, we will expand the n<sup>th</sup> derivative using the General Leibniz rule:

$$
\frac{d^{n}}{dx^{n}}(xe^{-x^2}) = \sum_{k=0}^{n} {n \choose k} x^{(n-k)} (e^{-x^2})^{(k)}
$$

$$
= x \frac{d^n}{dx^n}e^{-x^2} + n\frac{d^{n-1}}{dx^{n-1}}e^{-x^2}
$$

Substituting this result into the above equation, we get

$$
= (-1)^n \left[ 2xe^{x^2}\frac{d^n}{dx^n}e^{-x^2} - 2xe^{x^2}\frac{d^n}{dx^n}e^{-x^2} -2ne^{x^2}\frac{d^{n-1}}{dx^{n-1}}e^{-x^2}\right]
$$

$$
= (-1)^n \left[-2ne^{x^2}\frac{d^{n-1}}{dx^{n-1}}e^{-x^2}\right]
$$

$$
= (2n)\left((-1)^{n-1} e^{x^2}\frac{d^{n-1}}{dx^{n-1}}e^{-x^2}\right)
$$

$$
\boxed{= 2nH_{n-1}(x)}
$$

## 2. Orthogonality

With this recurrence relationship derived, we return to the original problem. We will first consider the case for $$n\neq m$$. Without loss of generality, we will say that $$m > n$$. A direct integration follows:

$$
\int_{-\infty}^{\infty}H_n(x)H_m(x)e^{-x^2}dx
$$

Substituting in the definition of the Hermite polynomial:

$$
= (-1)^m\int_{-\infty}^{\infty}H_n(x)\frac{d^m}{dx^m}e^{-x^2}dx
$$

Using integration by parts, we get

$$
= (-1)^m\left[H_n(x)\frac{d^{m-1}}{dx^{m-1}}e^{-x^2}\right]_{-\infty}^{\infty} -(-1)^m\int_{-\infty}^{\infty}H'_n(x)\frac{d^{m-1}}{dx^{m-1}}e^{-x^2}dx
$$


The left term is a polynomial term multiplied by an $$e^{-x^2}$$. Regardless of the polynomial, the exponential term will ultimately dominate the expression as $$x \to \pm \infty$$. Thus, this term is zero.

$$
= -(-1)^m \int_{-\infty}^{\infty}H'_n(x)\frac{d^{m-1}}{dx^{m-1}}e^{-x^2}dx
$$

Repeating the integration by parts $$m$$ times, we get

$$
= (-1)^{2m} \int_{-\infty}^{\infty}\left(\frac{d^m}{dx^m}H_n(x)\right)e^{-x^2}dx
$$

$$
= \int_{-\infty}^{\infty}\left(\frac{d^m}{dx^m}H_n(x)\right)e^{-x^2}dx
$$

Because $$m>n$$, and $$H_n(x)$$ is an n<sup>th</sup> order polynomial, the m<sup>th</sup> order derivative of $$H_n(x)$$ is zero. Thus, the integral is zero.

We now consider the case of $$n=m$$. In this case, the problem proceeds in the same way, with $$m$$ repeated integration by parts.

$$
= \int_{-\infty}^{\infty}\left(\frac{d^m}{dx^m}h_m(x)\right)e^{-x^2}dx
$$

In this case, however, the derivative is not equal to zero. To derive the value of this derivative, we use the recurence relationship derived above.

$$
= \int_{-\infty}^{\infty}2^mm!H_0(x)e^{-x^2}dx
$$

$$
= 2^mm!H_0(x)\int_{-\infty}^{\infty}e^{-x^2}dx
$$

The $$0$$<sup>th</sup> Hermite polynomial is $$1$$, and the integral to the right evaluates to $$\sqrt{\pi}$$. Thus, the final result

$$
= 2^mm!\sqrt{\pi}
$$

$$
\blacksquare
$$
