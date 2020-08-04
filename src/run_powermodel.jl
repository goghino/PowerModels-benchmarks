using PowerModels
using Ipopt
using KNITRO

in_case=ARGS[1]
optimizer=ARGS[2]
println(in_case)
if(optimizer=="knitro")
	result = run_ac_opf(in_case, with_optimizer(KNITRO.Optimizer))
elseif(optimizer=="ipopt")
	result = run_ac_opf(in_case, with_optimizer(Ipopt.Optimizer))

println("Time to Solution........:",result["solve_time"])
println("Final cost..............:")
println("Constraint violation....::)
