#Decided to bruteforce the code through python

#Variables from Assembly Code
xor_number = 1333337
add_number = 1337
sub_number = 133337

#This is the same process the Assembly puts our input through

for i in range(0000,99999999):
	
  #Convert to string and pad with leading zeros since input has to be at least 4 bytes (according to the assembly code)
  beginning = str(i).zfill(4)
  
  #convert back to int and start following the assembly
	first_step = int(beginning) ^ xor_number
	second_step = first_step + add_number
	third = second_step - sub_number
	#This is where it gets tricky. EAX * EAX * EAD basically means EAX * 3, don't get confused.
  fourth = third * 3
	#Another tricky EAX * 3.
  fifth = fourth * 3
  #EAX * EAX
	sixth = fifth * 2
  #Found out SAL means * 2 in this instance
  #https://c9x.me/x86/html/file_module_x86_id_285.html
	seventh = sixth * 2
  #check to see what makes the cmp intruction true!
	if seventh == 43270380:
		print(i)

		#THIS IS THE ASSEMBLY GIVEN
#flag_checker:
#        push    rbp
#        mov     rbp, rsp
#        mov     DWORD PTR [rbp-4], edi
#        xor     DWORD PTR [rbp-4], 1333337
#        add     DWORD PTR [rbp-4], 1337
#        sub     DWORD PTR [rbp-4], 133337
#        mov     edx, DWORD PTR [rbp-4]
#        mov     eax, edx
#        add     eax, eax
#        add     eax, edx
#        mov     DWORD PTR [rbp-4], eax
#        mov     edx, DWORD PTR [rbp-4]
#        mov     eax, edx
#        add     eax, eax
#        add     eax, edx
#        add     eax, eax
#        mov     DWORD PTR [rbp-4], eax
#        sal     DWORD PTR [rbp-4]
#        cmp     DWORD PTR [rbp-4], 43270380
#        jne     .L2
#        mov     eax, 1
#        jmp     .L3
#.L2:
#        mov     eax, 0
#.L3:
#        pop     rbp
#        ret
#.LC0:
#        .string "Enter the secret number: "
#.LC1:
#        .string "%d"
#.LC2:
#        .string "Correct number :D"
#.LC3:
#        .string "Wrong number :p"
#main:
#        push    rbp
#        mov     rbp, rsp
#        sub     rsp, 16
#        mov     edi, OFFSET FLAT:.LC0
#        mov     eax, 0
#        call    printf
#        lea     rax, [rbp-8]
#        mov     rsi, rax
#        mov     edi, OFFSET FLAT:.LC1
#        mov     eax, 0
#        call    __isoc99_scanf
#        mov     eax, DWORD PTR [rbp-8]
#        mov     edi, eax
#        call    flag_checker
#        mov     DWORD PTR [rbp-4], eax
#        cmp     DWORD PTR [rbp-4], 0
#        je      .L5
#        mov     edi, OFFSET FLAT:.LC2
#        call    puts
#        jmp     .L6
#.L5:
#        mov     edi, OFFSET FLAT:.LC3
#        call    puts
#.L6:
#        mov     eax, 0
#        leave
#        ret
