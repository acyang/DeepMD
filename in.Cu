units           metal
atom_style      atomic
boundary	    p p p

lattice			fcc 3.615
region			cubic block 0 10 0 10 0 10
create_box		1 cubic
create_atoms	1 box 
mass            1 63.55
print ${rseed}
velocity        all create 300.0 ${rseed} mom yes rot yes dist gaussian

pair_style		eam
pair_coeff		1 1 Cu_u3.eam

neighbor		2.0 bin
neigh_modify	every 2 delay 20 check yes   ## 20+1 step=>check
timestep	    0.001   #1fs

thermo          1000
thermo_style    custom step time temp press vol pe ke etotal enthalpy
thermo_modify   flush yes

variable        a1 equal step
variable        a2 equal time
variable        a3 equal temp
variable        a4 equal press
variable        a5 equal vol
variable        a6 equal "pe/atoms"
variable        a7 equal "ke/atoms"
variable        a8 equal etotal
variable        a9 equal enthalpy
fix             tdo all print 1000 "${a1} ${a2} ${a3} ${a4} ${a5} ${a6} ${a7} ${a8} ${a9}" file tdo.txt title "Step Time Temp Press Volume PotEng KinEng TotEng Enthalpy" screen no
min_style       cg
minimize        0.0 1.0e-6 20000 200000

fix		        1 all nve
fix				2 all temp/rescale 10 300.0 300.0 10.0 0.8

write_dump      all cfg initial.cfg mass type xs ys zs vx vy vz modify element Cu

dump            1 all cfg 10000 dump.*.cfg mass type xs ys zs vx vy vz fx fy fz
dump_modify     1 element Cu pad 6

run	            100000

unfix           1
unfix           2

fix             3 all npt temp 300.0 300.0 100.0 iso 1.01325 1.01325 1000.0

run	            100000