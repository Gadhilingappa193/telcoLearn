read -p "1.create, 2.Delete, 3. moviefiles. enter the number:" n

if [ $n == 1 ]; then
	read -p "enter the name of file to create:" name
	touch $name
elif [ $n == 2 ]; then
	read -p "enter the name of file to delete:" nam
	rm $nam
fi
	

