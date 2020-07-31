Instructions how to obtain the Knitro licence -------------------------------
create a knitro account : https://www.artelys.com/
download the binaries of knitro for linux 64
move it to the home folder of the cluster
run onto gpu compute node
 srun -p gpu --nodelist=icsnode11 ./get_machine_ID 
paste into the request form the machine_ID to get the license
copy the license file to the home folder of the cluster

Follow the quick-start guide instruction:  https://jump.dev/KNITRO.jl/latest/
 export LD_LIBRARY_PATH="$HOME/knitro-12.2.2-Linux-64/lib:$LD_LIBRARY_PATH"
At the Julia prompt, run Pkg.add("KNITRO").
Test that KNITRO.jl works by runnning Pkg.test("KNITRO").