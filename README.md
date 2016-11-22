Bank Simulation
===============

Overview
--------

This is a simulation of a bank with the next features

 - People arrive at minute (Non Stationary Poisson Arrivals)
 - People can be pref customers, regular customers or no customers at all.
 - There are servers. Each server can have a priority.
	 - Ex: Pref server will attend first the pref customers, and then help regular customers.
 - Most numbers will be Poisson-distributed random variables.
 - For rush hours, numbers will be Triangular-distributed random variables.
 - Time in the system is managed in minutes. The rates of arrivals are different at every 30 minute interval.
 - System also calculates which is the cost of mantaining the system, and is easily reusable to test with different configurations and probability tables.


Assumptions
--------
The system opens at 8:30 and allows people to arrive until 15:30. People that are already in the system will be attended from 15:30 to 16:00, but end time can be changed.

Each server has his/her own hour salary. If the person has to stay more time to work, even if it is just for a small time period of the next hour, he/she gets payed an extra hour (which is the double of the salary).

The bank loses money when any type of user is waiting. For every minute waiting, the associated loss is $0.03 per non customer, $0.06 per customer, and $0.09 per preferencial customer. After the bank passes the arrival hour (15:30 by default), the associated cost of waiting is $0.80 per non customer, $1.60 per customer, and $2.40 per preferencial customer. Finally, if any client needs to be dispatched because bank is closing, the associated cost is $2.00 per non customer, $4.00 per customer, and $6.00 per preferencial customer. 

Since it is Non-Stationary Poisson, at a certain minute 2.4999 persons can arrive. Since obviously this can't happen in a real system, the simulation just has 2 arrivals. The 0.499 gets added with the arrivals of the next minute.


Run Instructions
----------------
To run the simulation with a specific server configuration (ex: server1.json), in the fifth day of the month, run:

    python simulate.py server1 1 5

Note: For creating xlsx files, XlsxWrite module is used. To run it, be sure to run the next command:
	
	sudo pip install XlsxWriter

To run the simulation multiple times, run:

	python simulate.py server1 numberOfTimes numberOfDay

For example:

	python simulate.py server1 5

Final results are printed in the terminal, and xlsx files are created in the arrivals directory. A different directory is used for every server configuration.

Server configurations
---------------------
This server configurations use json format. You can create your own server configuration with your custom information.

 - server1.json
	
	 - 2 servers for preferencial customers 		
	 - 1 server for normal customer
	 - 1 server for no customer
	
 - server2.json 		
	 - 2 servers for preferencial customers 		
	 - 1 server for no customer 	
 
 - server3.json 	
	 - 1 server for preferencial customer
	 -  1 server for normal customer 		
	 - 1 server for no customer

 - server4.json
	 - 1 server for preferencial customer

 - server5.json
	 - 1 server for preferencial customer
	 - 1 server for normal customer





