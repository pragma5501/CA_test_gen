
n=10
start=1
end=4
for (( i=start; i<=end; i++ ))
do
    echo "problem $i test start"
    for ((j=1; j<=n; j++))
    do
        echo "----------------------------"
        python3 test_gen.py $i $j > tmp.txt # argv는 test_type random_seed
        echo "problem $i : test $j done"
        python3 main$i.py < tmp.txt

        
    done
    echo "========================"
done
