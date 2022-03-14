 #!/bin/bash
for i in {3..15}
do
    # a=3
    # j=0
    echo Example_ds_$i/2-13.log
    while read line1
    do
        # ((j+=1))
        # if [ "$j" -eq "$a" ]
        # then
            echo $line1
            # j=0
        # fi
    done < Example_ds_$i/2-13.log
done
