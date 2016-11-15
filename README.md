Bank Simulation
--------------------
This is a simulation of a bank with the next features

 - People arrive at every hour.
 - People can be pref customers, regular customers or no customers at all.
 - There are servers. Each server can have a priority.
	 - Ex: Pref server will attend first the pref customers, and then help regular customers.
 - Most numbers will be Poisson-distributed random variables.
 - For rush hours, numbers will be Triangular-distributed random variables.
 - Time in the system is managed in hours. The rates of arrivals are different at every hour.
 - System also calculates which is the cost of mantaining the system, and is easily reusable to test with different configurations and probability tables.


Server configurations
	server1.json
		2 servers for preferencial customers
		1 server for normal customer
		1 server for no customer
	server2.json
		2 servers for preferencial customers
		1 server for no customer
	server3.json
		1 server for preferencial customer
		1 server for normal customer
		1 server for no customer
