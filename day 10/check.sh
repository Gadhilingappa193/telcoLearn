if [ $UID -eq 0 ]; then
echo "Root User"
else
echo "normal user"
fi

read -p "enter num1:" num1	
read -p "enter num2:" num2
if [ $num1 -eq $num2 ]; then
echo "same"
else
echo "different"
fi

