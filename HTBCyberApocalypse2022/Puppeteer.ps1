﻿[byte[]] $stage1 = 0x99, 0x85, 0x93, 0xaa, 0xb3, 0xe2, 0xa6, 0xb9, 0xe5, 0xa3, 0xe2, 0x8e, 0xe1, 0xb7, 0x8e, 0xa5, 0xb9, 0xe2, 0x8e, 0xb3;
[byte[]] $stage2 = 0xac, 0xff, 0xff, 0xff, 0xe2, 0xb2, 0xe0, 0xa5, 0xa2, 0xa4, 0xbb, 0x8e, 0xb7, 0xe1, 0x8e, 0xe4, 0xa5, 0xe1, 0xe1;
[array]::Reverse($stage2);
$stage3 = $stage1 + $stage2;
$flag = ''
foreach($i in $stage3){
    $i = $i -bxor 0xd1;
    $decrypted = [System.Text.Encoding]::ASCII.GetString($i)
    $flag +=$decrypted
    }
$flag