.global _main
.section .text

bin:
.asciz "/bin/sh"

_main:

#syscall# -> eax 
#/bin/sh -> ebx
#1. exc 2. edx 3. esi 4. edi 5. ebp

pushl	%ebp
movl	%esp,%ebp
subl $8, %esp
movl $bin, %edi
movl %edi, -8(%ebp)
movl $0, -4(%ebp)
movl $11, %eax	
movl $bin, %ebx			
leal -8(%ebp), %ecx
movl $0, %edx
int $0x80


leave
ret
