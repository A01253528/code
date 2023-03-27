#include <xc.h>
#include "config.h" // Configuration bits file stored in a header file
#define _XTAL_FREQ 20000000 //define crystal frequency to 20MHz

// This array stores binary bit pattern that will be send to PORTD
unsigned char binary_pattern[]={0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F};

void main(void) 
{
    TRISD = 0x00; //define PORTD as a output pin
    while(1)
    {
        //this loop sends all binary patterns to PORTD
        for (int i=0;i<10;i++)
        {
            PORTD = binary_pattern[i];
            __delay_ms(1000);  //add delay of one second
        }
    }
    return;
}