 .text   
 .globl  main       
 main:  
    lui $1, 0x00001001
    ori $9, $1, 0x00000000
    lui $1, 0x10010000
    ori $2, $1, 0x00000004
    addu $3, $2, $4
 .data
    A:.word	32
    B:.word	0x05
    C:.word	0
       
 
 