This repo contains only part of the mechanoChemML library. It is simplified for the GPU Hackathon 2022 practice purpose. The original readme from the mechanoChemML library is attached at the end of this file. Same license as the mechanoChemML library is used for this repo.

# Installation

    $ git clone git@github.com:zxx2643/nn-pde-solver.git

    $ (base) conda create --name pde python==3.7

    $ (base) conda activate pde

    $ (pde) cd nn-pde-solver

    $ (pde) pip3 install -r requirements.txt

    $ (pde) python3 install_tensorflow.py

# Examples

    $ (pde) cd src/Example1_diffusion_steady_state

    $ (pde) python main.py octagon-32x32-cnn.ini


#########################################################################################################################

# mechanoChemML library

Developed by the [Computational Physics Group](http://www.umich.edu/~compphys/index.html) at the University of Michigan.

List of contributors (alphabetical order):
* Arjun Sundararajan
* Elizabeth Livingston
* Greg Teichert
* Jamie Holber
* Matt Duschenes
* Mostafa Faghih Shojaei
* Sid Srivastava
* Xiaoxuan Zhang
* Zhenlin Wang
* Krishna Garikipati

# Overview

mechanoChemML is a machine learning software library for computational materials physics. It is designed to function as an interface between platforms that are widely used for scientific machine learning on one hand, and others for solution of partial differential equations-based models of physics. Of special interest here, and the focus of mechanoChemML, are applications to computational materials physics. These typically feature the coupled solution of material transport, reaction, phase transformation, mechanics, heat transport and electrochemistry. mechanoChemML is available on PyPi at https://pypi.org/project/mechanoChemML/.

# License

BSD 4-Clause license. Please see the file LICENSE for details. 

# Installation

One can follow the installation instruction at https://mechanochemml.readthedocs.io/en/latest/installation.html to install the mechanoChemML library.

# Documentation and usage 

The documentation of this library is available at https://mechanochemml.readthedocs.io/en/latest/index.html, where one can find instructions of using the provided classes, functions, and workflows provided by the mechanoChemML library.

# Acknowledgements

This code has been developed under the support of the following:

- Toyota Research Institute, Award #849910 "Computational framework for data-driven, predictive, multi-scale and multi-physics modeling of battery materials"

# Referencing this code

If you write a paper using results obtained with the help of this code, please consider citing

- X. Zhang, G.H. Teichert, Z. Wang, M. Duschenes, S. Srivastava, A. Sunderarajan, E. Livingston, J. Holber, M. Shojaei, K. Garikipati (2021), mechanoChemML: A software library for machine learning in computational materials physics, arXiv preprint [arXiv:2112.04960](https://arxiv.org/abs/2112.04960).
