echo commit source rst
cd
call update.bat
del *.bak /s/q && git add * && git commit -m "update%date% %time%" && git push 
