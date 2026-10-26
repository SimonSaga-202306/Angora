#! /bin/bash

mtdvar=$(cat /proc/mtd | grep variable)

if [ -n "$mtdvar" ]; then
		fsvar=$(df -h | grep variable)
		
		if [ -z "$fsvar" ]; then
				echo "System mount ${mtdvar:0:4}:variable fail, rebuild fs and reboot"
				
				flash_erase /dev/${mtdvar:0:4} 0 0 &> /dev/null
				tar -xJOf /boot/variable | nandwrite /dev/${mtdvar:0:4} &> /dev/null
				
				#ubidetach /dev/ubi_ctrl -m ${mtdvar:3:1}
				#ubiattach /dev/ubi_ctrl -m ${mtdvar:3:1}
				
			  #mount -t ubifs ubi${mtdvar:3:1}:variable /var
			  reboot
		fi
fi

