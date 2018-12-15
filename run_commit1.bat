echo commit source rst
cd
del *.bak /s/q && git add * && git commit -m "update%date% %time%" && git push 
