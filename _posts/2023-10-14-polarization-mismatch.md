---
layout: post
title: Polarization Mismatch
author: Johnny Champagne
math: true
tags:
date: 2023-10-14 12:00 +0500
---

I was recently tasked with calculating the Polarization Loss Factor (PLF) for various radio transmit/receive pairs. Easier said than done!

PLF is the loss incurred in a radio scenario due to the transmitter and receiver having different polarizations. If the polarizations are perfectly aligned, the signal has no losses; the PLF is 1. If, for example, the transmitter is horizontally polarized and your receiver is vertically polarized, the entire signal is lost; the PLF is 0. 
In my research, I am surprised to say that a *well-behaved*, *general* equation to describe PLF is somewhat hard to find... but it does exist!

# Polarization Representations
I think one of the reasons that this problem is difficult is that there are many ways to mathematically represent a given polarization state. The five categories of polarization state are as follows

| Polarization State |
| ----------- |
| Linear      |
| Circular, CW |
| Circular, CCW |
| Elliptical, CW |
| Elliptical, CCW |

It is worth noting that both linear and circular polarization are just limiting cases of elliptical polarization. If the eccentricity of the ellipse is zero, it is circular; if the eccentricity is infinite, it is linear.

## Representation 1: Axial Ratio / Tilt Angle

One popular way to represent polarization state is with the axial ratio ($$\varepsilon$$) and tilt angle ($$\Psi$$).  The axial ratio is defined as the ratio of the major axis of a polarization ellipse to the minor axis; the tilt angle is the angle that the ellipse is tilted (simple enough!).

Because the major axis, by definition, is larger than the minor axis, the axial ratio has a range [1,$$\infty$$). As you let $$\varepsilon$$ go to $$\infty$$, the ellipse becomes flatter, degenerating into a linear polarization. Similarly, if the major and minor axis are equal, $$\varepsilon$$ equals 1, and you have circular polarization. The table below shows how each category is described by this representation. 

| Polarization State | Representation |
| --- | ----------- |
| Linear | $$\varepsilon=\infty$$ <br> $$0\le\Psi\lt2\pi$$ |
| Circular, CW | $$\varepsilon = 1$$ <br> $$\Psi$$ undefined |
| Circular, CCW | $$\varepsilon = 1$$ <br> $$\Psi$$ undefined |
| Elliptical, CW | $$\varepsilon > 1$$ <br> $$0\le\Psi\lt2\pi$$ |
| Elliptical, CCW | $$\varepsilon > 1$$ <br> $$0\le\Psi\lt2\pi$$ |

This representation has several problems. First, the axial ratio can be (and often is) infinite. Obviously, you cannot plug $$\infty$$ into an equation. At best, you'll have to take the limiting case of an equation as $$\varepsilon\to\infty$$, which will produce a new equation. The second issue is that this representation does not describe the direction of rotation (i.e. CW or CCW). Some literature remedies this by adding a sign to $$\varepsilon$$. If $$\varepsilon<0$$, the ellipse is CCW, $$\varepsilon>1$$ CW. Using this representation (with the addition of the signed $$\varepsilon$$), we can indeed fully describe polarization mismatch. See Dr. Phillip M. Feldman's webpage on the subject. The table below shows each polarization type in this representation.

| Polarization State | Representation |
| --- | ----------- |
| Linear | $$\varepsilon=\infty$$ <br> $$0\le\Psi\lt2\pi$$ |
| Circular, CW | $$\varepsilon = 1$$ <br> $$\Psi$$ undefined |
| Circular, CCW | $$\varepsilon = -1$$ <br> $$\Psi$$ undefined |
| Elliptical, CW | $$\varepsilon > 1$$ <br> $$0\le\Psi\lt2\pi$$ |
| Elliptical, CCW | $$\varepsilon < -1$$ <br> $$0\le\Psi\lt2\pi$$ |

Even in Dr. Feldmans's page, the infinity problem rears its ugly head. As Dr. Feldman says, 

>"In the case where the wave is linearly polarized, [$$\varepsilon$$] tends to infinity and the above formula cannot be used. Taking a limit, we obtain..."

There are two $$\varepsilon$$s (transmitter and receiver) in the equation. Thus, using this representation would require three equations. Here are those equations:

$$
\label{eq:MSE}\tag{1.1}
PLF = \frac{1}{2}+\frac{1}{2}\left[\frac{4\varepsilon_1\varepsilon_2+(1-\varepsilon_1^2)(1-\varepsilon_2^2)\cos(2\beta)}{(1+\varepsilon_1^2)(1+\varepsilon_2^2)}\right]$$

Where $$\beta$$ is the difference in tilt angle between the two antennae, $$\varepsilon_1$$,$$\varepsilon_2$$ are the signed axial ratio of each antenna. Note that the symmetry in the equation between $$\varepsilon_1$$ and $$\varepsilon_2$$ mirrors the physical symmetry between transmitter and receiver.

When one of the antennae is linearly polarized, $$\varepsilon\to\infty$$, yielding this equation:

$$
\label{eq:MSEEE}\tag{1.2}
PLF = \frac{1}{2}-\frac{1}{2}\left[\frac{(1-\varepsilon^2)\cos(2\beta)}{1+\varepsilon^2}\right]$$

When both antennae are linearly polarized, $$\varepsilon_1,\varepsilon_2\to\infty$$, yielding:

