using PowerModels
using Ipopt
using KNITRO

in_case=ARGS[1]
optimizer=ARGS[2]
formulation=ARGS[3]
println(in_case)
println(optimizer)
println(formulation)

# see if initializing the exact algorithm with the solution of the convex model helps to reduce the number of iterations (and thus overall time)
# exact non-convex formulations for now (ACP,ACR,ACT,IVR)
if (formulation=="ACP")
	type_formulation = ACPPowerModel
elseif (formulation=="ACR")
	type_formulation = ACRPowerModel
elseif (formulation=="ACT")
	type_formulation = ACTPowerModel	
else
	println("Error: wrong formulation")
end

data = PowerModels.parse_file(in_case)

if (optimizer=="knitro")
	convex_result = run_opf(data, DCPPowerModel, with_optimizer(KNITRO.Optimizer))
	PowerModels.update_data!(data, convex_result["solution"])
	result = run_opf(data, type_formulation, with_optimizer(KNITRO.Optimizer))
elseif (optimizer=="ipopt")
	convex_result = run_opf(data, DCPPowerModel, with_optimizer(Ipopt.Optimizer))
	PowerModels.update_data!(data, convex_result["solution"])
	result = run_opf(data, type_formulation, with_optimizer(Ipopt.Optimizer))
else
	println("Error: wrong optimizer")
end

println("Time to Solution........:",result["solve_time"])
#println("Final cost..............:")
#println("Constraint violation....:")
