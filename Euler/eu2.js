/*
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
*/

function fib(n) {
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;
    else 
        return fib(n-1) + fib(n-2);
}

s= [];
for (var i = 0; i < 10; i++)
    s[i] = fib(i);

function sumfib(array) {
    var sum = 0;
    for (var i =0; i<array.length; i++)
        if ( array[i] % 2 == 0)
            sum = sum + array[i];
    return sum;
}

console.log(sumfib(s));

    

