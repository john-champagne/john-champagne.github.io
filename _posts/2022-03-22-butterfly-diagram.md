---
layout: post
title: Butterfly Diagrams
author: Johnny Champagne
math: true
tags:
- signal-processing
date: 2022-03-22 13:56 +0500
---

If you've ever taken a course in DSP, you've probably encountered the butterfly diagram. The diagram is meant to illustrate the symmetry used in the Cooley-Tukey FFT. In case you've never seen one, take a look at the figure below.


![Butterfly Diagram](/assets/2022-03-22-butterfly-diagram/butterfly.svg)
*Source: Oppenheim & Schafer*

In this post I want to go over these diagrams and how we can use them for our signal processing applications.

# How to read a butterfly

Simply put, a butterfly diagram describes the mathematical relationship between two vectors. For those unfamiliar, I will explain how to read a butterfly diagram. Observe the simple butterfly below.

![Butterfly Diagram](/assets/2022-03-22-butterfly-diagram/butterfly-2.svg)

The diagram describes the mathematical relationship between the input vector, $$v_0$$, and the output vector, $$v_1$$. As the callouts sugest, the 'dots' represent summation points; two lines that both flow into a dot are summed together. The $$W$$ factors represent constant multiplications.

We can now write the equations for the output vector:

$$v_1[0] = v_0[0]+(W_{N}^{0})v_0[1]$$


$$v_1[1] = v_0[0]+(W_{N}^{4})v_0[1]$$

The '$$W$$ factors' are called twiddle factors, or, complex roots of unity. They are complex numbers with the form

$$W_{N}^{k} = e^{-j2\pi k/N} = \cos(2\pi k/N)-j \sin(2\pi k/N)$$

With all this in mind, you should be able to read the full butterfly diagram. Lets dig a little deeper into the structure of the diagram.

The original diagram shows an 8-point, radix-2 FFT. The diagram has four 'columns' which we can characterize as vectors. The left-most column represents the original time domain data, and the right-most vector is the Fourier transform. In general, an N point FFT will use $$\,\log_2{N}+1$$ vectors. The figure below illustrates this vector formulation.

![Butterfly Diagram](/assets/2022-03-22-butterfly-diagram/butterfly-3.svg)

This formulation helps us understand how the layers of the butterfly diagram relate to eachother. As an aside, I'd like to point out that each vector can be expressed as a linear transform of the previous vector. If you express the vectors as column matrices, we can formulate this as:

$$\mathbf{v}_n^{T} = \mathbf{v}_{n-1}^{T}\mathbf{M}_{n-1}$$

By repeatedly applying this identity, we can eventually get this as a transform of the original vector:

$$\mathbf{v}_n^{T} = \mathbf{v}_{n-2}^{T}\mathbf{M}_{n-2}\mathbf{M}_{n-1}$$

$$=\mathbf{v}_{0}^{T}\mathbf{M}_{0}\mathbf{M}_{1}\ldots\mathbf{M}_{n-1}$$

$$\boxed{=\mathbf{v}_{0}^{T}\mathbf{M}_{DFT}}$$

This matrix $$\mathbf{M}_{\mathrm{DFT}}$$ is similar to the [DFT matrix](https://en.wikipedia.org/wiki/DFT_matrix).[^1]

# How to write a butterfly

Reading a butterfly diagram is one thing, but writing one is much harder. Without referencing the original diagram, I challenge you to redraw the diagram for the 8-point FFT.

Not fun, right?

Let's dig a little and see if we can identify the rules. But first, a quick word on vector indexing...

## A quick word on vector indexing

The observant reader will note that the left most column in the original diagram are not in sequential order. The order goes: 0, 4, 2, 6, 1, 5, 7. Weird indexing is a neccesary evil of the FFT process.[^2]

To obtain the new sequence order, you perform a bit reversal algorithm. Observe:

$$0\to000\xrightarrow{\text{reverse}}000\to0$$

$$1\to001\xrightarrow{\text{reverse}}100\to4$$

$$2\to010\xrightarrow{\text{reverse}}010\to2$$

$$3\to011\xrightarrow{\text{reverse}}110\to6$$

$$...$$

A number of algorithms exist to perform this reordering algorithm. See [Bit-reversal permutation](https://en.wikipedia.org/wiki/Bit-reversal_permutation#Algorithms) from Wikipedia.

For the purpose of simplicity, this article will assume that the input vector, $$v_0$$ is already reordered. $$v_0[0]=x[0],v_0[1]=x[4]$$, etc.

## Digging into the butterfly

A key observation from diagram is this: each vector element is strictly dependent on two vector elements from the previous column. Visually, this can be seen as each vector element having two lines 'pointing' towards it. We can express this mathematically like so:

$$v_n[k] = v_{n-1}[k_1]+\Big(W_{N}^{Z}\Big)v_{n-1}[k_2]$$

Where
* $$n$$ is the vector column (as illustrated above)
* $$k$$ is the vector row

From here, we just need to solve for the unknowns: $$k_1$$, $$k_2$$, and $$Z$$. My personal preference is to use an intermediate variable, $$s$$, to make the closed form equations a little easier to parse. $$s$$ is either a 1 or a zero, and is described by the formula below.[^3]

$$s(n,k)=\mathrm{round}\bigg(\frac{k\mod 2^{n}}{2^{n}}\bigg)$$

If you're programming, you can use the this bitwise with the following code (the s stands for 'spaghetti code')
```
def s(n,k):
    return (k & ((1 << n)-1)) >> (n-1)
```

# Endnotes
[^1]:The only difference is that $$v_0$$ is rearanged, which shifts around the matrix around a bit. The general theory is the same.
[^2]:Although *where* the reordering happens can be changed. Decimation-in-Time FFTs have a reordered input vector and an in-order output vector. Decimation-in-frequency FFTs have in-order inputs and reordered outputs.
[^3]:In some texts, $$s$$ is expressed as the 'sign' of the twiddle factor.