
#include "Alteri.h"
#include <xc.h>
void main(void) {
    TRISD = 0;   // Puerto D es salida 
    TRISB = 255; //Puerto B es entrada 
    RD0=1;
    return;
}

