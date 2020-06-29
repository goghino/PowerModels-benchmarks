## Overview

The main focus of the project is to perform a series of benchmarks using optimization problems in the power grid, namely optimal power flow (OPF).
Recently, we have been doing an extensive evaluation of the optimization software using MATLAB toolchain, but we would like to see how do similar
tools implemented in Julia behave and perform. We will be using PowerModels tool [1,2].

Basically we have the OPF benchmark suite now in MATLAB and running all benchmarks sequentially. It would be nice to have a script that submits
parallel jobs containing individual benchmark instances. We would like to focus on following aspects of the OPF problem:
* Underlying optimizer (e.g. Ipopt, Knitro, etc...)
* Mathematical formulations
* Optimality gap between the convex formulations and the fully nonlinear models
    
[1] PowerModels home page, [https://lanl-ansi.github.io/PowerModels.jl/stable/]

[2] C. Coffrin, R. Bent, K. Sundar, Y. Ng and M. Lubin, "PowerModels. JL: An Open-Source Framework for Exploring Power Flow Formulations," 2018 Power Systems Computation Conference (PSCC), Dublin, 2018, pp. 1-8, doi: [10.23919/PSCC.2018.8442948](https://ieeexplore.ieee.org/document/8442948).

## Tasks
- [ ] Familiarize with the PowerModels framework
- [ ] Install Julia and PowerModels
- [ ] Run demo OPF problems, change parameters in the model and solution method
- [ ] Keep the project Wiki pages up to date during the process [see here](https://help.github.com/en/github/building-a-strong-community/documenting-your-project-with-wikis)
