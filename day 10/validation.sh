read -p "enter name:" name  #to enter the name 
read -p "enter Age:" age	# to enter age
if [ -z $name  ]; then	# checks whether the name is empty or not
	echo "empty"
else
	echo $name
fi

if [[ $name =~ ^[A-Za-z]+$ ]] && (( age > 0 && age < 100 )); then #
echo "valid name"
else
echo "invalid"
fi
