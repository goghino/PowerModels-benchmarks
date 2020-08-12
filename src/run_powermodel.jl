using PowerModels
using Ipopt
using KNITRO

in_case=ARGS[1]
optimizer=ARGS[2]
formulation=ARGS[3]
println(in_case)
println(optimizer)
println(formulation)

# exact non-convex formulations for now (ACP,ACR,ACT,IVR)
if (formulation=="ACP")
	type_formulation = ACPPowerModel
elseif (formulation=="ACR")
	type_formulation = ACRPowerModel
elseif (formulation=="ACT")
	type_formulation = ACTPowerModel	
elseif (formulation=="IVR")
	type_formulation = IVRPowerModel
elseif (formulation=="DCP")
	type_formulation = DCPPowerModel
elseif (formulation=="SOCW")
	type_formulation = SOCWRPowerModel
elseif (formulation=="QCRM")
	type_formulation = QCRMPowerModel
elseif (formulation=="SOCBF")
	type_formulation = SOCBFPowerModel
else
	println("Error: wrong formulation")
end

if (optimizer=="knitro")
	result = run_opf(in_case, type_formulation, with_optimizer(KNITRO.Optimizer))
elseif (optimizer=="ipopt")
	result = run_opf(in_case, type_formulation, with_optimizer(Ipopt.Optimizer))
else
	println("Error: wrong optimizer")
end

println("Time to Solution........:",result["solve_time"])
#println("Final cost..............:")
#println("Constraint violation....:")
