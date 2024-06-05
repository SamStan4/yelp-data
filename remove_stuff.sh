file1="yelp_business.txt";
file2="yelp_user.txt"
file3="yelp_checkin.txt"
file4="yelp_review.txt"

if [ -e $file1 ]; then
    rm $file1
fi

if [ -e $file2 ]; then
    rm $file2
fi

if [ -e $file3 ]; then
    rm $file3
fi

if [ -e "$file4" ]; then
    rm $file4
fi