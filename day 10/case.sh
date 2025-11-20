read -p "enter num" sh
case $sh in
1)read -p "enter the file to be added" p
  touch $p;;
2)read -p "enter the name if the dir" pp
  mkdir $pp;;
3) ls;;
8) echo "invalid";;
esac