$$
\label{eq:MSEE}\tag{1.3}
PLF=\frac{1}{2}+\frac{1}{2}\cos(2\beta)=\cos^2{\beta}$$

## Representation 2: Reciprocol Axial Ratio / Tilt Angle

Is there a better way? Yes.


The trick is simple: rather than using the axial ratio, we use the reciprocal of the axial ratio:
$$\varepsilon'=1/\varepsilon=\frac{\mathrm{Minor}}{\mathrm{Major}}.$$

This mathematical sleight of hand allows us to remove the infinities; the new parameter stays bounded. The table below shows the representations of each polarization type with this new parameterization.

| Polarization State | Representation |
| --- | ----------- |
| Linear | $$\varepsilon'=0$$ <br> $$0\le\Psi\lt2\pi$$ |
| Circular, CW | $$\varepsilon' = 1$$ <br> $$\Psi$$ undefined |
| Circular, CCW | $$\varepsilon' = -1$$ <br> $$\Psi$$ undefined |
| Elliptical, CW | $$0\lt\varepsilon'\lt 1$$ <br> $$0\le\Psi\lt2\pi$$ |
| Elliptical, CCW | $$-1\lt\varepsilon \lt0$$ <br> $$0\le\Psi\lt2\pi$$ |

To calculate the new formula for PLF, simply replace every instance of $$\varepsilon$$ in *Eq1.1* with $$1/\varepsilon'$$. I'll spare you the algebra and give you the new equation for PLF:

$$
\label{eq:PLF2}\tag{2}
PLF = \frac{1}{2}+\frac{1}{2}\left[\frac{4\varepsilon_1'\varepsilon_2'+(1-\varepsilon_1'^2)(1-\varepsilon_2'^2)\cos(2\beta)}{(1+\varepsilon_1'^2)(1+\varepsilon_2'^2)}\right]$$

Your eyes do not deceive you. This "new" equation with a new parameterization is identical to the old *Eq1.1*. Because of the new parameterization, the equation has no poles or infinities. Very nice!

## Representation 3: Jones Vector

One final representation I'd like to discuss is the Jones Vector representation. To motivate this, imagine a plane wave propagating in the $$\hat{z}$$ direction. The complex amplitude of the electric field can be described by the vector:

$$
\mathbf{E}(z,t)=\begin{pmatrix}
E_{x0} e^{j(kz-\omega t+\phi_x)} \\
E_{y0} e^{j(kz-\omega t+\phi_y}) \\
0
\end{pmatrix}$$

The wave is transverse, thus the $$\hat{z}$$ component is zero. The first step to getting to the Jones vector is dropping the $$\hat{z}$$ component.

$$
\mathbf{E}(z,t)=\begin{pmatrix}
E_{x0} e^{j(kz-\omega t+\phi_x)} \\
E_{y0} e^{j(kz-\omega t+\phi_y})
\end{pmatrix}$$

Next, we factor out the kz-ωt terms which are common between the two components:

$$
\begin{align*}
\mathbf{E}(z,t)&=\overbrace{\begin{pmatrix}
E_{x0} e^{j\phi_x} \\
E_{y0} e^{j\phi_y} \\
\end{pmatrix}}^{\mathrm{Jones\,Vector}}e^{j(kz-\omega t)}\\
\\
&=\tilde{\mathbf{E}}e^{j(kz-\omega t)}
\end{align*}
$$

Here we see the Jones Vector for a generalized plane wave.  The vector, which consists of two complex numbers, is parameterized by four positive, real numbers: $$E_{x0}$$, $$E_{y0}$$, $$\phi_x$$, $$\phi_y$$. The first two describe the amplitude of the wave, the latter two describe the polarization. Because amplitude is irrelevant in calculating PLF, we can normalize the vector:

$$\tilde{\mathbf{E}}^\dagger\tilde{\mathbf{E}}=1$$

Where $$\dagger$$ represents the conjugate-transpose or ‘Hermitian' operation. With this constraint, the new vector can be represented by only 3 positive real numbers:

$$
\tilde{\mathbf{E}}=\begin{pmatrix}
\cos(\theta) e^{j\phi_x} \\
\sin(\theta) e^{j\phi_y}
\end{pmatrix}$$


This representation fully describes the polarization state independent of the amplitude. One final concern with this representation is that it is not unique, that is, one polarization state can be described by more than one polarization vector. To remedy this, it is often convention to adjust the vector such that the first component of the vector is fully real. Thus, the final unique vector has the form:

$$
\tilde{\mathbf{E}}=\begin{pmatrix}
\cos(\theta) \\
\sin(\theta) e^{j\phi}
\end{pmatrix}$$

Which is parameterized by only two real numbers: $$\theta$$, $$\phi$$.
 
To calculate the PLF between two polarization states described by vectors $$\tilde{\mathbf{E}_1}$$, $$\tilde{\mathbf{E}_2}$$, you take the magnitude of their inner product:

$$PLF = \left|\tilde{\mathbf{E}}_1^\dagger \tilde{\mathbf{E}}_2\right|$$

The inner product of the two vectors is dot product of $$\tilde{\mathbf{E}}_1^*$$ and $$\tilde{\mathbf{E}}_2$$, or the product of the Hermitian of $$\tilde{\mathbf{E}}_1$$ and $$\tilde{\mathbf{E}}_2$$. This is an elegant result, which makes me fond of this representation.