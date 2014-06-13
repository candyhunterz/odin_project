function sum(array) {
    var n = 0;
    for (var i = 0; i<array.length ; i++)
        n = n + array[i];
        return n;
}
s = [];
var i = 0;
while (i < 1000) {
    if ((i % 3 == 0) || (i % 5 == 0)) 
        s[i] = i;
    else
        s[i] = 0;
    i++;
}    
a = [1,2,3]

        
console.log(sum(s));
    
