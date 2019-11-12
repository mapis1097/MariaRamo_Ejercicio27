grafica27.py: data.dat
	python grafica27.py

data.dat : datos.x
	./datos.x
	./datos.x > data.dat
   
datos.x : Ejercicio27.cpp
	c++ Ejercicio27.cpp -o datos.x