/* ************************************************** 
   Taller de Buses - Organizacion del computador I
      (por compatibilidad se omiten tildes)
************************************************** */

#include <iostream>
#include <fstream>
#include <string>
#include <unistd.h>
#include "bus.h"
using namespace std;

int main(int argc, char *argv[]) {

	write(D0,-1);
	write(D1,-1);
	write(D2,-1);
  
	bool clk = false;
	while(1) {
		if(clk) write(CLK,1); else write(CLK,0);
		cout << clk << endl;
		sleep(1);
		clk = !clk;
	}
}
